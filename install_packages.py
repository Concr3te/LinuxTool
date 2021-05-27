#!/usr/bin/python3

import os
import sys
import os.path
import getpass

def install_mini():

    homedir = os.path.expanduser("~")
    username = getpass.getuser()
    appdir = homedir + "/.LinuxTool"
    venvdir = appdir + "/.venv"

    from shutil import copyfile
    print(appdir + "/LinuxTool.py")

    copyfile("./LinuxTool.py", appdir + "/LinuxTool.py")

    os.system("chmod +x " + appdir + "/LinuxTool.py")

    copyfile("./database.db", appdir + "/database.db")

    copyfile("./getssl.sh", appdir + "/getssl.sh")

    python_path = venvdir + "/bin/activate"

    command = ". "+ python_path

    os.system(command)

    install_python_apt = "cp -r python3-apt/usr/lib/python3/dist-packages/* " + venvdir + "/lib/python3.8/site-packages"
    install_python_dbus = "cp -r python3-dbus/usr/lib/python3/dist-packages/* " + venvdir + "/lib/python3.8/site-packages"

    os.system(install_python_apt)
    os.system(install_python_dbus)

    pip_path = venvdir + "/bin/pip"

    os.system(pip_path + " install -r requirements.txt")


    import subprocess

    # Path to a Python interpreter that runs any Python script
    # under the virtualenv /path/to/virtualenv/
    python_bin = venvdir + "/bin/python3"
    # Path to the script that must run under the virtualenv
    script_file = "./create_user.py"

    script_file = os.path.abspath(script_file)

    subprocess.Popen([python_bin, script_file])

def InstallSystem():
    install_mini()

if __name__ == "__main__":
    InstallSystem()
