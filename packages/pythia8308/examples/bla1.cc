    if (hard_kinematics_vector.size() == hard_name_vector.size()) {
        for (size_t i = 0; i < hard_kinematics_vector.size(); ++i) {
            std::vector<double>& kin_vec = hard_kinematics_vector[i];
            const std::string& name = hard_name_vector[i];
            std::cout << "size " << name << " = " << kin_vec.size() << std::endl;
        }
    } else {
        std::cout << "Error: The hard_kinematics_vector and hard_name_vector have different sizes." << std::endl;
    }

    // Write the column names to the first row of the CSV file
    for (auto& name : hard_name_vector) {
        hard_outfile << name << ",";
    }
    hard_outfile << "\n";

    // Write the data to the remaining rows of the CSV file
    for (int i = 0; i < hard_kinematics_vector[0].size(); i++) {
        for (int j = 0; j < hard_kinematics_vector.size(); j++) {
            hard_outfile << hard_kinematics_vector[j][i] << ",";
        }
        hard_outfile << "\n";
    }