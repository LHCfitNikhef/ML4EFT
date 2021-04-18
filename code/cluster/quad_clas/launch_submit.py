# Author: Jaco ter Hoeve
# Python script that initiates the submission of the training to the smefit cluster

import subprocess

# Make it executable
subprocess.call(['chmod', '+x', './submit_training.sh'])
# Launch the training submission script
subprocess.call("./submit_training.sh")