import os
import os.path
import binascii
import getpass
import hashlib
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from PyQt5.QtWidgets import *
from PyQt5 import QtCore

class LinuxInstaller(QMainWindow):
    def __init__(self, homedir, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        #self.homedir = homedir 
        self.appdir = homedir
        self.venvdir = self.appdir + "/.venv"

        if not os.path.exists(self.appdir):
            #TODO - replace this with a UI prompt
            print("Application not installed")
            return
        #self.setGeometry(1368 / 2 , 100, 400, 600);
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        self.setFixedSize(400, 600)
        self.setWindowTitle("Linux Tool Installer")

        self.AppUserName = QLineEdit()
        self.AppUserNameInputLabel = QLabel("Username")
        self.AppUserPassword = QLineEdit()
        self.AppUserPasswordInputLabel = QLabel("Password")
        self.AppUserPassword.setEchoMode(QLineEdit.Password)

        self.AppLoginButton = QPushButton("&Sign up")
        self.AppLoginButtonPadding = QPushButton()

        self.AppLoginButton.setFixedSize(100, 25)
        self.AppLoginButton.clicked.connect(self.AppSignUp)
        self.AppLoginButtonPadding.setFixedSize(100, 25)
        self.AppLoginButtonPadding.hide()

        self.LoginLayout = QFormLayout()

        self.ResetPassword = QCheckBox()
        self.AppResetButtonPadding = QPushButton()
        self.AppResetButtonPadding.setFixedSize(100, 25)
        self.AppResetButtonPadding.hide()

        self.LoginLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.LoginLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.LoginLayout.setFormAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.LoginLayout.setLabelAlignment(QtCore.Qt.AlignLeft)

        self.LoginLayout.addRow(self.AppUserNameInputLabel, self.AppUserName)
        self.LoginLayout.addRow(self.AppUserPasswordInputLabel, self.AppUserPassword)
        self.LoginLayout.addRow(self.AppLoginButtonPadding, self.AppLoginButton)
        self.LoginLayout.addRow(self.AppResetButtonPadding, self.ResetPassword)

        self.LoginWidget = QWidget(self)
        #self.LoginWidget.setStyleSheet("background-color: grey;");
        self.setCentralWidget(self.LoginWidget)

        self.LoginWidget.setLayout(self.LoginLayout)
    
    def InstallDesktopFile(self):
        file_path = self.appdir + "/LinuxTool.desktop"
        pattern = "Exec=filepath"
        substitute = "Exec=" + self.appdir + "/LinuxTool.py"
        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(pattern, substitute))
        copymode(file_path, abs_path)
        remove(file_path)
        move(abs_path, file_path)
        os.system("desktop-file-install " + file_path)


    def AppSignUp(self):
        #Log user in or fail with an error
        username = self.AppUserName.text()
        password = self.AppUserPassword.text()

        resetpass = self.ResetPassword.checkState()

        self.InstallDesktopFile()

        if resetpass:
            import sqlite3
            db_path = self.appdir + "/database.db"
            con = sqlite3.connect(db_path)

            con.execute("DROP TABLE login")

            salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
            pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
            pwdhash = binascii.hexlify(pwdhash)
            pwdhash = (salt + pwdhash).decode('ascii')
            con.execute("CREATE table login (username, password)")
            query = 'INSERT INTO login (username, password) VALUES("{username}", "{hashed_password}")'.format(username=username, hashed_password=pwdhash)
            con.execute(query)
            con.commit()
            os.remove(self.appdir + "/new.db")
        else:
            os.system("mv " + self.appdir + "/new.db " + self.appdir + "/database.db")
            import sqlite3
            db_path = self.appdir + "/database.db"
            con = sqlite3.connect(db_path)

            salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
            pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
            pwdhash = binascii.hexlify(pwdhash)
            pwdhash = (salt + pwdhash).decode('ascii')
            con.execute("CREATE table login (username, password)")
            query = 'INSERT INTO login (username, password) VALUES("{username}", "{hashed_password}")'.format(username=username, hashed_password=pwdhash)
            con.execute(query)
            con.commit()

