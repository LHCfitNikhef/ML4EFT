#pragma region headers
// Pythia
#include "Pythia8/Pythia.h"
#include <Pythia8/Info.h>
#include <Pythia8/SigmaTotal.h>

// Fastjet headers
#include "fastjet/ClusterSequence.hh"
#include "fastjet/Selector.hh"
#include "fastjet/contrib/RecursiveSoftDrop.hh"
#include "fastjet/contrib/SoftDrop.hh"

#include "fastjet/contrib/RecursiveSymmetryCutBase.hh"

#include <iostream> // needed for io
#include <fstream>  // needed for output vsc file
#include <cstdio>   // needed for io
// For lepton analysis
#include <vector>
#include <algorithm>
#include <cmath>

// For processing pseudojets
#include <map>
#include <functional>

// printing in decimals
#include <iomanip>

//getting pi
#include <numbers>

// jet pruning
#include "fastjet/tools/Filter.hh"
#include "fastjet/tools/Pruner.hh"

// create output directory
#include <sys/stat.h>
#include <iostream>

//reading in input values for the code
#include <cstdlib>

#pragma endregion headers

using namespace Pythia8;
using namespace std;

// Functions
//these functions are used in other functions so we want to declare them at the top
bool is_b_hadron(int pdgId)
{
    int abs_pdgId = std::abs(pdgId);
    int first_digit = abs_pdgId / 1000;
    int second_digit = (abs_pdgId / 100) % 10;
    int third_digit = (abs_pdgId / 10) % 10;

    return (first_digit == 5) || (second_digit == 5) || (third_digit == 5);
}

bool is_lepton(int pdgId)
{
    return (pdgId == 11) || (pdgId == 13);
}

bool is_anti_lepton(int pdgId)
{
    return (pdgId == -11) || (pdgId == -13);
}

//consistency section
//to see if there are visible particles with significant pt other than the particles of interest, we filter the visible particles in 
//an event to exclude the particles of interest and to save space also not consider particles with a pt smaller than 20 Gev
std::pair<std::vector<double>, std::vector<int>> process_visible_particles(const std::vector<fastjet::PseudoJet>& visible_particles) {
    std::vector<fastjet::PseudoJet> pseudojets = sorted_by_pt(visible_particles);
    std::vector<double> pt_values;
    std::vector<int> id_values;

    // Variables to track removal
    bool lepton_removed = false;
    bool anti_lepton_removed = false;
    int b_hadrons_removed = 0;

    // Iterate over vector and remove particles
    pseudojets.erase(std::remove_if(pseudojets.begin(), pseudojets.end(), 
        [&](const fastjet::PseudoJet& jet) {
            int id = jet.user_index();
            if(!lepton_removed && is_lepton(id)) {
                lepton_removed = true;
                return true;
            }
            if(!anti_lepton_removed && is_anti_lepton(id)) {
                anti_lepton_removed = true;
                return true;
            }
            if(b_hadrons_removed < 2 && is_b_hadron(id)) {
                b_hadrons_removed++;
                return true;
            }
            return false;
        }), pseudojets.end());

    // After filtering, we push back the pt values > 20 GeV to the pt_values vector
    for(const auto& jet : pseudojets){
        if(jet.pt() > 20){
            pt_values.push_back(jet.pt());
            id_values.push_back(jet.user_index());
        }
    }

    return {pt_values, id_values};
}

// Filtering of the events
std::vector<std::vector<double>> filter_events(const std::vector<std::vector<double>>& event_pt_values, const std::vector<bool>& event_selection) {
    std::vector<std::vector<double>> filtered_events;
    for (int i = 0; i < event_pt_values.size(); i++) {
        if (event_selection[i]) {
            filtered_events.push_back(event_pt_values[i]);
        }
    }
    return filtered_events;
}

// Flattening of the vector of vectors into a single vector
std::vector<double> flatten(const std::vector<std::vector<double>>& event_pt_values) {
    std::vector<double> flat_pt_values;
    for (const auto& event : event_pt_values) {
        for (double pt : event) {
            flat_pt_values.push_back(pt);
        }
    }
    return flat_pt_values;
}


//Function to parse the values of zcut and beta we want to provide the code with
std::vector<std::pair<double,double>> parse_zcut_beta(const std::string& zcut_beta_str){
    std::vector<std::pair<double, double>> zcut_beta_vec;
    std::stringstream ss(zcut_beta_str);
    std::string pair_str;

    while (std::getline(ss, pair_str, ';')){
        double zcut, beta;
        std::stringstream pair_ss(pair_str);
        if (pair_ss >> zcut && pair_ss.ignore(1,',') && pair_ss >> beta){
            zcut_beta_vec.emplace_back(zcut,beta);
        }

    }

    return zcut_beta_vec;
}

//extract the name of the event (i.e. wilson coefficient) from the path of the lhe file
std::string extract_event_name(const std::string &lhe_file_path) {
    std::string base_path = "/data/theorie/jthoeve/ML4EFT_events/";
    size_t start_pos = base_path.length();
    size_t end_pos = lhe_file_path.find('/', start_pos);
    return lhe_file_path.substr(start_pos, end_pos - start_pos);
}

//extract the job number for each wilson coefficient/event from the path of the lhe file
int extract_job_number(const std::string &lhe_file_path) {
    size_t start_pos = lhe_file_path.find("job");
    start_pos += 3; // Move past the "job" substring
    size_t end_pos = lhe_file_path.find('/', start_pos);
    return std::stoi(lhe_file_path.substr(start_pos, end_pos - start_pos));
}

