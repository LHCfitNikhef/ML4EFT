// KTClusCXX Package
//
// Copyright (c) 2021 Andrii Verbytskyi <andrii.verbytskyi@mpp.mpg.de>
//
// $Id$
//----------------------------------------------------------------------
//    The package aims to implement the functionality of KTCLUS from the
//    'ktclus.f' package by M.Seymour, 1992-2010, which was widely 
//    used in the past. Therefore, the KTClusCXXJetDefinition function
//    attempts to mimic the interface of the KTCLUS and accepts a single 
//    4-digit integer to create a jet algorithm definition. The integer
//    is decoded as follows (the definition is taken from the 'ktclus.f'):
//
//    The collision type and analysis type are indicated by the first
//    argument of KTCLUS. IMODE=<TYPE><ANGLE><MONO><RECOM> where
//    TYPE:  1=>ee, 2=>ep with p in -z direction, 3=>pe, 4=>pp
//    ANGLE: 1=>angular kt def., 2=>DeltaR, 3=>f(DeltaEta,DeltaPhi)
//           where f()=2(cosh(eta)-cos(phi)) is the QCD emission metric
//    MONO:  1=>derive relative pseudoparticle angles from jets
//           2=>monotonic definitions of relative angles
//    RECOM: 1=>E recombination scheme, 2=>pt scheme, 3=>pt**2 scheme
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

#ifndef __FASTJET_CONTRIB_KTCLUSCXX_HH__
#define __FASTJET_CONTRIB_KTCLUSCXX_HH__

#include <iostream>
#include <limits>
#include <vector>
#include <sstream>
#include <string>
#include "fastjet/PseudoJet.hh"
#include "fastjet/JetDefinition.hh"
#include "fastjet/NNH.hh"

FASTJET_BEGIN_NAMESPACE      // defined in fastjet/internal/base.hh
// forward declaration to reduce includes
class ClusterSequence;

namespace contrib {


namespace KTClusCXX {
   enum Type {
       ee = 1000,
       ep = 2000,
       pe = 3000,
       pp = 4000
     };
   enum Angle {
       angular = 100,
       deltar = 200,
       f = 300
     };
   enum Mono {
       jets = 10,
       monolitic = 20
     };
   enum Recom {
       e = 1,
       pt =2,
       pt2 =3
     };
};

class KTClusInfo {
public:
    KTClusInfo(const double R = 1.0): _R(R) {}
    double R() const {
        return _R;
    }
private:
    double _R;
};

template<int TYPE, int ANGLE, int MONO, int RECOM>
class KTClusBriefJet {
public:
    inline double to_pi(const double& a1) const {
      double  phi = a1;
      while (phi>M_PI) phi -= (2*M_PI);
      while (phi<-M_PI) phi += (2*M_PI);
      return phi;
    }
    void init(const PseudoJet & jet, KTClusInfo* IN) {
        double norm = 1.0/std::sqrt(jet.modp2());
        nx = jet.px() * norm;
        ny = jet.py() * norm;
        nz = jet.pz() * norm;
        E = jet.E();
        pt = jet.pt();
        phi = jet.phi();
        eta = jet.eta();
        rap = jet.rap();
        R = IN->R();
    }


