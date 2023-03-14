#include "Pythia8/Pythia.h"
#include <iostream>

using namespace Pythia8;

int main() {
  Pythia pythia;

  // Set up top quark with momentum p = (100 GeV, 0, 0, 100 GeV)
  double mass = 172.5;    // Top quark mass in GeV
  double pT = 100.0;      // Transverse momentum in GeV
  double phi = 0.0;       // Azimuthal angle in radians
  double eta = 0.0;       // Pseudorapidity
  double pz = pT * sinh(eta); // Longitudinal momentum
  double e = sqrt(pT*pT + pz*pz + mass*mass); // Energy
  int id = 6;             // Top quark ID

  // Add top quark to Pythia event record
  Event& event = pythia.event;
  event.reset();
  event.append( id, 23, 0, 0, pT * cos(phi), pT * sin(phi), pz, e );

  // Set up Pythia to decay the top quark
  pythia.readString("Top:all = on");
  pythia.init();

  // Perform top quark decay
  if (!pythia.next()) {
    std::cerr << "ERROR: Top quark decay failed." << std::endl;
    return 1;
  }

  // Print out final state particles.
  std::cout << "Final state particles:" << std::endl;
  for (int i = 0; i < event.size(); ++i) {
    if (event[i].isFinal()) {
      std::cout << event[i] << std::endl;
    }
  }

  return 0;
}