bool directory_exists(const std::string &path)
{
    struct stat info;
    if (stat(path.c_str(), &info) != 0)
    {
        return false;
    }
    return (info.st_mode & S_IFDIR) != 0;
}

bool file_exists(const std::string &file_path)
{
    std::ifstream file(file_path);
    return file.good();
}

bool prompt_override(const std::string &file_path)
{
    std::string response;
    std::cout << "File " << file_path << " already exists. Do you want to override it? (y/n): ";
    std::cin >> response;
    return response == "y" || response == "Y";
}

std::tuple<double, double, double, double, int> get_kinematics(int i, bool process, Pythia8::Pythia &pythia)
{
    double px = process ? pythia.process[i].px() : pythia.event[i].px();
    double py = process ? pythia.process[i].py() : pythia.event[i].py();
    double pz = process ? pythia.process[i].pz() : pythia.event[i].pz();
    double e = process ? pythia.process[i].e() : pythia.event[i].e();
    int id = process ? pythia.process[i].id() : pythia.event[i].id();

    return std::make_tuple(px, py, pz, e, id);
}

void get_pseudojet(double px, double py, double pz, double e, int id, std::vector<fastjet::PseudoJet> &vec, const std::string &type = "")
{
    bool store = false;

    if (type == "")
    {
        store = true;
    }
    else if (type == "h_l" || type == "l")
    {
        if (id == 11 || id == 13)
        {
            store = true;
        }
    }
    else if (type == "h_lbar" || type == "lbar")
    {
        if (id == -11 || id == -13)
        {
            store = true;
        }
    }
    else if (type == "h_b" || type == "b")
    {
        if (std::abs(id) == 5)
        {
            store = true;
        }
    }

    if (store)
    {
        fastjet::PseudoJet particle(px, py, pz, e);
        particle.set_user_index(id);
        vec.push_back(particle);
    }
}

void get_bjets(
    std::vector<fastjet::PseudoJet> &b_jets,
    std::vector<fastjet::PseudoJet> &visible_particles,
    fastjet::JetDefinition &jetDef,
    std::vector<double> &pt_values,
    std::vector<int> &id_values,
    std::vector<size_t> &indices_to_remove,
    double zcut = 0,
    double beta = 0,
    double Rparam = 0
)

{

    fastjet::ClusterSequence clust_seq(visible_particles, jetDef);

    // Extract inclusive jets sorted by pT (note minimum pT of 20.0 GeV)
    double ptmin = 30; // GeV
    std::vector<fastjet::PseudoJet> inclusive_jets = clust_seq.inclusive_jets(ptmin);
    std::vector<fastjet::PseudoJet> sorted_jets1 = sorted_by_pt(inclusive_jets);


    fastjet::contrib::SoftDrop softdrop(beta, zcut, Rparam);
    std::vector<fastjet::PseudoJet> groomed_jets, groomed_jets_softdrop;
    for (const auto &jet : inclusive_jets)
    {
        fastjet::PseudoJet groomed_jet = softdrop(jet);
        groomed_jets.push_back(groomed_jet);
    }

    std::vector<fastjet::PseudoJet> sorted_jets = sorted_by_pt(groomed_jets);

    int num_b_jets = 0;
    // B-tagging
    for (const auto &jet : sorted_jets)
    {
        int b_hadron_count = 0;
        std::vector<fastjet::PseudoJet> constituents = jet.constituents();
        // cout << "jets of this events analysed for constituents" << endl;
        for (const auto &constituent : constituents)
        {
            int id = constituent.user_index();
            // cout << "constituents id: " << id << endl;
            // cout << "pt of constituent: " << constituent.pt() << endl;
            if (is_b_hadron(id))
            {
                b_hadron_count++;
            }
        }
        bool is_b_jet = b_hadron_count > 0;

        // This code is to only save the b-jets with the highest pt
        if (is_b_jet)
        {
            // cerr << "num of b jets" << num_b_jets << endl;
            if (num_b_jets == 2)
            {
                break;
            }
            for (const auto &constituent : constituents)
            {
                double constituent_pt = constituent.pt();  // Get the transverse momentum of the constituent

                int constituent_id = constituent.user_index();            //     std::cout << "constituent pt = " << constituent_pt << std::endl;index();  // Get the pdg id of the constituent

                for (size_t i = 0; i < pt_values.size(); ++i){
                    if (pt_values[i] == constituent_pt && id_values[i] == constituent_id) {
                        indices_to_remove.push_back(i);
                        break;
                    }
                }
            }

            // for (const auto &constituent : constituents)
            // {
            //     std::cout << "constituents id: " << constituent.user_index() << std::endl;
            //     std::cout << "pt of constituent: " << constituent.pt() << std::endl;
            // }

            b_jets.push_back(jet);

            num_b_jets++;
        }
    }

    if (num_b_jets < 2)
    { // Here an unphysical jet is added to keep the kinematic vectors the same size and events with these jets are later deleted
        fastjet::PseudoJet fill_jet1(9999, 0, 0, 0);
        fastjet::PseudoJet fill_jet2(9999, 0, 0, 0);
        if (num_b_jets == 1)
        {
            b_jets.push_back(fill_jet1);
        }
        else if (num_b_jets == 0)
        {
            b_jets.push_back(fill_jet1);
            b_jets.push_back(fill_jet2);
        }
    }
}

