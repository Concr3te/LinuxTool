#!/usr/bin/python3

import os
import sys
import os.path
import getpass

def install():
    homedir = os.path.expanduser("~")
    username = getpass.getuser()
    appdir = homedir + "/.LinuxTool"
    venvdir = appdir + "/.venv"

    print(homedir)
    print(appdir)

    if os.path.exists(appdir):
        print("Application already installed\n")
        return
    else:
        os.mkdir(appdir)
    if os.path.exists(appdir + "/.venv"):
        print("Application already installed\n")
        return
    else:
        print("Application not already installed\n")
        os.system("mkdir "+ appdir)
        os.system("virtualenv "+ venvdir)
        #builder = EnvBuilder()
        #builder.create(venvdir)
    pip_path = venvdir + "/bin/pip"
    import subprocess

    # Path to a Python interpreter that runs any Python script
    # under the virtualenv /path/to/virtualenv/
    python_bin = venvdir + "/bin/python3"
    # Path to the script that must run under the virtualenv
    script_file = "./install_packages.py"

    subprocess.Popen([python_bin, script_file])


if __name__ == "__main__":
    install()
