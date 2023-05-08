import subprocess
import json

def save_conda_environment_details(output_file):
    try:
        env_name = subprocess.check_output(['conda', 'info', '--json']).decode('utf-8').split('"active_prefix":', 1)[-1].split('"', 1)[1]
        
        conda_list_output = subprocess.check_output(['conda', 'list', '-e']).decode('utf-8')

        with open(output_file, 'w') as f:
            f.write(f"Conda environment details for {env_name}:\n")
            f.write(conda_list_output)

        print(f"Conda environment details saved to {output_file}")

    except subprocess.CalledProcessError as e:
        print("Error occurred while fetching conda environment details:", e)

if __name__ == '__main__':
    output_file = "/data/theorie/pherbsch/ML4EFT/subproj/output/conda_environment_details.txt"
    save_conda_environment_details(output_file)