std::pair<std::vector<fastjet::PseudoJet>, std::vector<fastjet::PseudoJet>> separate_visible_and_neutrino(std::vector<fastjet::PseudoJet> &final_particles_)
{

    std::vector<fastjet::PseudoJet> neutrinos, visible_particles;
    std::vector<int> neutrino_ids = {12, -12, 14, -14, 16, -16};

    for (const auto &particle : final_particles_)
    {
        if (std::find(neutrino_ids.begin(), neutrino_ids.end(), particle.user_index()) != neutrino_ids.end())
        {
            neutrinos.push_back(particle);
        }
        else
        {
            visible_particles.push_back(particle);
        }
    }

    return std::make_pair(neutrinos, visible_particles);
}

double get_pt(const std::vector<fastjet::PseudoJet> &particles_)
{
    double px = 0, py = 0;
    for (const auto &particle : particles_)
    {
        px += particle.px();
        py += particle.py();
    }
    double pt = sqrt(pow(px, 2.0) + pow(py, 2.0));
    return pt;
}

double get_delta_r(fastjet::PseudoJet &particle1, fastjet::PseudoJet &particle2)
{
    double delta_phi = particle1.phi() - particle2.phi();
    double delta_eta = particle1.eta() - particle2.eta();
    double delta_r = sqrt(pow(delta_phi, 2.0) + pow(delta_eta, 2.0));

    return delta_r;
}

struct KinematicBData
{
    std::vector<double> *pt_lead;
    std::vector<double> *pt_trail;
    std::vector<double> *eta_lead;
    std::vector<double> *eta_trail;
    std::vector<double> *pt_bb;
    std::vector<double> *m_bb;

    KinematicBData() : pt_lead(nullptr), pt_trail(nullptr), eta_lead(nullptr), eta_trail(nullptr), pt_bb(nullptr), m_bb(nullptr) {}

    KinematicBData(std::vector<double> &pt_lead_, std::vector<double> &pt_trail_, std::vector<double> &eta_lead_, std::vector<double> &eta_trail_, std::vector<double> &pt_bb_, std::vector<double> &m_bb_)
        : pt_lead(&pt_lead_), pt_trail(&pt_trail_), eta_lead(&eta_lead_), eta_trail(&eta_trail_), pt_bb(&pt_bb_), m_bb(&m_bb_) {}
};

struct KinematicLData
{
    std::vector<double> *pt_lead;
    std::vector<double> *pt_trail;
    std::vector<double> *eta_lead;
    std::vector<double> *eta_trail;
    std::vector<double> *pt_l;
    std::vector<double> *pt_lbar;
    std::vector<double> *eta_l;
    std::vector<double> *eta_lbar;
    std::vector<double> *abs_diff_phi;
    std::vector<double> *diff_abs_eta;
    std::vector<double> *pt_ll;
    std::vector<double> *m_ll;

    KinematicLData() : pt_lead(nullptr), pt_trail(nullptr), eta_lead(nullptr), eta_trail(nullptr),
                       pt_l(nullptr), pt_lbar(nullptr), eta_l(nullptr), eta_lbar(nullptr),
                       abs_diff_phi(nullptr), diff_abs_eta(nullptr), pt_ll(nullptr), m_ll(nullptr) {}

    KinematicLData(std::vector<double> &pt_lead_, std::vector<double> &pt_trail_, std::vector<double> &eta_lead_, std::vector<double> &eta_trail_,
                   std::vector<double> &pt_l_, std::vector<double> &pt_lbar_, std::vector<double> &eta_l_, std::vector<double> &eta_lbar_,
                   std::vector<double> &abs_diff_phi_, std::vector<double> &diff_abs_eta_, std::vector<double> &pt_ll_, std::vector<double> &m_ll_)
        : pt_lead(&pt_lead_), pt_trail(&pt_trail_), eta_lead(&eta_lead_), eta_trail(&eta_trail_),
          pt_l(&pt_l_), pt_lbar(&pt_lbar_), eta_l(&eta_l_), eta_lbar(&eta_lbar_),
          abs_diff_phi(&abs_diff_phi_), diff_abs_eta(&diff_abs_eta_), pt_ll(&pt_ll_), m_ll(&m_ll_) {}
};

struct KinematicCutData
{
    std::vector<double> *n_pt_miss;
    std::vector<double> *v_pt_miss;
    std::vector<double> *delta_R;

    KinematicCutData() : n_pt_miss(nullptr), v_pt_miss(nullptr), delta_R(nullptr) {}

    KinematicCutData(std::vector<double> &n_pt_miss_, std::vector<double> &v_pt_miss_, std::vector<double> &delta_R_)
        : n_pt_miss(&n_pt_miss_), v_pt_miss(&v_pt_miss_), delta_R(&delta_R_) {}
};

std::map<std::string, KinematicBData> kinematic_b_data_map;
std::map<std::string, KinematicLData> kinematic_l_data_map;
std::map<std::string, KinematicCutData> kinematic_cut_data_map;

// Define a static function to return the default pseudojet
std::vector<fastjet::PseudoJet> &get_default_pseudojet()
{
    static std::vector<fastjet::PseudoJet> default_jet = {fastjet::PseudoJet(0.0, 0.0, 0.0, 0.0)};
    return default_jet;
}

