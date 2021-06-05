#!/usr/bin/python3

import os
import sys
import os.path
import getpass
import subprocess
from shutil import copyfile

def install():
    homedir = os.path.expanduser("~")
    username = getpass.getuser()
    appdir = homedir + "/.LinuxTool"
    venvdir = appdir + "/.venv"

    installed = os.path.exists(appdir)
    print(installed)

    if not installed:
        os.system("mkdir "+ appdir)
        os.system("virtualenv "+ venvdir)
        copyfile("./LinuxTool.py", appdir + "/LinuxTool.py")
        os.system("chmod +x " + appdir + "/LinuxTool.py")
        copyfile("./database.db", appdir + "/new.db")
        copyfile("./getssl.sh", appdir + "/getssl.sh")
        copyfile("./ElevatedScript.py", appdir + "/ElevatedScript.py")
        os.system("chmod +x " + appdir + "/getssl.sh")
        copyfile("./LinuxTool.desktop", appdir + "/LinuxTool.desktop")
        python_path = venvdir + "/bin/activate"
        command = ". "+ python_path
        os.system(command)
        install_python_apt = "cp -r python3-apt/usr/lib/python3/dist-packages/* " + venvdir + "/lib/python3.8/site-packages"
        install_python_dbus = "cp -r python3-dbus/usr/lib/python3/dist-packages/* " + venvdir + "/lib/python3.8/site-packages"
        os.system(install_python_apt)
        os.system(install_python_dbus)
        pip_path = venvdir + "/bin/pip"
        os.system(pip_path + " install -r requirements.txt")


    python_bin = venvdir + "/bin/python3"
    script_file = "./create_user.py"
    script_file = os.path.abspath(script_file)
    subprocess.Popen([python_bin, script_file])

if __name__ == "__main__":
    install()
