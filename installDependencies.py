#!/usr/bin/python	

import subprocess
import os, sys

# Check installed dependencies
# TODO
# pip

# Checking root privileges
# get the effective user ID
euid = os.geteuid()

# if euid has root privileges
if euid != 0:
	print "You have to run this script with administrator priviledges"
else:
	# Install Matplotlib
	subprocess.call(["apt-get", "-y", "install", "python-matplotlib"])
	# Install PySide 
	subprocess.call(["apt-get", "-y", "install", "python-pyside"])
	
