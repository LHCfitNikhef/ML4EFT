#include "Pythia8/Pythia.h"
#include "Pythia8/ParticleData.h"


using namespace Pythia8;

int main() {
  Pythia pythia;
  pythia.readString("Beams:eCM = 13000.");
  pythia.readString("Beams:idA = 2212");
  pythia.readString("Beams:idB = 2212");

  pythia.readString("PartonLevel:FSR=off");
  pythia.readString("PartonLevel:FSR=ISR");
  pythia.readString("PartonLevel:FSR=all");

  pythia.readString("Top:gg2ttbar = on");
  // pythia.readString("Top:qqbar2ttbar = off");





  pythia.readString("6:m0 = 172.5");
  pythia.init();

  // Generate events.
  int iEvent = 0;
  while (iEvent < 10) {
    if (!pythia.next()) continue;

    // Print out final-state particles.
    for (int i = 0; i < pythia.event.size(); ++i) {
      if (pythia.event[i].isFinal()) {
        cout << setw(4) << pythia.event[i].id() << setw(14) << pythia.event[i].px() << setw(14) << pythia.event[i].py()
             << setw(14) << pythia.event[i].pz() << setw(14) << pythia.event[i].e() << endl;
      }
    }
    ++iEvent;
  }
  return 0;
}
