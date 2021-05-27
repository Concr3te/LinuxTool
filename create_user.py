import elevate
import getpass
import sys
import os
import sqlite3

def is_root():
    return os.getuid() == 0

def GetVariables():
    homedir = os.path.expanduser("~")
    appdir = homedir + "/.LinuxTool"
    venvdir = appdir + "/.venv"
    username = getpass.getuser()

    root = is_root()

    if not root:
        with open("/tmp/user.txt", "w+") as f:
            f.write(appdir)
    else:
        with open("/tmp/user.txt","r") as appdir_file:
            appdir = appdir_file.readline()
            #os.remove("/tmp/user.txt")
    print(appdir)
    return appdir

def CreateUser(appdir):
    from LinuxInstallerClass import LinuxInstaller
    from PyQt5.QtWidgets import QApplication

    root = is_root()

    if root:
        os.environ["DISPLAY"] = ":0"


    root_ownership = "chown -R root:root " + appdir

    os.system(root_ownership)

    con = sqlite3.connect(appdir + "/database.db")

    cursor = con.cursor()

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
    elevate.elevate()
    CreateUser(appdir)
