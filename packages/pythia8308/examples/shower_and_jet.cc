//Pythia
#include "Pythia8/Pythia.h"
//Fastjet headers
#include "fastjet/ClusterSequence.hh"
#include "fastjet/Selector.hh"



#include <iostream> // needed for io
#include <fstream> // needed for output vsc file
#include <cstdio>   // needed for io
//For lepton analysis
#include <vector> 
#include <algorithm>
#include <cmath>
#include <set> //for comparing the set of highest pt leptons with the set of daughters from the w's 

using namespace Pythia8;
using namespace std;


void check_vector(const std::vector<double>& vec, double a, double b);

// Function to check if a particle is a B-hadron based on its pdgId
bool is_b_hadron(int pdgId) {
    int abs_pdgId = std::abs(pdgId);
    int first_digit = abs_pdgId / 1000;
    int second_digit = (abs_pdgId / 100) % 10;
    int third_digit = (abs_pdgId / 10) % 10;

  return (first_digit == 5) || (second_digit == 5) || (third_digit == 5);
}


int main() {

  // Generator
  Pythia pythia;

  // Initialize Les Houches Event File run. List initialization information.
  pythia.readString("Beams:frameType = 4"); 
  // Turn off Multiple Parton Interactions (MPI)
  pythia.readString("PartonLevel:MPI = off");
  pythia.readString("24:onMode = off");
  pythia.readString("24:onIfAny = 11 13");
  // Loop through all particle data in Pythia
  // Loop through a reasonable range of particle IDs
    //Turn off the decay of b-mesons and b-hadrons to be able to tag b-jets
    ParticleData& particleData = pythia.particleData;
    int id = 1;     //technically we're missing id = 1, but that isn't a b-meson/b-hadrons anyway, so that's okay

    for (int i = 0; ; ++i){
        id = particleData.nextId(id);
        if (id == 0) break;
        if (is_b_hadron(id)){
          pythia.readString("HadronLevel:Decay off " + std::to_string(id));   
            if (particleData.hasAnti(id)){
                pythia.readString("HadronLevel:Decay off " + std::to_string(-id));
            }
        }
    }


  pythia.readString("Beams:LHEF = /data/theorie/jthoeve/ML4EFT_events/tt_sm/job1/Events/run_01/unweighted_events.lhe");

  pythia.init();

  // Fastjet analysis - select algorithm and parameters
  double Rparam = 0.4;
  fastjet::Strategy               strategy = fastjet::Best;
  fastjet::RecombinationScheme    recombScheme = fastjet::E_scheme;
  fastjet::JetDefinition jetDef = fastjet::JetDefinition(fastjet::antikt_algorithm, Rparam, recombScheme, strategy);

  //Print information about the jet analysis before printing the info per event.
  // cout << "Ran " << jetDef.description() << endl;
  // Fastjet input
  std::vector <fastjet::PseudoJet> input_particles, inclusive_jets, sorted_jets, b_jets;

  bool firstEvent = true; //Used later to print info for the first event
  // Allow for possibility of a few faulty events. (could maybe even leave this out)
  int nAbort = 10;
  int iAbort = 0;
  int mismatch_pt_daught = 0;
  int max_mismatch_pt_daught = 10;
  // Create a vector to store the px and py values of selected particles
  std::vector<std::tuple<double, double, double, double>> hard_leptons;
  std::vector<std::tuple<double, double, double>> p_lbar, p_l_daught, leptons, anti_leptons;
  std::vector<double> pt_l, pt_lbar, eta_lepton, eta_l, eta_lbar, eta_l_leading, eta_l_trailing, pt_ll;
  std::vector<std::pair<double, double>> w_plus_daughters, w_min_daughters;
  std::vector<double> minus_pt, h_pt_leading, h_pt_trailing, h_pt_l, h_pt_lbar, hard_px_l, hard_py_l, h_pt_ll, h_pt_l_lead, h_pt_l_trail;
  std::vector<double> h_eta_l, h_eta_lbar, h_eta_l_lead, h_eta_l_trail, pt_l_lead, pt_l_trail, eta_l_lead, eta_l_trail, pt_lep, pt_anti_lep;
  std::vector<double> b_pt_lead, b_pt_trail, b_eta_lead, b_eta_trail, pt_bbar, m_bbar;
  std::vector<double> h_pt_b, h_eta_b, h_pt_bbar, h_eta_bbar; 
  std::vector<int> event_list;
  std::vector<std::vector<double>> kinematics_vector;
  std::vector<std::string> name_vector;
  //Particle information to get the label instead of the ID of the particle
  // const ParticleData& particleData = pythia.particleData; // needed for w analysis, but doesn't work with turning off b-hadrons, can look at it later

  double hard_pt_lepton = 0.0;
  double hard_lepton_id = 0.0;

  #pragma region resize    
  pt_l.resize(0);
  pt_lbar.resize(0);
  pt_l_lead.resize(0);
  pt_l_trail.resize(0);
  pt_ll.resize(0);
  eta_l.resize(0);
  eta_lbar.resize(0);
  eta_l_lead.resize(0);
  eta_l_trail.resize(0);                
  h_pt_l.resize(0);
  h_pt_lbar.resize(0);
  h_pt_l_lead.resize(0);
  h_pt_l_trail.resize(0);
  h_pt_ll.resize(0);
  h_eta_l.resize(0);
  h_eta_lbar.resize(0);
  h_eta_l_lead.resize(0);
  h_eta_l_trail.resize(0);
  #pragma endregion resize

  // Begin event loop; generate until none left in input file.
  for (int iEvent = 0; iEvent < 20; ++iEvent) {                // you can add ; iEvent < 10 ; for fast itteration times
    bool continue_outer_loop = false;           //to "continue" in the event loop if the cuts on the jets aren't satisfied

    // Generate events, and check whether generation failed.
    if (!pythia.next()) {

      // If failure because reached end of file then exit event loop.
      if (pythia.info.atEndOfFile()) break;

      // First few failures write off as "acceptable" errors, then quit.
      if (++iAbort < nAbort) continue;
      break;
    }

    // Reset Fastjet input
    input_particles.resize(0);
    b_jets.resize(0);
    //reset the vectors for pt analysis
    leptons.resize(0);
    anti_leptons.resize(0);
    w_plus_daughters.resize(0);
    w_min_daughters.resize(0);
    minus_pt.resize(0);           //prob delete this later
  //double Et = 0;

    //I just want to look at the ancestry for the first w+ and w- in an event, so I'll make the if statement to recognize a one pass
    bool w_plus_is_executed = false;
    bool w_min_is_executed = false;
    bool plus_daught_found = false;
    bool min_daught_found = false;
    //to use the index outside of the if statement we have to define it here and putting it here also conveniently resets it every event
    int w_plus_index = -1;
    int w_min_index = -1;
    
    for (int i = 0; i < pythia.event.size(); ++i) {


      Particle& p = pythia.event[i];       
      bool isAncestorOf24 = false;
  
      if (!w_plus_is_executed){
        if (p.id() == 24){
          w_plus_index = p.index();
        w_plus_is_executed = true;
        }
      }

      if (!w_min_is_executed){
        if (p.id() == -24){
          w_min_index = p.index();
        w_min_is_executed = true;
        }
      }
      
      bool is_w_plus_dec = p.isAncestor(w_plus_index);
      bool is_w_min_dec = p.isAncestor(w_min_index);

      if (is_w_plus_dec && p.isFinal() && (abs(p.id()) == 11 || abs(p.id()) == 13)){    //we're looking for final state leptons of the electron or muon type that came from a w+
        // if (!plus_daught_found){                                                        //this if statement is to notify me if there is more than one lepton coming from the w+ boson
        double w_plus_daught_index = p.index();
        double w_plus_daught_id = p.id();
        w_plus_daughters.push_back(std::make_pair(w_plus_daught_index,w_plus_daught_id));
        // plus_daught_found = true;
        // }
        // else {
        //   throw std::runtime_error("w- has multiple daughters, the code is not made to handle this. Now you have to select the one with the highest pt, I think");
        // }
      }


      if (is_w_min_dec && p.isFinal() && (abs(p.id()) == 11 || abs(p.id()) == 13)){
        // if (!min_daught_found){
        double w_min_daught_index = p.index();
        double w_min_daught_id = p.id();
        double w_min_daught_pt = p.pT();
        minus_pt.push_back(w_min_daught_pt);
        w_min_daughters.push_back(std::make_pair(w_min_daught_index,w_min_daught_id));
        // min_daught_found = true;
        // }
        // else {
        //   throw std::runtime_error("w- has multiple daughters, the code is not made to handle this. Now you have to select the one with the highest pt, I think");
        // }
      }

      if (!pythia.event[i].isFinal())        continue;

        // info on i'th particle
        double index = pythia.event[i].index();
        double id_lep = pythia.event[i].id();
        double px = pythia.event[i].px();
        double py = pythia.event[i].py();
        double pz = pythia.event[i].pz();
        double e = pythia.event[i].e();
        double eta = pythia.event[i].eta();

      // Store the pt of the two leading leptons, in this case we only consider electrons and muons, not tau's.
      if(abs(pythia.event[i].id()) == 11 || abs(pythia.event[i].id()) == 13){

        //filter the leptons and anti leptons
        if (id_lep > 0){   //lepton
          leptons.push_back(std::make_tuple(px, py, eta));
          }
        if (id_lep < 0){   //anti lepton 
          anti_leptons.push_back(std::make_tuple(px, py, eta));
          }
      }

      // Store the momenta and index of the particles in a pseudojet
      fastjet::PseudoJet particle(px, py, pz, e);
      particle.set_user_index(index);
      input_particles.push_back(particle);

    //end of particles in event loop
    }
  
  //We want to skip the events where the b-jets don't pass the kinematic cuts. 
  #pragma region fastjet
  if (input_particles.size() == 0) {
    cout << "Error: event with no final state particles" << endl;
    continue;
  }

  fastjet::ClusterSequence clust_seq(input_particles, jetDef);


  // For the first event, print the FastJet details
  if (firstEvent) {
    cout << "Ran " << jetDef.description() << endl;
    cout << "Strategy adopted by FastJet was "
          << clust_seq.strategy_string() << endl << endl;
    firstEvent = false;
  }

  // Extract inclusive jets sorted by pT (note minimum pT of 20.0 GeV)
  double ptmin = 30; //GeV
  inclusive_jets = clust_seq.inclusive_jets(ptmin);
  sorted_jets    = sorted_by_pt(inclusive_jets);

  int num_b_jets = 0;
  // B-tagging
  for (const auto &jet : sorted_jets) {
      int b_hadron_count = 0;
      std::vector<fastjet::PseudoJet> constituents = clust_seq.constituents(jet);
      for (const auto &constituent : constituents) {
          // cout << "index constituents = " << constituent.user_index() << endl;
          int index = constituent.user_index();
          // cout << "index = " << index << endl;
          int id = pythia.event[index].id();
          // cout << "id = " << id << endl;
          if (is_b_hadron(id)) {
              b_hadron_count++;
          }

      }
      bool is_b_jet = b_hadron_count > 0;

        //This code is to only save the b-jets with the highest pt
        if (is_b_jet){
          // cerr << "num of b jets" << num_b_jets << endl;
          if (num_b_jets == 2){ 
            break;
            }
          // cerr << "pushing back b jet" << endl;
          b_jets.push_back(jet);
            num_b_jets++;
        }
      
      // std::cout << "Jet pt: " << jet.pt() << ", eta: " << jet.eta() << ", phi: " << jet.phi() << ", is b-jet? " << is_b_jet << std::endl;
  }
  if (b_jets.size()< 2){
      continue_outer_loop = true;
      continue; // Break out of the inner loop
  }
  // std::cout << "Jet pt: " << b_jets[0].pt() << ", eta: " <<  b_jets[0].eta() << ", phi: " <<  b_jets[0].phi() << std::endl;
  // std::cout << "Jet pt: " << b_jets[1].pt() << ", eta: " <<  b_jets[1].eta() << ", phi: " <<  b_jets[1].phi() << std::endl;

  // std::vector<double> b_pt_lead, b_pt_trail, b_eta_lead, b_eta_trail, pt_bbar, m_bbar;

    double b_px_lead = b_jets[0].px();
    double b_py_lead = b_jets[0].py();
    double b_pz_lead = b_jets[0].pz();
    double b_e_lead = b_jets[0].e();
    double bot_eta_lead = b_jets[0].eta();
    double b_px_trail = b_jets[1].px();
    double b_py_trail = b_jets[1].py();
    double b_pz_trail = b_jets[1].pz();
    double b_e_trail = b_jets[1].e();
    double bot_eta_trail = b_jets[1].eta();
    double bot_pt_lead = sqrt(pow(b_px_lead,2.0) + pow(b_py_lead,2.0));
    double bot_pt_trail = sqrt(pow(b_px_trail,2.0) + pow(b_py_trail,2.0));
    double botbotbar_pt = sqrt(pow(b_px_lead + b_px_trail,2.0) + pow(b_px_lead + b_py_trail,2.0));
    double mass_bbar = sqrt(pow(b_e_lead + b_e_trail,2.0) + pow(b_px_lead + b_px_trail,2.0) - pow(b_py_lead + b_py_trail,2.0) - pow(b_pz_lead + b_pz_trail,2.0));
    b_pt_lead.push_back(bot_pt_lead);
    b_eta_lead.push_back(bot_eta_lead);
    b_pt_trail.push_back(bot_pt_trail);
    b_eta_trail.push_back(bot_eta_trail);
    pt_bbar.push_back(botbotbar_pt);
    m_bbar.push_back(mass_bbar);

    //output the information on jets directly per event. At some point I should do this after the 
    //event loop, but right now it's a good test. 
    // label the columns
    // printf("%5s %15s %15s %15s\n","jet #", "rapidity", "phi", "Et");
    
    // // print out the details for each jet
    // for (unsigned int i = 0; i < sorted_jets.size(); i++) {
    //   printf("%5u %15.8f %15.8f %15.8f\n",
    //   i, sorted_jets[i].rap(), sorted_jets[i].phi(),
    //   sorted_jets[i].Et());
    // }


  #pragma endregion fastjet

  #pragma region hard_leptons
    hard_leptons.resize(0);
    //Hard scattering information
    for (int i = 0 ; i < pythia.process.size(); i++){
      if (abs(pythia.process[i].id()) == 11 || abs(pythia.process[i].id()) == 13){
        double hard_px_lepton = pythia.process[i].px();
        double hard_py_lepton = pythia.process[i].py();
        double hard_eta_lep = pythia.process[i].eta();
        // Save the id of the lepton to determine if it a lepton or anti lepton
        double hard_id_lep = pythia.process[i].id();
        hard_leptons.push_back(std::make_tuple(hard_px_lepton, hard_py_lepton, hard_eta_lep,hard_id_lep));
      }
    }
  // Sort the p_l vector in descending order of pt
  std::sort(hard_leptons.begin(), hard_leptons.end(), [](const std::tuple<double, double, double, double>& a, const std::tuple<double, double, double, double>& b) {
      double ax = std::get<0>(a);
      double ay = std::get<1>(a);
      double bx = std::get<0>(b);
      double by = std::get<1>(b);
      return std::sqrt(ax*ax + ay*ay) > std::sqrt(bx*bx + by*by);
  });


    for (int i = 0; i < 2 ; i++){   //info on hard leptons
      double hard_px_l = std::get<0>(hard_leptons[i]);
      double hard_py_l = std::get<1>(hard_leptons[i]);
      double hard_eta_l = std::get<2>(hard_leptons[i]);
      double hard_id_l = std::get<3>(hard_leptons[i]);
      if (hard_id_l > 0){   //lepton hard
        double hard_pt_l = sqrt(pow(hard_px_l,2.0)+ pow(hard_py_l,2.0));
        h_pt_l.push_back(hard_pt_l);
        h_eta_l.push_back(hard_eta_l);
      }
      if (hard_id_l < 0){   //anti lepton hard
        double hard_pt_lbar = sqrt(pow(hard_px_l,2.0)+ pow(hard_py_l,2.0));
        h_pt_lbar.push_back(hard_pt_lbar);
        h_eta_lbar.push_back(hard_eta_l);

      }
      if (i == 0){    //leading hard
        double hard_pt_l_lead = sqrt(pow(hard_px_l,2.0)+ pow(hard_py_l,2.0));
        h_pt_l_lead.push_back(hard_pt_l_lead);
        h_eta_l_lead.push_back(hard_eta_l);

      }
      if (i == 1){    //trailing hard
        double hard_pt_l_trail = sqrt(pow(hard_px_l,2.0)+ pow(hard_py_l,2.0));
        h_pt_l_trail.push_back(hard_pt_l_trail);
        h_eta_l_trail.push_back(hard_eta_l);
      }
      if (std::get<3>(hard_leptons[0])*std::get<3>(hard_leptons[1]) > 0){
        cout << "There are cases of hard scattering where the leading leptons are both particles or anti particless" << endl;
        pythia.process.list();
      }

    }
    
    double hard_px_l_lead = std::get<0>(hard_leptons[0]);
    double hard_py_l_lead = std::get<1>(hard_leptons[0]);
    double hard_px_l_trail = std::get<0>(hard_leptons[1]);
    double hard_py_l_trail = std::get<1>(hard_leptons[1]);
    double hard_pt_ll = sqrt(pow(hard_px_l_lead + hard_px_l_trail,2.0) + pow(hard_py_l_lead + hard_py_l_trail, 2.0));
    h_pt_ll.push_back(hard_pt_ll);
  #pragma endregion hard leptons


  // Sort the lepton vector in descending order of pt
  std::sort(leptons.begin(), leptons.end(), [](const std::tuple<double, double, double>& a, const std::tuple<double, double, double>& b) {
      double ax = std::get<0>(a);
      double ay = std::get<1>(a);
      double bx = std::get<0>(b);
      double by = std::get<1>(b);
      return std::sqrt(ax*ax + ay*ay) > std::sqrt(bx*bx + by*by);
  });

    // Sort the anti_lepton vector in descending order of pt
  std::sort(anti_leptons.begin(), anti_leptons.end(), [](const std::tuple<double, double, double>& a, const std::tuple<double, double, double>& b) {
      double ax = std::get<0>(a);
      double ay = std::get<1>(a);
      double bx = std::get<0>(b);
      double by = std::get<1>(b);
      return std::sqrt(ax*ax + ay*ay) > std::sqrt(bx*bx + by*by);
  });

  #pragma region w analysis1
  //sort the w+ daughters
    std::sort(w_plus_daughters.begin(), w_plus_daughters.end(), [](const std::pair<double, double>& a, const std::pair<double, double>& b) {
      double ax = std::get<0>(a);
      double ay = std::get<1>(a);
      double bx = std::get<0>(b);
      double by = std::get<1>(b);
      return std::sqrt(ax*ax + ay*ay) > std::sqrt(bx*bx + by*by);
  });

  //sort the w- daughters
    std::sort(w_min_daughters.begin(), w_min_daughters.end(), [](const std::pair<double, double>& a, const std::pair<double, double>& b) {
      double ax = std::get<0>(a);
      double ay = std::get<1>(a);
      double bx = std::get<0>(b);
      double by = std::get<1>(b);
      return std::sqrt(ax*ax + ay*ay) > std::sqrt(bx*bx + by*by);
  });
  #pragma endregion w analysis1

  // cout << "size leptons" << leptons.size() << endl;
  // for (int i = 0; i < leptons.size(); i++){
  //   double lep_x = std::get<0>(leptons[i]);
  //   double lep_y = std::get<1>(leptons[i]);
  //   cout << "leptons px = " << lep_x << endl;
  //   cout << "leptons py = " << lep_y << endl;
  // }
    //Get the kinematics for each event of the leptons
  double px_l1 = std::get<0>(leptons[0]);
  double py_l1 = std::get<1>(leptons[0]);
  double eta_l1 = std::get<2>(leptons[0]);
  double px_lbar1 = std::get<0>(anti_leptons[0]);
  double py_lbar1 = std::get<1>(anti_leptons[0]);
  double eta_lbar1 = std::get<2>(anti_leptons[0]);

  double pt_lepton = sqrt(pow(px_l1,2.0) + pow(py_l1,2.0));
  double pt_anti_lepton = sqrt(pow(px_lbar1,2.0) + pow(py_lbar1,2.0));
  double pt_llbar = sqrt(pow(px_l1 + px_lbar1,2.0) + pow(py_l1 + py_lbar1,2.0));
  pt_l.push_back(pt_lepton);
  pt_lbar.push_back(pt_anti_lepton);
  pt_ll.push_back(pt_llbar);
  eta_l.push_back(eta_l1);
  eta_lbar.push_back(eta_lbar1);

  if (pt_lepton > pt_anti_lepton){                                   
    double pt_l_leading = pt_lepton;  
    double pt_l_trailing = pt_anti_lepton;
    double eta_l_leading = eta_l1;
    double eta_l_trailing = eta_lbar1;
    pt_l_lead.push_back(pt_l_leading);
    pt_l_trail.push_back(pt_l_trailing);
    eta_l_lead.push_back(eta_l_leading);
    eta_l_trail.push_back(eta_l_trailing);
  }
  else {
    double pt_l_leading = pt_anti_lepton;  
    double pt_l_trailing = pt_lepton;
    double eta_l_leading = eta_lbar1;
    double eta_l_trailing = eta_l1;
    pt_l_lead.push_back(pt_l_leading);
    pt_l_trail.push_back(pt_l_trailing);
    eta_l_lead.push_back(eta_l_leading);
    eta_l_trail.push_back(eta_l_trailing);
  }
  
  #pragma region mismatch pt lead trail and w daughters // this code is outdated, we no longer store the index, this has to be modified
//   double index_pt1 = std::get<2>(leptons[0]);
//   double index_pt2 = std::get<2>(anti_leptons[0]);

//   double index_plus_daught = w_plus_daughters[0].first;
//   double plus_id = w_plus_daughters[0].second;
//   double index_min_daught = w_min_daughters[0].first;
//   double min_id = w_min_daughters[0].second;

//   //now we want to see if the highest pt leptons have the same index as the daughter particles from the w's. We do this by comparing the two sets of doubles
  
  
//   std::set<double> set_pt = {index_pt1, index_pt2};
//   std::set<double> set_daught = {index_plus_daught, index_min_daught};
  
//   int interesting_event_number = 0; //this makes the list not work anymore, but I'm trying to print the event record per event.

//   if (set_pt != set_daught){
//     mismatch_pt_daught +=1;
//     interesting_event_number = iEvent;
//     // cout << "w daught and pt mismatch # = " << mismatch_pt_daught << " iEvent = " << iEvent << endl;
//     double mother_index_pt1 = pythia.event[index_pt1].mother1();
//     int mother_id_pt1 = pythia.event[mother_index_pt1].id();
//     const std::string& mother_name_pt1 = particleData.name(mother_id_pt1);
//     double mother_index_pt2 = pythia.event[index_pt2].mother1();
//     int mother_id_pt2 = pythia.event[mother_index_pt2].id();
//     const std::string& mother_name_pt2 = particleData.name(mother_id_pt2);
//     // cout << "index pt1 = " << index_pt1 << " mother index of pt1 = " << mother_index_pt1 << " mother pt1 name = " << mother_name_pt1 << endl;
//     // cout << "index pt2 = " << index_pt2 << " mother index of pt2 = " << mother_index_pt2 << " mother pt2 name = " << mother_name_pt2 << endl;
//     // pythia.process.list();
//     // pythia.event.list();



//   //   if ( mismatch_pt_daught > max_mismatch_pt_daught){
//   //     throw std::runtime_error("The daughters from the w's don't all have the highest pt");
//   //   }
  #pragma endregion mismatch pt lead trail and w daughters
//   }

//This is usefull for a visual confirmation that the daughters of the w's are the leptons with the highest pt.
  #pragma region visualise w daughters
  
//   for (int i = 0; i < w_plus_daughters.size(); i++){
//   if (i > 0){
//     // cout << "w+ has multiple leptonic daughters" <<endl;  
//     // cout << "w+ daughter index by pt = " << w_plus_daughters[i].first << " w+ daughter id = " << w_plus_daughters[i].second << " pt of w+ daught = "  << endl;
//     } 
//   }

//   for (int i = 0; i < w_min_daughters.size(); i++){
//     if (i > 0){
//       // cout << "w- has multiple leptonic daughters" << endl;
//       // cout << "w- daughter index by pt = " << w_min_daughters[i].first << " w- daughter id = " << w_min_daughters[i].second << endl;
//     }
//   }

//   // cout << "leading pt lepton index = " << index_pt1 << " trailing pt lepton index = " << index_pt2 << endl;
  #pragma endregion visualise w daughters





  // End of event loop.
  }


  #pragma region kinematic vector sizes
  cout << "size pt_l = " << pt_l.size() << endl;
  cout << "size pt_lbar = " << pt_lbar.size() << endl;
  cout << "size pt_l_lead = " << pt_l_lead.size() << endl;
  cout << "size pt_l_trail = " << pt_l_trail.size() << endl;
  cout << "size pt_ll = " << pt_ll.size() << endl;
  cout << "size h_pt_l = " << h_pt_l.size() << endl;
  cout << "size h_pt_lbar = " << h_pt_lbar.size() << endl;
  cout << "size h_pt_l_lead = " << h_pt_l_lead.size() << endl;
  cout << "size h_pt_l_trail = " << h_pt_l_trail.size() << endl;
  cout << "size h_pt_ll = " << h_pt_ll.size() << endl;
  cout << "size b_pt_lead = " << b_pt_lead.size() << endl;
  cout << "size b_pt_trail = " << b_pt_trail.size() << endl;
  cout << "size b_eta_lead = " << b_eta_lead.size() << endl;
  cout << "size b_eta_trail = " << b_eta_trail.size() << endl;
  cout << "size pt_bbar = " << pt_bbar.size() << endl;
  cout << "size m_bbar = " << m_bbar.size() << endl;

  #pragma endregion kinematic vector sizes


  //See how many highest pt leptons didn't come from leptons
  // cout << "the number of highest pt lepton sets that don't correspond to daughters of w's = " << mismatch_pt_daught << endl;

  // Statistics
  pythia.stat();
  // export output:

  for (int i = 0 ; i < 10; i++){
    cout << "b_pt_lead = " << b_pt_lead[i] << endl;
    cout << "b_pt_trail = " << b_pt_trail[i] << endl;
  }


  // Open output file
  std::ofstream outfile("kinematics_vector_with_b_jets.csv");
  kinematics_vector = {pt_l, pt_lbar, pt_l_lead, pt_l_trail, pt_ll, eta_l, eta_lbar, eta_l_lead, eta_l_trail,
                       h_pt_l, h_pt_lbar, h_pt_l_lead, h_pt_l_trail, h_pt_ll, h_eta_l, h_eta_lbar, h_eta_l_lead, h_eta_l_trail,
                       b_pt_lead, b_pt_trail, pt_bbar, b_eta_lead, b_eta_trail, m_bbar};
  name_vector = {"pt_l","pt_lbar", "pt_l_lead", "pt_l_trail", "pt_ll", "eta_l", "eta_lbar", "eta_l_lead", "eta_l_trail",
                 "h_pt_l","h_pt_lbar", "h_pt_l_lead", "h_pt_l_trail", "h_pt_ll", "h_eta_l", "h_eta_lbar", "h_eta_l_lead", "h_eta_l_trail",
                 "b_pt_lead", "b_pt_trail", "pt_bbar", "b_eta_lead", "b_eta_trail", "m_bbar"};

    // Write the column names to the first row of the CSV file
    for (auto& name : name_vector) {
        outfile << name << ",";
    }
    outfile << "\n";

    // Write the data to the remaining rows of the CSV file
    for (int i = 0; i < kinematics_vector[0].size(); i++) {
        for (int j = 0; j < kinematics_vector.size(); j++) {
            outfile << kinematics_vector[j][i] << ",";
        }
        outfile << "\n";
    }
  

  
  // // Write header row
  // outfile << "pt_ll, pt_ll_daught\n";

  // // Write data rows
  // for (int i = 0; i < static_cast<int>(pt_ll.size()); ++i) {      //The static cast is used because i is a signed int and pt_ll.size is an unsigned int, this makes it a signed in.
  //   outfile1 << pt_ll[i] << "\n";
  // }

  // for (int i = 0; i < static_cast<int>(eta_l.size()); ++i) { 
  //   outfile2 << eta_l[i] << "\n";
  // }

  //   for (int i = 0; i < static_cast<int>(h_pt_ll.size()); ++i) { 
  //   outfile3 << h_pt_ll[i] << "\n";
  // }

  // // for (int i = 0; i < static_cast<int>(pt_ll.size()); ++i) {      //The static cast is used because i is a signed int and pt_ll.size is an unsigned int, this makes it a signed in.
  // //   outfile << pt_ll[i] << "," << pt_ll_daught[i] << "\n";
  // // }

  // // Close output file
  // outfile1.close();
  // outfile2.close();
  // outfile3.close();


  return 0; 
}




// 
// g++ shower_and_jet.cc -o shower_and_jet -w -I../include -O2 -std=c++11 -pedantic -W -Wall -Wshadow -fPIC -pthread  -L../lib -Wl,-rpath,../lib -lpythia8 -ldl -I/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/include -L/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib -Wl,-rpath,/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib -lfastjet -lz