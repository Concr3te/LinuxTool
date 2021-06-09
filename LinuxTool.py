#!/usr/bin/python3

import os
import getpass
import subprocess

def is_root():
    return os.getuid() == 0

def GetVariables():
    homedir = os.path.expanduser("~")
    appdir = homedir + "/.LinuxTool"
    venvdir = appdir + "/.venv"    
    username = getpass.getuser()
        
    root = is_root()
 
    variables = []
    working_dir = ""
 
    if not root:
        with open("/tmp/variables.txt", "w+") as f:
            f.write(appdir)
            f.write("\n")
            f.write(os.path.abspath("."))
    else:
        with open("/tmp/variables.txt","r") as appdir_file:
            appdir = appdir_file.readline()
            appdir = appdir.rstrip()
            working_dir = appdir_file.readline()
            #os.remove("/tmp/user.txt")
    variables.append(appdir)
    variables.append(working_dir)
    return variables

if __name__ == "__main__":
    variables = GetVariables()

    venvdir = variables[0] + "/.venv"

    python_bin = "python3"
    script_file = variables[0] + "/ElevatedScript.py"
    script_file = os.path.abspath(script_file)
    subprocess.Popen([python_bin, script_file])
