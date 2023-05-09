  #pragma region hard_bs
    hard_b.resize(0);
    //Hard scattering information
    for (int i = 0 ; i < pythia.process.size(); i++){
      if (abs(pythia.process[i].id()) == 5){
        double hard_b_px = pythia.process[i].px();
        double hard_b_py = pythia.process[i].py();
        double hard_b_pz = pythia.process[i].pz();
        double hard_b_e = pythia.process[i].e();
        double hard_b_eta = pythia.process[i].eta();
        // Save the id of the b to determine if it a b or anti b
        double hard_id_b = pythia.process[i].id();
        hard_bs.push_back(std::make_tuple(hard_b_px, hard_b_py,hard_b_pz,hard_b_e, hard_b_eta,hard_id_b));
      }
    }
  // Sort the p_b vector in descending order of pt
  std::sort(hard_bs.begin(), hard_bs.end(), [](const std::tuple<double, double, double, double, double, double>& a, const std::tuple<double, double, double, double, double, double>& b) {
      double ax = std::get<0>(a);
      double ay = std::get<1>(a);
      double bx = std::get<0>(b);
      double by = std::get<1>(b);
      return std::sqrt(ax*ax + ay*ay) > std::sqrt(bx*bx + by*by);
  });

    //Where I think this code might go wrong is if we have to leading bs or anti bs, it's not made to deab with that, but I'bb deab with that bater

      double hard_b_px_lead = std::get<0>(hard_bs[i]);
      double hard_b_py_lead = std::get<1>(hard_bs[i]);
      double hard_b_pz_lead = std::get<2>(hard_bs[i]);
      double hard_b_e_lead = std::get<3>(hard_bs[i]);
      double hard_bot_eta_lead = std::get<4>(hard_bs[i]);
      double hard_id_b_lead = std::get<5>(hard_bs[i]);
      double hard_b_px_trail = std::get<0>(hard_bs[i]);
      double hard_b_py_trail = std::get<1>(hard_bs[i]);
      double hard_b_pz_trail = std::get<2>(hard_bs[i]);
      double hard_b_e_trail = std::get<3>(hard_bs[i]);
      double hard_bpt_eta_trail = std::get<4>(hard_bs[i]);
      double hard_id_b_trail = std::get<5>(hard_bs[i]);
      double hard_bot_pt_lead = sqrt(pow(hard_b_px_lead,2.0) + pow(hard_b_py_lead,2.0));
      double hard_bot_pt_trail = sqrt(pow(hard_b_px_trail,2.0) + pow(hard_b_py_trail,2.0));
      double hard_botbotbar_pt = sqrt(pow(hard_b_px_lead + hard_b_px_trail,2.0) + pow(hard_b_px_lead + hard_b_py_trail,2.0));
      double hard_mass_bbar = sqrt(pow(hard_b_e_lead + hard_b_e_trail,2.0) + pow(hard_b_px_lead + hard_b_px_trail,2.0) - pow(hard_b_py_lead + hard_b_py_trail,2.0) - pow(hard_b_pz_lead + hard_b_pz_trail,2.0));
      h_b_pt_lead.push_back(hard_bot_pt_lead);
      h_b_eta_lead.push_back(hard_bot_eta_lead);
      h_b_pt_trail.push_back(hard_bot_pt_trail);
      h_b_eta_trail.push_back(hard_bot_eta_trail);
      h_pt_bbar.push_back(hard_botbotbar_pt);
      h_m_bbar.push_back(hard_mass_bbar);

  #pragma endregion hard bs