import os
import os.path
import getpass
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

        self.LoginLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.LoginLayout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)
        self.LoginLayout.setFormAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.LoginLayout.setLabelAlignment(QtCore.Qt.AlignLeft)

        self.LoginLayout.addRow(self.AppUserNameInputLabel, self.AppUserName)
        self.LoginLayout.addRow(self.AppUserPasswordInputLabel, self.AppUserPassword)
        self.LoginLayout.addRow(self.AppLoginButtonPadding, self.AppLoginButton)

        self.LoginWidget = QWidget(self)
        #self.LoginWidget.setStyleSheet("background-color: grey;");
        self.setCentralWidget(self.LoginWidget)

        self.LoginWidget.setLayout(self.LoginLayout)

    def AppSignUp(self):
        #Log user in or fail with an error
        username = self.AppUserPassword.text()
        password = self.AppUserPassword.text()

        import sqlite3
        db_path = self.appdir + "database.db"

        con = sqlite3.connect(db_path)
        passHash = QtCore.QCryptographicHash.hash(password, QtCore.QCryptographicHash.Sha1 );
        #QString passHashString(passHash.toHex());


        hashed_password = passHash.toHex()

        con.execute("CREATE table login (username, password)")

        query = "INSERT INTO login ({username}, {hashed_password})".format(username=username, hashed_password=hashed_password)

        con.execute(query)
        
        con.commit()

