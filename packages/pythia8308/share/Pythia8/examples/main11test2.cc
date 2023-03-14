// main11.cc is a part of the PYTHIA event generator.
// Copyright (C) 2022 Torbjorn Sjostrand.
// PYTHIA is licenced under the GNU GPL v2 or later, see COPYING for details.
// Please respect the MCnet Guidelines, see GUIDELINES for details.

// Keywords: basic usage; LHE file;

// This is a simple test program.
// It illustrates how Les Houches Event File input can be used in Pythia8.
// It uses the ttsample.lhe(.gz) input file, the latter only with 100 events.

#include "Pythia8/Pythia.h"
using namespace Pythia8;
int main() {


  // Generator. We here stick with default values, but changes
  // could be inserted with readString or readFile.
  Pythia pythia;

  // Initialize Les Houches Event File run. List initialization information.
  pythia.readString("Beams:frameType = 4");
  // pythia.readString("HardQCD:all = on"); 
  pythia.readString("Next:numberShowInfo = 0");
  pythia.readString("Next:numberShowProcess = 0");
  pythia.readString("Next:numberShowEvent = 0");
  // pythia.readString("PhaseSpace:pTHatMin = 200.");
  pythia.readString("Beams:LHEF = /data/theorie/pherbsch/ML4EFT/pythia8308/examples/unweighted_events_copy.lhe");
  pythia.init();

  // Book histogram.
  // Hist nCharged("charged particle multiplicity",100,-0.5,399.5);

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

    // // Sum up final charged multiplicity and fill in histogram.
    // int nChg = 0;
    // for (int i = 0; i < pythia.event.size(); ++i)
    // if (pythia.event[i].isFinal() && pythia.event[i].isCharged())
    //   ++nChg;
    // nCharged.fill(nChg);

  // End of event loop.
  }

  // Give statistics. Print histogram.
  pythia.stat();
  // cout << nCharged;

  // Done.
  return 0;
}
