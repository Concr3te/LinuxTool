import elevate
import getpass
import sys
import os
import sqlite3
import binascii
import hashlib

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

def CreateUser(appdir):
    from LinuxInstallerClass import LinuxInstaller
    from PyQt5.QtWidgets import QApplication

    root = is_root()

    if root:
        os.environ["DISPLAY"] = ":0"


    root_ownership = "chown -R root:root " + appdir

    os.system(root_ownership)

    print(appdir)

    con = sqlite3.connect(appdir + "/database.db")

    cursor = con.cursor()
    check_locked = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="locked")
    cursor.execute(check_locked)
    result = cursor.fetchall()

    if not result:
        statement = "CREATE table locked (package);"
        cursor.execute(statement)

    app = QApplication(sys.argv)

    Installer = LinuxInstaller(appdir)

    Installer.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    appdir = GetVariables()
    root = is_root()
    if not root:
        os.system("xhost +")
    print(appdir)
    #elevate.elevate()
    CreateUser(appdir[0])
