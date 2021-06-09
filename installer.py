#!/usr/bin/python3
import getpass
import sys
import os
import sqlite3
import binascii
import hashlib
import getpass
import subprocess
import os.path
import pwd
from shutil import copyfile

def is_root():
    return os.getuid() == 0

def CreateDir(appdir):
    installed = os.path.exists(appdir)

    if not installed:
        os.system("mkdir "+ appdir)

def GetVariables():
    homedir = os.path.expanduser("~")
    appdir = homedir + "/.LinuxTool"
    username = getpass.getuser()

    root = is_root()

    variables = []
    working_dir = ""
    display = ""

    if not root:
        with open("/tmp/variables.txt", "w+") as f:
            f.write(appdir)
            f.write("\n")
            f.write(os.path.abspath("."))
            f.write("\n")
            f.write(os.environ["DISPLAY"])
            f.write("\n")
            f.write(username)
    else:
        with open("/tmp/variables.txt","r") as appdir_file:
            appdir = appdir_file.readline()
            appdir = appdir.rstrip()
            working_dir = appdir_file.readline()
            working_dir = working_dir.rstrip()
            display = appdir_file.readline()
            display = display.rstrip()
            username = appdir_file.readline()
            #os.remove("/tmp/user.txt")
    variables.append(appdir)
    variables.append(working_dir)
    variables.append(display)
    variables.append(username)
    return variables

def install(appdir, username):
    venvdir = appdir + "/.venv"
    os.system("apt install pip")
    os.system("apt install --reinstall libxcb-xinerama0")
    chown_appdir = 'chown -R {username}:{username} {appdir}'.format(username=username,appdir=appdir)
    os.system(chown_appdir)

def InstallIptablesFilter():
    root = is_root()
    variables = GetVariables() 

    if root:
        with open("/etc/rsyslog.d/20-ufw.conf", "w") as f:
            f.write(':msg,contains,"[netfilter] " -/var/log/iptables.log')
            f.write("& stop")
            f.close()
            os.system("systemctl restart rsyslog")

        os.environ["DISPLAY"] = variables[2]

def InstallPackages(Variables):
    appdir = Variables[0]
    workingdir = Variables[1]
    venvdir = appdir + "/.venv"

    if workingdir:
        copyfile(workingdir + "/LinuxTool.py", appdir + "/LinuxTool.py")
        os.system("chmod +x " + appdir + "/LinuxTool.py")
        copyfile(workingdir + "/database.db", appdir + "/new.db")
        copyfile(workingdir + "/getssl.sh", appdir + "/getssl.sh")
        copyfile(workingdir + "/ElevatedScript.py", appdir + "/ElevatedScript.py")
        os.system("chmod +x " + appdir + "/getssl.sh")
        copyfile(workingdir + "/LinuxTool.desktop", appdir + "/LinuxTool.desktop")
        os.system("pip3 install -r " + workingdir + "/requirements.txt")
    else:
        copyfile("./LinuxTool.py", appdir + "/LinuxTool.py")
        os.system("chmod +x " + appdir + "/LinuxTool.py")
        copyfile("./database.db", appdir + "/new.db")
        copyfile("./getssl.sh", appdir + "/getssl.sh")
        copyfile("./ElevatedScript.py", appdir + "/ElevatedScript.py")
        os.system("chmod +x " + appdir + "/getssl.sh")
        copyfile("./LinuxTool.desktop", appdir + "/LinuxTool.desktop")
        os.system("pip install -r " + workingdir + "./requirements.txt")

def CreateUser(Variables):
    root = is_root()

    if root:
        os.environ["DISPLAY"] = Variables[2]

    root_ownership = "chown -R root:root " + Variables[0]
    appdir = Variables[0]
    workingdir = Variables[1]

    os.system(root_ownership)

    con = sqlite3.connect(Variables[0] + "/new.db")

    cursor = con.cursor()
    check_locked = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="locked")
    cursor.execute(check_locked)
    result = cursor.fetchall()

    if not result:
        statement = "CREATE table locked (package);"
        cursor.execute(statement)

    statement = "CREATE table shell (status);"
    cursor.execute(statement)

    from LinuxInstallerClass import LinuxInstaller
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    Installer = LinuxInstaller(Variables[0])

    Installer.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    variables = GetVariables()
    root = is_root()

    homedir = os.path.expanduser("~")
    appdir = homedir + "/.LinuxTool"

    CreateDir(appdir)

    if root:
        InstallPackages(variables)

    if not root:
        CreateDir(variables[0])
        os.system("pip install elevate")
    else:
        os.system("apt install -y vsftpd")
        os.system("apt install -y ssh")
        os.system("apt install -y python3-apt")
        os.system("apt install -y python3-dbus")
        install(variables[0], variables[3])

    import sqlite3
    import binascii
    import hashlib
    import elevate

    elevate.elevate()
    InstallIptablesFilter()
    CreateUser(variables)
