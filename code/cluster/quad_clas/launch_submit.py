import subprocess

# Make it executable
subprocess.call(['chmod', '+x', './submit_training.sh'])
subprocess.call("./submit_training.sh")