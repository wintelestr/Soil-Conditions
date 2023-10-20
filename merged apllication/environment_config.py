'''
This script is used to install and configure the necessary packages and tools for the Soil Condition Visual software.
The following packages and tools are required in the installation and runtime process:
'''
import subprocess

# Install Pygimli and create a virtual environment
subprocess.run(["conda", "install", "-c", "gimli", "pygimli"])
subprocess.run(["conda", "create", "-n", "pg", "-c", "gimli", "-c", "conda-forge", "pygimli=1.4.3"])

# Activate the virtual environment
subprocess.run(["conda", "activate", "pg"])

# Install Pybert
subprocess.run(["conda", "install", "-c", "gimli", "pybert"])

# Install pip
subprocess.run(["apt-get", "update"])
subprocess.run(["apt-get", "upgrade"])
subprocess.run(["apt-get", "install", "python3-pip"])

# Install required Python packages
subprocess.run(["pip", "install", "pyqt5"])
subprocess.run(["pip", "install", "matplotlib"])
subprocess.run(["pip", "install", "numpy"])
subprocess.run(["pip", "install", "imageio"])