    double distance(const KTClusBriefJet * jet) const {
        /// For a better readability we have a single line for each set of template arguments.
        if (MONO != 10) throw Error("The algorithms with MONO!=1 are not implemented in the current version.");
        
        if (TYPE == 1000 && ANGLE == 100) return 2*std::min(E*E, jet->E*jet->E)*(1.0 - (nx*jet->nx + ny*jet->ny + nz*jet->nz));
        if (TYPE == 2000 && ANGLE == 100) return 2*std::min(E*E, jet->E*jet->E)*(1.0 - (nx*jet->nx + ny*jet->ny + nz*jet->nz));
        if (TYPE == 3000 && ANGLE == 100) return 2*std::min(E*E, jet->E*jet->E)*(1.0 - (nx*jet->nx + ny*jet->ny + nz*jet->nz));
        if (TYPE == 4000 && ANGLE == 100) return 2*std::min(E*E, jet->E*jet->E)*(1.0 - (nx*jet->nx + ny*jet->ny + nz*jet->nz));

        if (TYPE == 1000 && ANGLE == 200) return std::min(pt*pt, jet->pt*jet->pt)*(std::pow(to_pi(phi - jet->phi), 2)  + std::pow(rap - jet->rap, 2));
        if (TYPE == 2000 && ANGLE == 200) return std::min(pt*pt, jet->pt*jet->pt)*(std::pow(to_pi(phi - jet->phi), 2)  + std::pow(rap - jet->rap, 2));
        if (TYPE == 3000 && ANGLE == 200) return std::min(pt*pt, jet->pt*jet->pt)*(std::pow(to_pi(phi - jet->phi), 2)  + std::pow(rap - jet->rap, 2));
        if (TYPE == 4000 && ANGLE == 200) return std::min(pt*pt, jet->pt*jet->pt)*(std::pow(to_pi(phi - jet->phi), 2)  + std::pow(rap - jet->rap, 2));

        if (TYPE == 1000 && ANGLE == 300) return std::min(pt*pt, jet->pt*jet->pt)*2*(std::cosh(rap - jet->rap) - std::cos(to_pi(phi - jet->phi)));
        if (TYPE == 2000 && ANGLE == 300) return std::min(pt*pt, jet->pt*jet->pt)*2*(std::cosh(rap - jet->rap) - std::cos(to_pi(phi - jet->phi)));
        if (TYPE == 3000 && ANGLE == 300) return std::min(pt*pt, jet->pt*jet->pt)*2*(std::cosh(rap - jet->rap) - std::cos(to_pi(phi - jet->phi)));
        if (TYPE == 4000 && ANGLE == 300) return std::min(pt*pt, jet->pt*jet->pt)*2*(std::cosh(rap - jet->rap) - std::cos(to_pi(phi - jet->phi)));

        throw Error("Unknown distance function");
        
    }

    double beam_distance() const {
        /// For a better readability we have a single line for each set of template arguments.
        if (TYPE == 1000 && ANGLE == 100) return std::numeric_limits<double>::max()/256;
        if (TYPE == 2000 && ANGLE == 100) return 2*R*R*E*E*(1 + nz);
        if (TYPE == 3000 && ANGLE == 100) return 2*R*R*E*E*(1 - nz);
        if (TYPE == 4000 && ANGLE == 100) return 2*R*R*E*E*std::min(1 - nz, 1 + nz);

        if (TYPE == 1000 && ANGLE == 200) return std::numeric_limits<double>::max()/256;
        if (TYPE == 2000 && ANGLE == 200) return R*R*pt*pt;
        if (TYPE == 3000 && ANGLE == 200) return R*R*pt*pt;
        if (TYPE == 4000 && ANGLE == 200) return R*R*pt*pt;

        if (TYPE == 1000 && ANGLE == 300) return std::numeric_limits<double>::max()/256;
        if (TYPE == 2000 && ANGLE == 300) return R*R*pt*pt;
        if (TYPE == 3000 && ANGLE == 300) return R*R*pt*pt;
        if (TYPE == 4000 && ANGLE == 300) return R*R*pt*pt;

        throw Error("Unknown beam distance function");
    }

private:
    double E, pt, eta, rap, phi, nx, ny, nz, R;
};


template<int TYPE, int ANGLE, int MONO, int RECOM>
class KTClusCXXPlugin : public JetDefinition::Plugin {
public:
    enum Strategy { strategy_NNH = 0};

    KTClusCXXPlugin (const double radius = 1.0, Strategy strategy = strategy_NNH): _R(radius),  _strategy(strategy) {}

    KTClusCXXPlugin (const KTClusCXXPlugin & plugin) {
        *this = plugin;
    }

    virtual std::string description () const {
        std::ostringstream desc;
        desc << " KTCLUS algorithm plugin in mode " << TYPE << ANGLE << MONO << RECOM;
        switch(_strategy) {
        case strategy_NNH:
            desc << ", using NNH strategy";
            break;
        default:
            throw Error("Unrecognized strategy in KTClusCXX");
        }

        return desc.str();
    }

