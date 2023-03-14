#include "Pythia8/Pythia.h"
#include <fstream>
using namespace Pythia8;

int main() {

// You can always read a plain LHE file,
  // but if you ran "./configure --with-gzip" before "make"
  // then you can also read a gzipped LHEF file.
#ifdef GZIP
  bool useGzip = true;
#else
  bool useGzip = false;
#endif
  cout << " useGzip = " << useGzip << endl;

  // Generator. We here stick with default values, but changes
  // could be inserted with readString or readFile.
  Pythia pythia;

  // Initialize Les Houches Event File run. List initialization information.
  pythia.readString("Beams:frameType = 1");
  if (useGzip) pythia.readString("Beams:LHEF = /data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/unweighted_events.lhe.gz");
  else         pythia.readString("Beams:LHEF = /data/theorie/pherbsch/MG5_aMC_v3_4_1/small_shower_test/Events/run_01/unweighted_events_copy.lhe");
  pythia.init();

  // Open a file to write the particle information
  ofstream outputFile;
  outputFile.open("particle_info.txt");

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

    // Find the top and anti-top quarks in the event
    int topQuarkIndex = -1, antiTopQuarkIndex = -1;
    for (int i = 0; i < pythia.event.size(); ++i) {
      if (pythia.event[i].id() == 6 && pythia.event[i].isFinal()) {
        topQuarkIndex = i;
      }
      if (pythia.event[i].id() == -6 && pythia.event[i].isFinal()) {
        antiTopQuarkIndex = i;
      }
    }

    // Check if both top and anti-top quarks were found in the event
    if (topQuarkIndex == -1 || antiTopQuarkIndex == -1) {
      cout << "Top or anti-top quark not found in the event." << endl;
      continue;
    }
    
    // Store the current event and clear the event record in Pythia
    Event event = pythia.event;
    pythia.event.clear();

    // Add the top quark to the event record
    pythia.event.append(6, 1, 0, 0, event[topQuarkIndex].px(), event[topQuarkIndex].py(), event[topQuarkIndex].pz(), event[topQuarkIndex].e());

    // Shower and hadronize the top quark
    pythia.next();

    // Add the anti-top quark to the event record
    pythia.event.append(-6, 1, 0, 0, event[antiTopQuarkIndex].px(), event[antiTopQuarkIndex].py(), event[antiTopQuarkIndex].pz(), event[antiTopQuarkIndex].e());

    // Shower and hadronize the anti-top quark
    pythia.next();

    // Write the particle information to the file
    for (int i = 0; i < pythia.event.size(); ++i) {
      if (pythia.event[i].isFinal()) {
        outputFile << pythia.event[i].id() << " " 
                  << pythia.event[i].px() << " " 
                  << pythia.event[i].py() << " " 
                  << pythia.event[i].pz() << " " 
                  << pythia.event[i].e() << endl;
      }
    }
  // End of event loop.
  }

  // Close the file
  outputFile.close();

  // Give statistics.
  pythia.stat();


  // Done.
  return 0;
}
