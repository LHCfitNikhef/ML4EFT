#include <cstddef>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <fastjet/ClusterSequence.hh>
#include "KTClusCXX.hh"

using namespace fastjet;

class Input {
public:
    Input() {};
    ~Input() {};
    const double PIMASS = 0.139;
    std::vector <PseudoJet> input_particles;
    std::size_t N;
    void fill(const std::string& inp="")
    {
        input_particles.clear();
        std::size_t i = 0;
        double px, py, pz, E;

        if (inp.size()) {
            std::ifstream myfile;
            myfile.open (inp.c_str());
            while (myfile >> px >> py >> pz >> E) {
                input_particles.push_back(PseudoJet(px, py, pz, E));
                i++;
            }
            myfile.close();
        } else {

            while (std::cin >> px >> py >> pz >> E) {
                input_particles.push_back(PseudoJet(px, py, pz, E));
                i++;
            }
        }
        N = i;
    }
};
inline std::ostream& operator<<(std::ostream& os, const PseudoJet &j) {
    os <<  j.px() << " " << j.py() << " " << j.pz() << " " << j.e();
    return os;
}
int main( int argc, char** argv)
{
    if (argc<2) std::cout <<"#Usage: "<<argv[0]<<" <input file=standard input>  <Radius=1.0> <YCUT=0.0001> <ECUT=1.0>" <<std::endl;
    std::vector<int> modes {
    1111,2111,3111,4111,1211,2211,3211,4211,
    1311,2311,3311,4311,1112,2112,3112,4112,
    1212,2212,3212,4212,1312,2312,3312,4312,
    1113,2113,3113,4113,1213,2213,3213,4213,
    1313,2313,3313,4313
    };
    std::vector<bool> inclusives{true,false};
    double Radius = argc>2?std::atof(argv[2]):1.0;
    double YCUT = argc>3?std::atof(argv[3]):0.0001;
    double ECUT =argc>4?std::atof(argv[4]):1.0;
    Input IN;
    IN.fill(argc>1?argv[1]:"");
    std::cout << std::fixed << std::setw(11) << std::setprecision(6);
    std::cout<<"Input particles:"<<std::endl;
    for (auto& i: IN.input_particles) {
        std::cout<<i<<std::endl;
    }
    std::vector < PseudoJet > fastjets;
    fastjets.reserve(IN.N);

    for (const auto& inclusive: inclusives) {
    for (const auto& mode: modes) {
    ClusterSequence cs(IN.input_particles, contrib::KTClusCXXJetDefinition(mode, Radius));
    if (inclusive) {
        fastjets = cs.inclusive_jets();
    } else {
        fastjets = cs.exclusive_jets(ECUT*ECUT*YCUT);
    }
    std::vector < double > fastjets_dmerge;
    std::sort(fastjets.begin(), fastjets.end(), [](const PseudoJet & a, const PseudoJet & b) -> bool { return a.E() > b.E(); });
    for (std::size_t i = 0; i < IN.N; i++) {
        fastjets_dmerge.push_back(cs.exclusive_dmerge_max(i));
    }

    std::cout<<"Parameters: "<< mode << (inclusive?std::string("i"):std::string(""))<< " " << Radius << " " << YCUT<< " " << ECUT <<std::endl;
    std::cout<<"Pseudojets:"<<std::endl;
    for (auto& j: fastjets) {
        std::cout<<j<<std::endl;
    }
    std::cout<<"exclusive_dmerge:"<<std::endl;
    for (auto& d: fastjets_dmerge) {
        std::cout<<std::min(1000000.0,d)<<std::endl;
    }
}
}
    return 0;
}
