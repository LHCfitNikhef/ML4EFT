#include "Pythia8/Pythia.h"
#include <iostream>
using namespace Pythia8;
using namespace std;

int main() {

    // Initialize Pythia
    Pythia pythia;

    // Set up the process
    pythia.readString("Beams:eCM = 13000.");
    pythia.readString("Beams:idA = 2212");
    pythia.readString("Beams:idB = 2212");
    pythia.readString("Top:gg2ttbar = on");
    pythia.readString("6:m0 = 172.5");
    pythia.readString("HardQCD:all = on");

    // Initialize the run
    pythia.init();

    // Loop over events
    for (int iEvent = 0; iEvent < 10; ++iEvent) {
        // Generate the next event
        if (!pythia.next()) continue;

        // Loop over all particles in the event
        for (int i = 0; i < pythia.event.size(); ++i) {

            // Check if the particle is a top or anti-top quark
            if (abs(pythia.event[i].id()) == 6) {

                // Check if the particle came from the ttbar decay channel
                if (pythia.event[pythia.event[i].mother1()].id() == pythia.event[pythia.event[i].mother2()].id() && abs(pythia.event[pythia.event[i].mother1()].id()) == 24) {
                
                    // Print kinematic information of the final state particles from ttbar decay
                    cout << "id: " << pythia.event[i].id() 
                        << "  px: " << pythia.event[i].px() 
                        << "  py: " << pythia.event[i].py() 
                        << "  pz: " << pythia.event[i].pz() 
                        << "  e: " << pythia.event[i].e() 
                        << endl;
                }
            }
        }
    }

    // Done
    pythia.stat();
    return 0;
}
