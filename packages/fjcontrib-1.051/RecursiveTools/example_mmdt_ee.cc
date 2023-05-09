//----------------------------------------------------------------------
/// \file example_ee.cc
///
/// This example program is meant to illustrate how to use
/// RecursiveTools for e+e- events. It is done using the
/// ModifiedMassDropTagger class but the same strategy would work as
/// well for SoftDrop, RecursiveSoftDrop and IteratedSoftDrop
///
/// Run this example with
///
/// \verbatim
///     ./example_ee < ../data/single-ee-event.dat
/// \endverbatim
//----------------------------------------------------------------------

// $Id: example_mmdt_ee.cc 1064 2017-09-08 09:19:57Z gsoyez $
//
// Copyright (c) 2017-, Gavin P. Salam, Gregory Soyez, Jesse Thaler,
// Kevin Zhou, Frederic Dreyer
//
//----------------------------------------------------------------------
// This file is part of FastJet contrib.
//
// It is free software; you can redistribute it and/or modify it under
// the terms of the GNU General Public License as published by the
// Free Software Foundation; either version 2 of the License, or (at
// your option) any later version.
//
// It is distributed in the hope that it will be useful, but WITHOUT
// ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
// or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
// License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this code. If not, see <http://www.gnu.org/licenses/>.
//----------------------------------------------------------------------

#include <iostream>
#include <sstream>

#include <sstream>
#include <iomanip>
#include <cmath>
#include "fastjet/ClusterSequence.hh"
#include "fastjet/tools/Filter.hh"
#include "ModifiedMassDropTagger.hh" // In external code, this should be fastjet/contrib/ModifiedMassDropTagger.hh

using namespace std;
using namespace fastjet;

// forward declaration to make things clearer
void read_event(vector<PseudoJet> &event);
ostream & operator<<(ostream &, const PseudoJet &);

//----------------------------------------------------------------------
int main(){

  //----------------------------------------------------------
  // read in input particles
  vector<PseudoJet> event;
  read_event(event);
  cout << "# read an event with " << event.size() << " particles" << endl;

  // first get some Cambridge/Aachen jets
  double R = 1.0;
  JetDefinition jet_def(ee_genkt_algorithm, R, 0.0);
  ClusterSequence cs(event, jet_def);

  double Emin = 10.0;
  Selector sel_jets = SelectorEMin(Emin);
  vector<PseudoJet> jets = sorted_by_E(sel_jets(cs.inclusive_jets()));
  
  // give the tagger a short name
  typedef contrib::ModifiedMassDropTagger MMDT;
  
  // This version uses the following setup:
  //  - use energy for the symmetry measure
  //    Note: since the mMDT does not require angular information,
  //      here we could use either theta_E or cos_theta_E (it would
  //      only change the value of DeltaR). For
  //      SoftDrop/RecursiveSoftDrop/IteratedSoftDrop, this would make
  //      a difference and we have
  //        DeltaR_{ij}^2 = theta_{ij}^2              (theta_E)
  //        DeltaR_{ij}^2 = 2 [1-cos(theta_{ij}^2)]   (cos_theta_E)
  //
  //  - recurse into the branch with the largest energy
  //
  //  - use a symmetry cut, with no mass-drop requirement
  double z_cut = 0.20;
  MMDT tagger(z_cut,
              MMDT::cos_theta_E,
              std::numeric_limits<double>::infinity(),
              MMDT::larger_E);
  cout << "tagger is: " << tagger.description() << endl;

  for (unsigned ijet = 0; ijet < jets.size(); ijet++) {
    // first run MMDT and examine the output
    PseudoJet tagged_jet = tagger(jets[ijet]);
    cout << endl;
    cout << "original jet: " << jets[ijet] << endl;
    cout << "tagged   jet: " << tagged_jet << endl;
    if (tagged_jet == 0) continue;  // If symmetry condition not satisified, jet is not tagged
    cout << "  delta_R between subjets: " << tagged_jet.structure_of<MMDT>().delta_R() << endl;
    cout << "  symmetry measure(z):     " << tagged_jet.structure_of<MMDT>().symmetry() << endl;
    cout << "  mass drop(mu):           " << tagged_jet.structure_of<MMDT>().mu() << endl;

    cout << endl;
  }

  return 0;
}

//----------------------------------------------------------------------
/// read in input particles
void read_event(vector<PseudoJet> &event){  
  string line;
  while (getline(cin, line)) {
    istringstream linestream(line);
    // take substrings to avoid problems when there are extra "pollution"
    // characters (e.g. line-feed).
    if (line.substr(0,4) == "#END") {return;}
    if (line.substr(0,1) == "#") {continue;}
    double px,py,pz,E;
    linestream >> px >> py >> pz >> E;
    PseudoJet particle(px,py,pz,E);

    // push event onto back of full_event vector
    event.push_back(particle);
  }
}

//----------------------------------------------------------------------
/// overloaded jet info output
ostream & operator<<(ostream & ostr, const PseudoJet & jet) {
  if (jet == 0) {
    ostr << " 0 ";
  } else {
    ostr << " E = " << jet.pt()
         << " m = " << jet.m();
  }
  return ostr;
}