    virtual void run_clustering(ClusterSequence & cs) const {
        switch(_strategy) {
        case strategy_NNH:
            _actual_run_clustering<NNH<KTClusBriefJet < TYPE, ANGLE, MONO, 0 >,KTClusInfo> >(cs);
            break;
        default:
            throw Error("Unrecognized strategy in KTClusCXX");
        }
    }

    virtual double R() const {
        return _R;
    }

    virtual bool exclusive_sequence_meaningful() const {
        return true;
    }

private:
    double _R;
    Strategy _strategy;
    template<class N> void _actual_run_clustering(ClusterSequence & cs) const {
        int njets = cs.jets().size();
        KTClusInfo  IN(_R);
        N nn(cs.jets(),&IN);
        while (njets > 0) {
            int i, j, k;
            double dij = -1;
            dij= nn.dij_min(i, j);
            if (j >= 0) {
                cs.plugin_record_ij_recombination(i, j, dij, k);
                nn.merge_jets(i, j, cs.jets()[k], k);
            } else {
                KTClusBriefJet < TYPE, ANGLE, MONO, 0 > jt;
                jt.init(cs.jets()[i],&IN);
                double diB = jt.beam_distance();
                cs.plugin_record_iB_recombination(i, diB);
                nn.remove_jet(i);
            }
            njets--;
        }
    }
};

template<int MODE>
JetDefinition KTClusCXXJetDefinition(const double Rad = 1.0) {
    RecombinationScheme rs;
    if (MODE%10 == 1) rs = E_scheme;
    if (MODE%10 == 2) rs = pt_scheme;
    if (MODE%10 == 3) rs = pt2_scheme;
    JetDefinition JD(new KTClusCXXPlugin<1000*(MODE/1000), 100*((MODE/100)%10), 10*((MODE/10)%10), MODE%10>(Rad));
    JD.set_recombination_scheme(rs);
    JD.delete_plugin_when_unused();
    return JD;
}

inline JetDefinition KTClusCXXJetDefinition(const int m, const double x = 1.0) {
    switch (m) {
    case 1111: return KTClusCXXJetDefinition<1111>(x); break;
    case 2111: return KTClusCXXJetDefinition<2111>(x); break;
    case 3111: return KTClusCXXJetDefinition<3111>(x); break;
    case 4111: return KTClusCXXJetDefinition<4111>(x); break;

    case 1211: return KTClusCXXJetDefinition<1211>(x); break;
    case 2211: return KTClusCXXJetDefinition<2211>(x); break;
    case 3211: return KTClusCXXJetDefinition<3211>(x); break;
    case 4211: return KTClusCXXJetDefinition<4211>(x); break;

    case 1311: return KTClusCXXJetDefinition<1311>(x); break;
    case 2311: return KTClusCXXJetDefinition<2311>(x); break;
    case 3311: return KTClusCXXJetDefinition<3311>(x); break;
    case 4311: return KTClusCXXJetDefinition<4311>(x); break;

    case 1121: return KTClusCXXJetDefinition<1121>(x); break;
    case 2121: return KTClusCXXJetDefinition<2121>(x); break;
    case 3121: return KTClusCXXJetDefinition<3121>(x); break;
    case 4121: return KTClusCXXJetDefinition<4121>(x); break;

    case 1221: return KTClusCXXJetDefinition<1221>(x); break;
    case 2221: return KTClusCXXJetDefinition<2221>(x); break;
    case 3221: return KTClusCXXJetDefinition<3221>(x); break;
    case 4221: return KTClusCXXJetDefinition<4221>(x); break;

    case 1321: return KTClusCXXJetDefinition<1321>(x); break;
    case 2321: return KTClusCXXJetDefinition<2321>(x); break;
    case 3321: return KTClusCXXJetDefinition<3321>(x); break;
    case 4321: return KTClusCXXJetDefinition<4321>(x); break;

    case 1112: return KTClusCXXJetDefinition<1112>(x); break;
    case 2112: return KTClusCXXJetDefinition<2112>(x); break;
    case 3112: return KTClusCXXJetDefinition<3112>(x); break;
    case 4112: return KTClusCXXJetDefinition<4112>(x); break;

    case 1212: return KTClusCXXJetDefinition<1212>(x); break;
    case 2212: return KTClusCXXJetDefinition<2212>(x); break;
    case 3212: return KTClusCXXJetDefinition<3212>(x); break;
    case 4212: return KTClusCXXJetDefinition<4212>(x); break;

    case 1312: return KTClusCXXJetDefinition<1312>(x); break;
    case 2312: return KTClusCXXJetDefinition<2312>(x); break;
    case 3312: return KTClusCXXJetDefinition<3312>(x); break;
    case 4312: return KTClusCXXJetDefinition<4312>(x); break;

    case 1122: return KTClusCXXJetDefinition<1122>(x); break;
    case 2122: return KTClusCXXJetDefinition<2122>(x); break;
    case 3122: return KTClusCXXJetDefinition<3122>(x); break;
    case 4122: return KTClusCXXJetDefinition<4122>(x); break;

    case 1222: return KTClusCXXJetDefinition<1222>(x); break;
    case 2222: return KTClusCXXJetDefinition<2222>(x); break;
    case 3222: return KTClusCXXJetDefinition<3222>(x); break;
    case 4222: return KTClusCXXJetDefinition<4222>(x); break;

    case 1322: return KTClusCXXJetDefinition<1322>(x); break;
    case 2322: return KTClusCXXJetDefinition<2322>(x); break;
    case 3322: return KTClusCXXJetDefinition<3322>(x); break;
    case 4322: return KTClusCXXJetDefinition<4322>(x); break;

    case 1113: return KTClusCXXJetDefinition<1113>(x); break;
    case 2113: return KTClusCXXJetDefinition<2113>(x); break;
    case 3113: return KTClusCXXJetDefinition<3113>(x); break;
    case 4113: return KTClusCXXJetDefinition<4113>(x); break;

    case 1213: return KTClusCXXJetDefinition<1213>(x); break;
    case 2213: return KTClusCXXJetDefinition<2213>(x); break;
    case 3213: return KTClusCXXJetDefinition<3213>(x); break;
    case 4213: return KTClusCXXJetDefinition<4213>(x); break;

    case 1313: return KTClusCXXJetDefinition<1313>(x); break;
    case 2313: return KTClusCXXJetDefinition<2313>(x); break;
    case 3313: return KTClusCXXJetDefinition<3313>(x); break;
    case 4313: return KTClusCXXJetDefinition<4313>(x); break;

    case 1123: return KTClusCXXJetDefinition<1123>(x); break;
    case 2123: return KTClusCXXJetDefinition<2123>(x); break;
    case 3123: return KTClusCXXJetDefinition<3123>(x); break;
    case 4123: return KTClusCXXJetDefinition<4123>(x); break;

    case 1223: return KTClusCXXJetDefinition<1223>(x); break;
    case 2223: return KTClusCXXJetDefinition<2223>(x); break;
    case 3223: return KTClusCXXJetDefinition<3223>(x); break;
    case 4223: return KTClusCXXJetDefinition<4223>(x); break;

    case 1323: return KTClusCXXJetDefinition<1323>(x); break;
    case 2323: return KTClusCXXJetDefinition<2323>(x); break;
    case 3323: return KTClusCXXJetDefinition<3323>(x); break;
    case 4323: return KTClusCXXJetDefinition<4323>(x); break;
    default:
    throw Error(std::string("In KTClusCXXJetDefinition, unrecognized mode =")+ std::to_string(m));
    }
    return JetDefinition();
}
inline JetDefinition KTClusCXXJetDefinition(const int m1,const int m2,const int m3,const int m4, const double x = 1.0) 
{ return KTClusCXXJetDefinition(m1+m2+m3+m4, x);}

}  // namespace contrib
FASTJET_END_NAMESPACE        // defined in fastjet/internal/base.hh

#endif // __KTCLUSCXX_HH__