void process_pseudojets(std::vector<fastjet::PseudoJet> &vec1, std::vector<fastjet::PseudoJet> &vec2 = get_default_pseudojet(),
                        std::vector<fastjet::PseudoJet> &vec3 = get_default_pseudojet(), std::vector<fastjet::PseudoJet> &vec4 = get_default_pseudojet(),
                        const std::string &type = "")
{
    std::vector<fastjet::PseudoJet> sorted_jets1 = sorted_by_pt(vec1);
    // process vec2 here because it is only necessary for leptons. It is important that the leptons come first and the anti leptons second. In this code, the order matters
    std::vector<fastjet::PseudoJet> sorted_jets2 = sorted_by_pt(vec2);
    std::vector<fastjet::PseudoJet> leading_lep_anti_lep = {sorted_jets1[0], sorted_jets2[0]};
    std::vector<fastjet::PseudoJet> sorted_lead_trail_lep = sorted_by_pt(leading_lep_anti_lep);
    std::vector<fastjet::PseudoJet> sorted_jets3 = sorted_by_pt(vec3);

    if (kinematic_b_data_map.find(type) != kinematic_b_data_map.end())
    {
        KinematicBData &kbd = kinematic_b_data_map[type];
        kbd.pt_lead->push_back(sorted_jets1[0].pt());
        kbd.pt_trail->push_back(sorted_jets1[1].pt());
        kbd.eta_lead->push_back(sorted_jets1[0].eta());
        kbd.eta_trail->push_back(sorted_jets1[1].eta());
        kbd.pt_bb->push_back((sorted_jets1[0] + sorted_jets1[1]).pt());
        kbd.m_bb->push_back((sorted_jets1[0] + sorted_jets1[1]).m());
    }

    if (kinematic_l_data_map.find(type) != kinematic_l_data_map.end())
    {

        KinematicLData &kld = kinematic_l_data_map[type];
        kld.pt_lead->push_back(sorted_lead_trail_lep[0].pt());
        kld.pt_trail->push_back(sorted_lead_trail_lep[1].pt());
        kld.eta_lead->push_back(sorted_lead_trail_lep[0].eta());
        kld.eta_trail->push_back(sorted_lead_trail_lep[1].eta());
        kld.pt_l->push_back(sorted_jets1[0].pt());
        kld.pt_lbar->push_back(sorted_jets2[0].pt());
        kld.eta_l->push_back(sorted_jets1[0].eta());
        kld.eta_lbar->push_back(sorted_jets2[0].eta());

        double abs_diff_phi = abs(sorted_jets1[0].phi() - sorted_jets2[0].phi());
        // std::cout << "abs_diff_phi_before_adjustment: " << abs_diff_phi << std::endl;
        if(abs_diff_phi > M_PI){
            abs_diff_phi = 2*M_PI - abs_diff_phi;
        }
        kld.abs_diff_phi->push_back(abs_diff_phi);
        // std::cout << "abs_diff_phi: " << abs_diff_phi << std::endl;
        // std::cout << "pi: " << M_PI << std::endl;

        kld.diff_abs_eta->push_back(abs(sorted_jets1[0].eta()) - abs(sorted_jets2[0].eta()));
        kld.pt_ll->push_back((sorted_jets1[0] + sorted_jets2[0]).pt());
        kld.m_ll->push_back((sorted_jets1[0] + sorted_jets2[0]).m());
    }

    if (kinematic_cut_data_map.find(type) != kinematic_cut_data_map.end())
    {
        KinematicCutData &kcd = kinematic_cut_data_map[type];
        const auto &[neutrinos, visible_particles] = separate_visible_and_neutrino(vec4);

        kcd.n_pt_miss->push_back(get_pt(neutrinos));
        kcd.v_pt_miss->push_back(get_pt(visible_particles));
        double ll = get_delta_r(sorted_jets1[0], sorted_jets2[0]), l1j1 = get_delta_r(sorted_jets1[0], sorted_jets3[0]), l1j2 = get_delta_r(sorted_jets1[0], sorted_jets3[1]),
               l2j1 = get_delta_r(sorted_jets2[0], sorted_jets3[0]), l2j2 = get_delta_r(sorted_jets2[0], sorted_jets3[1]), jj = get_delta_r(sorted_jets3[0], sorted_jets3[1]);
        std::vector<double> distances{ll, l1j1, l1j2, l2j1, l2j2, jj};
        double min_delta_R = *std::min_element(distances.begin(), distances.end());
        kcd.delta_R->push_back(min_delta_R);
    }
}

