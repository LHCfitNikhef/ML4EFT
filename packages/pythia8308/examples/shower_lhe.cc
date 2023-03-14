#include "Pythia8/Pythia.h"
#include <iostream> // needed for io
#include <sstream>  // needed for internal io
using namespace std;
using namespace Pythia8;
int main() {
  Pythia pythia;

  // Initialize Les Houches Event File run. List initialization information.
  pythia.readString("Beams:frameType = 4");
  pythia.readString("Beams:LHEF = /data/theorie/pherbsch/ML4EFT/packages/pythia8308/examples/unweighted_events_copy.lhe");
  pythia.init();

  // Allow for possibility of a few faulty events.
  int nAbort = 10;
  int iAbort = 0;
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

  double Et = 0;
    // Loop over event record to decide what to pass to FastJet
    for (int i = 0; i < pythia.event.size(); ++i) {
      // Final state only
      if (!pythia.event[i].isFinal())        continue;

      //obtain the transverse energy for the top tagger. I now implement this for each event, because
      //I'm finding the jets for each event, but at some point I might have to do this outside the for loop over events.
      Et += pythia.event[i].eT();
    }
    cout << "Et = " << Et << endl; 
  // End of event loop.
  }

  // Give statistics. Print histogram.
  pythia.stat();
  // Done.
  return 0;
}
