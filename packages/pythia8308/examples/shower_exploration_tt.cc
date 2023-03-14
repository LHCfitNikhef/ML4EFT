#include "Pythia8/Pythia.h"
#include <iostream>

using namespace Pythia8;

int main() {

  // Initialize the generator
  Pythia pythia;

  // Read the LHE file
  pythia.readString("Beams:frameType = 4");
  pythia.readString("Beams:LHEF = /data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/unweighted_events_copy.lhe");
  // pythia.init();

  // Loop over all events in the LHE file
  for (int i = 0; i < int(pythia.event.size()); ++i) {
    cout << i << endl;
    // int id = pythia.event[i].id();
    // double pT = pythia.event[i].pT();
    // cout << id << endl;
  }

  // Done
  return 0;
}
