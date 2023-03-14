#include "Pythia8/Pythia.h"
#include "fastjet/PseudoJet.hh"
#include "fastjet/ClusterSequence.hh"
#include <fastjet/tools/JHTopTagger.hh>
#include <iostream> // needed for io
#include <fstream> // needed for output vsc file
#include <cstdio>   // needed for io
//For lepton analysis
#include <vector> 
#include <algorithm>
#include <cmath>

using namespace Pythia8;
using namespace std;


int main() {

  // Generator
  Pythia pythia;

  // Initialize Les Houches Event File run. List initialization information.
  pythia.readString("Beams:frameType = 4");
  pythia.readString("24:onMode = off");
  pythia.readString("24:onIfAny = 11 13");


  pythia.readString("Beams:LHEF = /data/theorie/pherbsch/MG5_aMC_v3_4_1/shower_tests/sm/Events/run_01/unweighted_events_copy.lhe");

  pythia.init();

  // Fastjet analysis - select algorithm and parameters
  double Rparam = 0.8;
  fastjet::Strategy               strategy = fastjet::Best;
  fastjet::RecombinationScheme    recombScheme = fastjet::E_scheme;
  fastjet::JetDefinition jetDef = fastjet::JetDefinition(fastjet::antikt_algorithm, Rparam, recombScheme, strategy);

  //Print information about the jet analysis before printing the info per event.
  cout << "Ran " << jetDef.description() << endl;
  // Fastjet input
  std::vector <fastjet::PseudoJet> input_particles;

  bool firstEvent = true; //Used later to print info for the first event
  // Allow for possibility of a few faulty events. (could maybe even leave this out)
  int nAbort = 10;
  int iAbort = 0;

  // Create a vector to store the px and py values of selected particles
  std::vector<std::pair<double, double>> p_l, p_lbar;
  std::vector<double> pt_l, pt_lbar, eta_l, eta_lbar, pt_ll;

  // Begin event loop; generate until none left in input file.
  for (int iEvent = 0; ; ++iEvent) {

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
    p_l.resize(0);
  //double Et = 0;
    // Loop over event record to decide what to pass to FastJet
    for (int i = 0; i < pythia.event.size(); ++i) {
      // Final state only
      if (!pythia.event[i].isFinal())        continue;

      //code that obtained the leptons from the W+ and w- decays
      // Particle* p = &pythia.event[i]; 

      //obtain the transverse energy for the top tagger. I now implement this for each event, because
      //I'm finding the jets for each event, but at some point I might have to do this outside the for loop over events.
      //Et += pythia.event[i].pt();

      // Store the pt of the two leading leptons, in this case we only consider electrons and muons, not tau's.
      if(abs(pythia.event[i].id()) == 11 || abs(pythia.event[i].id()) == 13){
            
        // Save the px and py values of the current particle
        double px = pythia.event[i].px();
        double py = pythia.event[i].py();
        p_l.push_back(std::make_pair(px, py));
      }

      // Store as input to Fastjet
      input_particles.push_back( fastjet::PseudoJet( pythia.event[i].px(),
        pythia.event[i].py(), pythia.event[i].pz(), pythia.event[i].e() ) );
      

    }
  
  // Sort the p_l vector in descending order of pt
  std::sort(p_l.begin(), p_l.end(), [](const std::pair<double, double>& a, const std::pair<double, double>& b) { return sqrt(a.first*a.first + a.second*a.second) > sqrt(b.first*b.first + b.second*b.second); });

  double px_l1 = p_l[0].first;
  double py_l1 = p_l[0].second;
  double px_l2 = p_l[1].first;
  double py_l2 = p_l[1].second;
  double ptll = sqrt(pow(px_l1 + px_l2, 2.0) + pow(py_l1 + py_l2, 2.0));

  pt_ll.push_back(ptll);
  // // Print out the px and py values of the selected particles
  // for (int i = 0; i < p_l.size(); ++i) {
  //   std::cout << "Lepton " << i << " px: " << p_l[i].first << " py: " << p_l[i].second << std::endl;
  // }

    if (input_particles.size() == 0) {
      cout << "Error: event with no final state particles" << endl;
      continue;

    }

    // Run Fastjet algorithm
    vector <fastjet::PseudoJet> inclusive_jets, sorted_jets;
    fastjet::ClusterSequence clustSeq(input_particles, jetDef);

    // For the first event, print the FastJet details
    if (firstEvent) {
      cout << "Ran " << jetDef.description() << endl;
      cout << "Strategy adopted by FastJet was "
           << clustSeq.strategy_string() << endl << endl;
      firstEvent = false;
    }

    // Extract inclusive jets sorted by pT (note minimum pT of 20.0 GeV)
    inclusive_jets = clustSeq.inclusive_jets(2.0);
    sorted_jets    = sorted_by_pt(inclusive_jets);

    //output the information on jets directly per event. At some point I should do this after the 
    //event loop, but right now it's a good test. 
    // label the columns
    // printf("%5s %15s %15s %15s\n","jet #", "rapidity", "phi", "Et");
    
    double Et_tot = 0;

    for (unsigned int i = 0; i < sorted_jets.size(); i++) {
      Et_tot += sorted_jets[i].Et();
    }
    cout << "Et_tot = " << Et_tot << endl;
    // // print out the details for each jet
    // for (unsigned int i = 0; i < sorted_jets.size(); i++) {
    //   printf("%5u %15.8f %15.8f %15.8f\n",
    //   i, sorted_jets[i].rap(), sorted_jets[i].phi(),
    //   sorted_jets[i].Et());
    // }
  // End of event loop.
  }

  for (int i = 0; i < static_cast<int>(pt_ll.size()); ++i){
    std::cout << "#event = " << i << "pt_ll = " << pt_ll[i] << endl;
  }


  // // Print out the px and py values of the selected particles
  // for (int i = 0; i < p_l.size(); ++i) {
  //   std::cout << "Lepton " << i << " px: " << p_l[i].first << " py: " << p_l[i].second << std::endl;
  // }


  // Statistics
  pythia.stat();

  // export output:

  // Open output file
  std::ofstream outfile("output_pt_ll.csv");

  // Write header row
  outfile << "pt_ll\n";

  // Write data rows
  for (int i = 0; i < static_cast<int>(pt_ll.size()); ++i) {      //The static cast is used because i is a signed int and pt_ll.size is an unsigned int, this makes it a signed in.
    outfile << pt_ll[i] << "\n";
  }

  // Close output file
  outfile.close();


  return 0;
}

