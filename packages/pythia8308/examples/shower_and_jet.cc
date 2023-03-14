//Pythia
#include "Pythia8/Pythia.h"
//Fastjet headers
#include "fastjet/ClusterSequence.hh"
#include "fastjet/Selector.hh"
#include "fastjet/tools/SubjetTagger.hh"
#include "fastjet/contrib/SoftDrop.hh"
#include "fastjet/contrib/JetTagger.hh"
#include "fastjet/contrib/BTagging.hh"




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

int main() {

  // Generator
  Pythia pythia;

  // Initialize Les Houches Event File run. List initialization information.
  pythia.readString("Beams:frameType = 4"); 
  // pythia.readString("24:onMode = off");
  // pythia.readString("24:onIfAny = 11 13");

  pythia.readString("Beams:LHEF = /data/theorie/jthoeve/ML4EFT_events/tt_ctd8/job1/Events/run_01/unweighted_events.lhe");

  pythia.init();

  // Fastjet analysis - select algorithm and parameters
  double Rparam = 0.8;
  fastjet::Strategy               strategy = fastjet::Best;
  fastjet::RecombinationScheme    recombScheme = fastjet::E_scheme;
  fastjet::JetDefinition jetDef = fastjet::JetDefinition(fastjet::antikt_algorithm, Rparam, recombScheme, strategy);

  //Print information about the jet analysis before printing the info per event.
  // cout << "Ran " << jetDef.description() << endl;
  // Fastjet input
  std::vector <fastjet::PseudoJet> input_particles;

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
  std::vector<int> event_list;
  std::vector<std::vector<double>> kinematics_vector;
  std::vector<std::string> name_vector;
  //Particle information to get the label instead of the ID of the particle
  const ParticleData& particleData = pythia.particleData;

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
  for (int iEvent = 0; ; ++iEvent) {                // you can add ; iEvent < 10 ; for fast itteration times

    // Generate events, and check whether generation failed.
    if (!pythia.next()) {

      // If failure because reached end of file then exit event loop.
      if (pythia.info.atEndOfFile()) break;

      // First few failures write off as "acceptable" errors, then quit.
      if (++iAbort < nAbort) continue;
      break;
    }
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

    //Where I think this code might go wrong is if we have to leading leptons or anti leptons, it's not made to deal with that, but I'll deal with that later
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
    // pythia.process.list();
    // cout << "iEevent = " << iEvent <<  " h_pt_ll = " << h_pt_ll[iEvent] << endl;




    // Reset Fastjet input
    input_particles.resize(0);
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

      // Store the pt of the two leading leptons, in this case we only consider electrons and muons, not tau's.
      if(abs(pythia.event[i].id()) == 11 || abs(pythia.event[i].id()) == 13){
        
        // info on i'th particle
        double particle_index = pythia.event[i].index();
        double id_lep = pythia.event[i].id();
        double px = pythia.event[i].px();
        double py = pythia.event[i].py();
        double eta = pythia.event[i].eta();

        //filter the leptons and anti leptons
        if (id_lep > 0){   //lepton
          leptons.push_back(std::make_tuple(px, py, eta));
          }
        if (id_lep < 0){   //anti lepton 
          anti_leptons.push_back(std::make_tuple(px, py, eta));
          }
      }

      // Store as input to Fastjet
      input_particles.push_back( fastjet::PseudoJet( pythia.event[i].px(),
        pythia.event[i].py(), pythia.event[i].pz(), pythia.event[i].e() ) );
    
    //end of particles in event loop
    }
  
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
  
//   #pragma region mismatch pt lead trail and w daughters
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
//   #pragma endregion mismatch pt lead trail and w daughters
//   }

// //This is usefull for a visual confirmation that the daughters of the w's are the leptons with the highest pt.
//   #pragma region visualise w daughters
  
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
//   #pragma endregion visualise w daughters

  // double px_l1 = std::get<0>(leptons[0]);
  // double py_l1 = std::get<1>(leptons[0]);
  // double px_l2 = std::get<0>(leptons[1]);
  // double py_l2 = std::get<1>(leptons[1]);
  // double ptll = sqrt(pow(px_l1 + px_l2, 2.0) + pow(py_l1 + py_l2, 2.0));

  // pt_ll.push_back(ptll);

  #pragma region fastjet
    if (input_particles.size() == 0) {
      cout << "Error: event with no final state particles" << endl;
      continue;

    }

    // // Run Fastjet algorithm
    // vector <fastjet::PseudoJet> inclusive_jets, sorted_jets;
    // fastjet::ClusterSequence clustSeq(input_particles, jetDef);

    // // For the first event, print the FastJet details
    // if (firstEvent) {
    //   cout << "Ran " << jetDef.description() << endl;
    //   cout << "Strategy adopted by FastJet was "
    //        << clustSeq.strategy_string() << endl << endl;
    //   firstEvent = false;
    // }

    // // Extract inclusive jets sorted by pT (note minimum pT of 20.0 GeV)
    // inclusive_jets = clustSeq.inclusive_jets(2.0);
    // sorted_jets    = sorted_by_pt(inclusive_jets);

    // //output the information on jets directly per event. At some point I should do this after the 
    // //event loop, but right now it's a good test. 
    // // label the columns
    // // printf("%5s %15s %15s %15s\n","jet #", "rapidity", "phi", "Et");
    
    // double Et_tot = 0;

    // for (unsigned int i = 0; i < sorted_jets.size(); i++) {
    //   Et_tot += sorted_jets[i].Et();
    // }
    // cout << "Et_tot = " << Et_tot << endl;
    // // print out the details for each jet
    // for (unsigned int i = 0; i < sorted_jets.size(); i++) {
    //   printf("%5u %15.8f %15.8f %15.8f\n",
    //   i, sorted_jets[i].rap(), sorted_jets[i].phi(),
    //   sorted_jets[i].Et());
    // }

  // Event event = pythia.event;
  // if (interesting_event_number != 0){
  //   event.list();
  // }
  // if (iEvent == 66){
  //   cout << "iEvent = " << iEvent << endl;
  //   pythia.process.list();
  // }
  #pragma endregion fastjet
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
  #pragma endregion kinematic vector sizes


  //See how many highest pt leptons didn't come from leptons
  // cout << "the number of highest pt lepton sets that don't correspond to daughters of w's = " << mismatch_pt_daught << endl;

  // Statistics
  pythia.stat();
  // export output:

  // Open output file
  std::ofstream outfile("kinematics_vector_test_jet.csv");
  kinematics_vector = {pt_l, pt_lbar, pt_l_lead, pt_l_trail, pt_ll, eta_l, eta_lbar, eta_l_lead, eta_l_trail,
                       h_pt_l, h_pt_lbar, h_pt_l_lead, h_pt_l_trail, h_pt_ll, h_eta_l, h_eta_lbar, h_eta_l_lead, h_eta_l_trail};
  name_vector = {"pt_l","pt_lbar", "pt_l_lead", "pt_l_trail", "pt_ll", "eta_l", "eta_lbar", "eta_l_lead", "eta_l_trail",
                 "h_pt_l","h_pt_lbar", "h_pt_l_lead", "h_pt_l_trail", "h_pt_ll", "h_eta_l", "h_eta_lbar", "h_eta_l_lead", "h_eta_l_trail"};

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
//g++ shower_and_jet.cc -o shower_and_jet -w -I../include -O2 -std=c++11 -pedantic -W -Wall -Wshadow -fPIC -pthread  -L../lib -Wl,-rpath,../lib -lpythia8 -ldl -I/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/include -L/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib -Wl,-rpath,/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib -lfastjet -lz