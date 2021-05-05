import os
import os.path
import getpass

from venv import EnvBuilder

def install():
    homedir = os.path.expanduser("~")
    username = getpass.getuser()

    appdir = homedir + "/.LinuxTool"
    venvdir = appdir + "/.venv"

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
        builder = EnvBuilder()
        builder.create(venvdir)

if __name__ == "__main__":
    install()
    #builder = EnvBuilder()
    #builder.create(".venv")