//adding inputs to the main function to input multiple values for a variable without having to recompile the code
int main(int argc, char* argv[])
{
    //input from lhe_parser

    //check if input values are given
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " no input given" << std::endl;
        return 1;
    }

    //The  input in this case are the smeft coefficient I want to input
    std::string lhe_file_path =  argv[1];
    std::string output_folder_hard = argv[2];
    std::string output_folder_event = argv[3];
    int num_events_per_job = std::stoi(argv[4]);
    std::string zcut_beta_str = argv[5];
    std::vector<std::pair<double,double>> zcut_beta_vec = parse_zcut_beta(zcut_beta_str);

    for (const auto& [zcut, beta] : zcut_beta_vec) {


#pragma region pythia setup
    // Generator
    Pythia pythia;

    // choose reference frame
    pythia.readString("Beams:frameType = 4");

    // turn off multiparticle interactions and underlying events for a more clean analysis
    // pythia.readString("PartonLevel:MPI = off");
    // pythia.readString("PartonLevel:ISR = off");
    
    // make only events with electrons and muons by only allowing the w decay mode to those particles
    pythia.readString("24:onMode = off");
    pythia.readString("24:onIfAny = 11 13");

    // Turn off the decay of b-mesons and b-hadrons to be able to tag b-jets
    ParticleData &particleData = pythia.particleData;
    int id = 1; // technically we're missing id = 1, but that isn't a b-meson/b-hadrons anyway, so that's okay

    for (int i = 0;; ++i)
    {
        id = particleData.nextId(id);
        if (id == 0)
            break;
        if (is_b_hadron(id))
        {
            pythia.readString("HadronLevel:Decay off " + std::to_string(id));
            if (particleData.hasAnti(id))
            {
                pythia.readString("HadronLevel:Decay off " + std::to_string(-id));
            }
        }
    }
    std::string event_name = extract_event_name(lhe_file_path);
    int job_number = extract_job_number(lhe_file_path);
    pythia.readString("Beams:LHEF = " + lhe_file_path);
    pythia.init();

    // Allow for faulty events in pythia
    int nAbort = 10;
    int iAbort = 0;

#pragma endregion pythia setup

#pragma region fastjet setup
    double Rparam = 0.4;
    fastjet::Strategy strategy = fastjet::Best;
    fastjet::RecombinationScheme recombScheme = fastjet::E_scheme;
    fastjet::JetDefinition jetDef = fastjet::JetDefinition(fastjet::antikt_algorithm, Rparam, recombScheme, strategy);
#pragma endregion fastjet setup

#pragma region object definitions
    // h_b
    std::vector<double> h_pt_b_leading, h_pt_b_trailing, h_eta_b_leading, h_eta_b_trailing, h_pt_bb, h_m_bb;
    // b
    std::vector<double> pt_b_leading, pt_b_trailing, eta_b_leading, eta_b_trailing, pt_bb, m_bb;
    // h_l
    std::vector<double> h_pt_l_leading, h_pt_l_trailing, h_eta_l_leading, h_eta_l_trailing, h_pt_l1, h_pt_l2, h_eta_l1, h_eta_l2, h_DeltaPhi_ll, h_DeltaEta_ll, h_pt_ll, h_m_ll;
    // l
    std::vector<double> pt_l_leading, pt_l_trailing, eta_l_leading, eta_l_trailing, pt_l1, pt_l2, eta_l1, eta_l2, DeltaPhi_ll, DeltaEta_ll, pt_ll, m_ll;
    // cut
    std::vector<double> nu_pt_miss, vis_pt_miss, delta_R;
    // cut
    std::vector<bool> event_selection;
    // cross_section
    double cross_section, h_cross_section;
    //consistency check
    std::vector<std::vector<double>> vec_vec_external_pt;
    std::map<int, int> id_counts;

    // defining the particles for different processes in pseudojets to easily manipulate them
    // hard pseudojets
    std::vector<fastjet::PseudoJet> hard_particles, hard_b_quarks, hard_leptons, hard_anti_leptons;
    // final pseudojets
    std::vector<fastjet::PseudoJet> final_particles, b_quarks, leptons, anti_leptons, b_jets;

    // output file definitions
    std::vector<std::vector<double>> hard_kinematics_vector, kinematics_vector;
    std::vector<std::string> name_vector;

    // Define the pairs of vectors of pseudojets and the type of particles they store
    std::vector<std::pair<std::reference_wrapper<std::vector<fastjet::PseudoJet>>, std::string>> hard_vec_type_pairs = {
        {hard_particles, ""},
        {hard_b_quarks, "h_b"},
        {hard_leptons, "h_l"},
        {hard_anti_leptons, "h_lbar"}};

    std::vector<std::pair<std::reference_wrapper<std::vector<fastjet::PseudoJet>>, std::string>> event_vec_type_pairs = {
        {final_particles, ""},
        {b_quarks, "b"},
        {leptons, "l"},
        {anti_leptons, "lbar"}};

    // particles for processing
    std::vector<std::pair<std::tuple<std::reference_wrapper<std::vector<fastjet::PseudoJet>>, std::reference_wrapper<std::vector<fastjet::PseudoJet>>,
                                     std::reference_wrapper<std::vector<fastjet::PseudoJet>>, std::reference_wrapper<std::vector<fastjet::PseudoJet>>>,
                          std::string>>
        pre_processed_particles = {
            {{hard_b_quarks, get_default_pseudojet(), get_default_pseudojet(), get_default_pseudojet()}, "h_b"},
            {{b_jets, get_default_pseudojet(), get_default_pseudojet(), get_default_pseudojet()}, "b"},
            {{hard_leptons, hard_anti_leptons, get_default_pseudojet(), get_default_pseudojet()}, "h_l"},
            {{leptons, anti_leptons, get_default_pseudojet(), get_default_pseudojet()}, "l"},
            {{leptons, anti_leptons, b_jets, final_particles}, "cut"}};

    // map the kinematic vectors to a type which we'll later use in process_pseudojets
    kinematic_b_data_map["h_b"] = KinematicBData(h_pt_b_leading, h_pt_b_trailing, h_eta_b_leading, h_eta_b_trailing, h_pt_bb, h_m_bb);
    kinematic_b_data_map["b"] = KinematicBData(pt_b_leading, pt_b_trailing, eta_b_leading, eta_b_trailing, pt_bb, m_bb);
    kinematic_l_data_map["h_l"] = KinematicLData(h_pt_l_leading, h_pt_l_trailing, h_eta_l_leading, h_eta_l_trailing, h_pt_l1, h_pt_l2, h_eta_l1, h_eta_l2, h_DeltaPhi_ll, h_DeltaEta_ll, h_pt_ll, h_m_ll);
    kinematic_l_data_map["l"] = KinematicLData(pt_l_leading, pt_l_trailing, eta_l_leading, eta_l_trailing, pt_l1, pt_l2, eta_l1, eta_l2, DeltaPhi_ll, DeltaEta_ll, pt_ll, m_ll);
    kinematic_cut_data_map["cut"] = KinematicCutData(nu_pt_miss, vis_pt_miss, delta_R);

#pragma endregion object definitions

    // debug code
    int list_event = 0;
    // the number of events is given by the number of events in the lhe input file

    // Begin event loop; generate until none left in input file..
    for (int iEvent = 0; iEvent < num_events_per_job ; ++iEvent)
    { // you can add ; iEvent < 10 ; for fast itteration times

// Reset the hard particles and particles vector of pseudojets every event to store the ones for the next event
#pragma region resize
        hard_particles.resize(0);
        hard_b_quarks.resize(0);
        hard_leptons.resize(0);
        hard_anti_leptons.resize(0);
        final_particles.resize(0);
        b_quarks.resize(0);
        leptons.resize(0);
        anti_leptons.resize(0);
        b_jets.resize(0);
#pragma endregion resize

        // Generate events, and check whether generation failed.
        if (!pythia.next())
        {

            // If failure because reached end of file then exit event loop.
            if (pythia.info.atEndOfFile())
                break;

            // First few failures write off as "acceptable" errors, then quit.
            if (++iAbort < nAbort)
                continue;
            break;
        }
            pythia.process.list();
            pythia.event.list();


        // loop over the hard process
        for (int i = 0; i < pythia.process.size(); i++)
        {
            bool process = true;
            auto [px, py, pz, e, id] = get_kinematics(i, process, pythia);

            for (auto &[vec_ref, type] : hard_vec_type_pairs)
            {
                get_pseudojet(px, py, pz, e, id, vec_ref.get(), type);
            }
        }

        // loop over the final state particles in an event
        for (int i = 0; i < pythia.event.size(); i++)
        {
            if (!pythia.event[i].isFinal())
                continue;
            bool process = false;
            auto [px, py, pz, e, id] = get_kinematics(i, process, pythia);

            for (auto &[vec_ref, type] : event_vec_type_pairs)
            {
                get_pseudojet(px, py, pz, e, id, vec_ref.get(), type);
            }
        }


        auto [neutrinos, visible_particles] = separate_visible_and_neutrino(final_particles);

        //highest pt particles of an event
        std::vector<fastjet::PseudoJet> order_pt_vis_particles = sorted_by_pt(visible_particles);


        //get external pt
        auto [pt_values, id_values] = process_visible_particles(visible_particles);
        

        // analyse the high pt external particles
        // for (size_t i = 0; i < pt_values.size(); ++i){
        //         if(pt_values[i] > 300.0){
        //             cout << "id before filter = "<< id_values[i] << "pt = " << pt_values[i] << endl;
        //         }
        //     }

        std::vector<size_t> indices_to_remove;
        //get the b jets
        get_bjets(b_jets, visible_particles, jetDef, pt_values, id_values, indices_to_remove, zcut, beta, Rparam);

        // Reverse sort the indices to remove so that removing items doesn't affect the indices of items yet to be removed
        std::sort(indices_to_remove.begin(), indices_to_remove.end(), std::greater<size_t>());

        // Remove the items
        for(size_t index : indices_to_remove) {
            pt_values.erase(pt_values.begin() + index);
            id_values.erase(id_values.begin() + index);
        }

        // for (size_t i = 0; i < pt_values.size(); ++i){
        //     if(pt_values[i] > 300.0){
        //         cout << "id after filter = "<< id_values[i] << " pt = " << pt_values[i] << endl;
        //         id_counts[id_values[i]]++;
        //     }
        // }





        vec_vec_external_pt.push_back(pt_values);
        // process the particles into the kinematic vectors
        for (const auto &entry : pre_processed_particles)
        {
            const auto &vec_tuple = entry.first;
            const auto &type = entry.second;

            std::vector<fastjet::PseudoJet> &vec1 = std::get<0>(vec_tuple).get();
            std::vector<fastjet::PseudoJet> &vec2 = std::get<1>(vec_tuple).get();
            std::vector<fastjet::PseudoJet> &vec3 = std::get<2>(vec_tuple).get();
            std::vector<fastjet::PseudoJet> &vec4 = std::get<3>(vec_tuple).get();
            process_pseudojets(vec1, vec2, vec3, vec4, type);
        }

    }

    pythia.stat();

    // Let's apply the cuts in GeV and corresponding standard particle physics units
    double l_pt_lead_cut = 25, l_pt_trail_cut = 20, b_pt_lead_cut = 30, b_pt_trail_cut = 30, b_eta_lead_cut = 2.5, b_eta_trail_cut = 2.5,
           ll_m_cut_low = 20, ll_m_cut_mid = 76, ll_m_cut_high = 106, delta_R_cut = 0.4, vis_pt_miss_cut = 40, faulty_jet_pt = 9999;
    //new lepton eta cut
    double l_eta_cut = 2.5;
    // cut counts
    double l_pt_lead_cut_count = 0, l_pt_trail_cut_count = 0, b_pt_cut_count = 0, b_eta_cut_count = 0,
           ll_m_cut_count = 0, delta_R_cut_count = 0, vis_pt_miss_cut_count = 0, faulty_jet_pt_cut_count = 0,
           l_eta_cut_count = 0;

    for (int i = 0; i < pt_b_leading.size(); i++)
    {
        bool keep_event = true;
        if (abs(eta_l1[i]) > l_eta_cut || abs(eta_l2[i]) > l_eta_cut)
        {
            keep_event = false;
            l_eta_cut_count++;
        }
        if (pt_l_leading[i] < l_pt_lead_cut)
        {
            keep_event = false;
            l_pt_lead_cut_count++;
        }
        if (pt_l_trailing[i] < l_pt_trail_cut)
        {
            keep_event = false;
            l_pt_trail_cut_count++;
        }
        if (pt_b_leading[i] < b_pt_lead_cut || pt_b_trailing[i] < b_pt_trail_cut)
        {
            keep_event = false;
            b_pt_cut_count++;
        }
        if (abs(eta_b_leading[i]) > b_eta_lead_cut || abs(eta_b_trailing[i]) > b_eta_trail_cut)
        {
            keep_event = false;
            b_eta_cut_count++;
        }
        if (m_ll[i] < ll_m_cut_low || (m_ll[i] > ll_m_cut_mid && m_ll[i] < ll_m_cut_high))
        {
            keep_event = false;
            ll_m_cut_count++;
        }
        if (delta_R[i] < delta_R_cut)
        {
            keep_event = false;
            delta_R_cut_count++;
        }
        if (vis_pt_miss[i] < vis_pt_miss_cut)
        {
            keep_event = false;
            vis_pt_miss_cut_count++;
        }
        if (pt_b_leading[i] == faulty_jet_pt)
        {
            keep_event = false;
            faulty_jet_pt_cut_count++;
        }
        event_selection.push_back(keep_event);
    }
    int total_potential_cut_count = l_pt_lead_cut_count + l_pt_trail_cut_count + b_pt_cut_count + b_eta_cut_count + ll_m_cut_count + delta_R_cut_count + vis_pt_miss_cut_count + faulty_jet_pt_cut_count + l_eta_cut_count;

    //consistency check for pt
    vec_vec_external_pt = filter_events(vec_vec_external_pt, event_selection);
    
    std::vector<double> external_pt = flatten(vec_vec_external_pt);


    //calculate the cross sections
    // for the event level cross section, we can calculate the fraction of events that are kept after the cuts by using the event_selection vector
    double fraction_events_kept = static_cast<double>(std::count(event_selection.begin(), event_selection.end(), true)) / event_selection.size();
    h_cross_section = pythia.info.sigmaGen() * pow(10, 9); // in pb
    cross_section = fraction_events_kept*pythia.info.sigmaGen() * pow(10, 9); // in pb

    cout << "l_pt_lead_cut = " << std::fixed << 100 * l_pt_lead_cut_count / total_potential_cut_count << "%" << endl;
    cout << "l_pt_trail_cut = " << 100 * l_pt_trail_cut_count / total_potential_cut_count << "%" << endl;
    cout << "b_pt_cut = " << 100 * b_pt_cut_count / total_potential_cut_count << "%" << endl;
    cout << "b_eta_cut = " << 100 * b_eta_cut_count / total_potential_cut_count << "%" << endl;
    cout << "ll_m_cut = " << 100 * ll_m_cut_count / total_potential_cut_count << "%" << endl;
    cout << "delta_R_cut = " << 100 * delta_R_cut_count / total_potential_cut_count << "%" << endl;
    cout << "vis_pt_miss_cut = " << 100 * vis_pt_miss_cut_count / total_potential_cut_count << "%" << endl;
    cout << "faulty_jet_cut = " << 100 * faulty_jet_pt_cut_count / total_potential_cut_count << "%" << endl;
    cout << "l_eta_cut_count = " << 100 * l_eta_cut_count / total_potential_cut_count << "%" << endl;
    cout << "total_potential_cut = " << total_potential_cut_count << endl;
    cout << "fraction_events_kept = " << fraction_events_kept << endl;
    cout << "h_cross_section =" << h_cross_section << endl;
    cout << "cross section" << cross_section << endl;
    for(const auto& pair : id_counts){
    std::cout << "particle id = " << pair.first << ", count = " << pair.second << std::endl;
    }

    // Create the output directory if it doesn't exist
    if (!directory_exists(output_folder_hard))
    {
        int dir_err = mkdir(output_folder_hard.c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
        if (dir_err == -1)
        {
            std::cerr << "Error creating directory: " << output_folder_hard << std::endl;
            return 1;
        }
    }
    if (!directory_exists(output_folder_event))
    {
        int dir_err = mkdir(output_folder_event.c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
        if (dir_err == -1)
        {
            std::cerr << "Error creating directory: " << output_folder_event << std::endl;
            return 1;
        }
    }

    // create output file names and check if they already exist
    //If we're doing a grooming analysis, we want to use the following
    std::string hard_outfile_name, outfile_name;
    
    hard_outfile_name = output_folder_hard + "events_" + std::to_string(job_number -1) + ".csv";
    outfile_name = output_folder_event + "events_" +  std::to_string(job_number -1) + ".csv";

    // Create the output files in the specified folder
    // Open output files in the specified folder
    std::ofstream hard_outfile(hard_outfile_name);
    std::ofstream outfile(outfile_name);

    // hard_kinematics_vector = {external_pt};
    // kinematics_vector = {external_pt};
    // name_vector = {"external_pt"};

    hard_kinematics_vector = {h_pt_l1, h_pt_l2, h_pt_l_leading, h_pt_l_trailing, h_eta_l1, h_eta_l2, h_eta_l_leading, h_eta_l_trailing,
                              h_pt_ll, h_m_ll, h_DeltaPhi_ll, h_DeltaEta_ll, h_pt_b_leading, h_pt_b_trailing, h_eta_b_leading, h_eta_b_trailing, h_pt_bb, h_m_bb};
    kinematics_vector = {pt_l1, pt_l2, pt_l_leading, pt_l_trailing, eta_l1, eta_l2, eta_l_leading, eta_l_trailing,
                         pt_ll, m_ll, DeltaPhi_ll, DeltaEta_ll, pt_b_leading, pt_b_trailing, eta_b_leading, eta_b_trailing, pt_bb, m_bb};

    name_vector = {"pt_l1", "pt_l2", "pt_l_leading", "pt_l_trailing", "eta_l1", "eta_l2", "eta_l_leading", "eta_l_trailing",
                   "pt_ll", "m_ll", "DeltaPhi_ll", "DeltaEta_ll", "pt_b_leading", "pt_b_trailing", "eta_b_leading", "eta_b_trailing", "pt_bb", "m_bb"};


    // Apply event selection (only on the event level because at hard process level, the event selection was already done in generating the lhe files)
    for (auto &kin_vec : kinematics_vector)
    {
        std::vector<double> filtered_vec;
        for (int i = 0; i < kin_vec.size(); i++)
        {
            if (event_selection[i])
            {
                filtered_vec.push_back(kin_vec[i]);
            }
        }
        kin_vec = filtered_vec;
    }


    // add the cross section as the first element of the vectors in the kinematics vector and the hard kinematics vector
    for (auto &sub_vector : kinematics_vector)
    {
        sub_vector.insert(sub_vector.begin(), cross_section);
    }
    for (auto &sub_vector : hard_kinematics_vector)
    {
        sub_vector.insert(sub_vector.begin(), h_cross_section);
    }


//    consistency check in output kinematic vector size
//     First check if the vectors in the kinematics_vector have the same size as the name_vector, then see if the vectors in the kinematic have the same size
//     if not throw an error message. If they are the same size, print the size with the text: Events at event level = ... 
    if (kinematics_vector.size() == name_vector.size())
    {
        for (size_t i = 1; i < kinematics_vector.size(); ++i)
        {
            if (kinematics_vector[i].size() != kinematics_vector[1].size())
            {
                std::cerr << "The kinematic vectors at event level don't have the same size" << std::endl;
                return 1;
            }
        }
        std::cout << "Number of events at event level = " << kinematics_vector[1].size() << std::endl;
    }
    else
    {
        std::cerr << "Error: The kinematics_vector and name_vector have different sizes." << std::endl;
        return 1;
    }

    //same for hard process level
    if (hard_kinematics_vector.size() == name_vector.size())
    {
        for (size_t i = 1; i < hard_kinematics_vector.size(); ++i)
        {
            if (hard_kinematics_vector[i].size() != hard_kinematics_vector[1].size())
            {
                std::cerr << "The kinematic vectors at event level don't have the same size" << std::endl;
                return 1;
            }
        }
        std::cout << "Number of events at hard process level = " << hard_kinematics_vector[1].size() << std::endl;
    }
    else
    {
        std::cerr << "Error: The kinematics_vector and name_vector have different sizes." << std::endl;
        return 1;
    }


    //writing the data to the output files
    //Event file
    // Write the column names to the first row of the CSV file
    for (int i = 0; i < name_vector.size(); i++)
    {
        outfile << name_vector[i];
        if (i < name_vector.size() - 1)
            outfile << ",";
    }
    outfile << "\n";

    // Write the data to the remaining rows of the CSV file
    for (int i = 0; i < kinematics_vector[0].size(); i++)
    {
        for (int j = 0; j < kinematics_vector.size(); j++)
        {
            outfile << kinematics_vector[j][i];
            if (j < kinematics_vector.size() - 1)
                outfile << ",";
        }
        outfile << "\n";
    }

    // Write the column names to the first row of the CSV file
    for (int i = 0; i < name_vector.size(); i++)
    {
        hard_outfile << name_vector[i];
        if (i < name_vector.size() - 1)
            hard_outfile << ",";
    }
    hard_outfile << "\n";

    // Write the data to the remaining rows of the CSV file
    for (int i = 0; i < hard_kinematics_vector[0].size(); i++)
    {
        for (int j = 0; j < hard_kinematics_vector.size(); j++)
        {
            hard_outfile << hard_kinematics_vector[j][i];
            if (j < hard_kinematics_vector.size() - 1)
                hard_outfile << ",";
        }
        hard_outfile << "\n";
    }

    }
    return 0;
}

// run line: g++ clean_shower.cc -o clean_shower -w -I../include -O2 -std=c++11 -pedantic -W -Wall -Wshadow -fPIC -pthread  -L../lib -Wl,-rpath,../lib -lpythia8 -ldl -I/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/include -L/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib -Wl,-rpath,/data/theorie/pherbsch/ML4EFT/packages/fastjet-install/lib -lfastjet -lz -lfastjet -lfastjettools