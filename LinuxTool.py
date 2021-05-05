import sys
import os
import elevate
import dbus

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QSize
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui

class LinuxTool(QMainWindow):
    #window = QWidget()
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.homedir = os.path.expanduser("~")
        self.appdir = self.homedir + "/.LinuxTool"
        self.venvdir = self.appdir + "/.venv"


        if not os.path.exists(self.appdir):
            #TODO - replace this with a UI prompt
            print("Application not installed")
            return

    def SetupUI(self):
        self.setWindowTitle("Linux Tool App")
        self.setGeometry(0,0, 800, 600)
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        #self.setStyleSheet("background-color: grey;")
        self.MainWidget = QWidget(self)
        self.MainWidget.setStyleSheet("background-color: grey;");
        self.MainWidget.setWindowTitle("PyQt5 App")
        self.MainWidget.setGeometry(0, 0, 800, 600)
        #window.move(frameGm.topLeft())

        fixedSize = QSize(800,600);
        self.setMinimumSize(fixedSize);
        self.setMaximumSize(fixedSize);
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed);

        #self.ExportAction = QAction("&Export configuration", self.MainWidget)
        #self.ExportAction.setShortcut("Ctrl+Q")
        #self.ExportAction.setStatusTip('Leave The App')
        #self.quitAction.triggered.connect(sys.exit())

        #self.quitAction = QAction("&Import configuration", self)
        #self.quitAction.setShortcut("Ctrl+Q")
        #self.quitAction.setStatusTip('Leave The App')
        #self.quitAction.triggered.connect(sys.exit())

        #self.statusBar()

        #self.MainMenu = self.menuBar()
        #self.fileMenu = self.MainMenu.addMenu('&File')
        #self.fileMenu.addAction(self.ExportAction)

        self.MainWidget.layout = QVBoxLayout(self.MainWidget)
        self.tabWidget = QTabWidget(self.MainWidget)

        self.overviewTab =  QWidget()
        self.servicesTab =  QWidget()
        self.networkTab =  QWidget()
        self.updatesTab =  QWidget()
        self.resourcesTab =  QWidget()

        self.tabWidget.addTab(self.overviewTab, "Overview")
        self.tabWidget.addTab(self.servicesTab, "Services")
        self.tabWidget.addTab(self.networkTab, "Network")
        self.tabWidget.addTab(self.resourcesTab, "Resources")
        self.tabWidget.addTab(self.updatesTab, "Updates")

        self.overviewTab.layout = QVBoxLayout(self)
        self.SSHAndFTPOptions = QComboBox(self.overviewTab)
        self.SSHAndFTPOptions.addItem("SSH")
        self.SSHAndFTPOptions.addItem("FTP")

        #self.SSHPortEdit = QLineEdit(self.overviewTab)

        self.SSHAndFTPPortEdit = QLineEdit(self.overviewTab)
        self.SSHAndFTPPortEdit.setGeometry(300, 50, 100, 25)

        #self.SSHAndFTPOptions.

        self.SSHPortApply = QPushButton("&Apply Changes", self.overviewTab)
        self.SSHPortApply.released.connect(self.ApplySSHAndFTPChanges)
        self.SSHPortApply.setGeometry(600, 50, 150, 25)

        #self.button1 = QPushButton("&Test")
        #self.button1.clicked.connect(self.Hello)
        #self.overviewTab.layout.addWidget(self.button1)

        #self.overviewTab.layout.addWidget(self.SSHAndFTPOptions)
        #self.overviewTab.layout.addWidget(self.SSHAndFTPPortEdit)
        #self.overviewTab.layout.addWidget(self.SSHPortApply)

        self.SSHAndFTPOptions.setGeometry(50, 50, 100, 25)

        self.overviewTab.setLayout(self.overviewTab.layout)

        self.MainWidget.layout.addWidget(self.tabWidget)
        self.MainWidget.setLayout(self.MainWidget.layout)

    def SetSSHPort(self, port, current_port):
        pattern = "Port "+ str(current_port)
        file_path = "/etc/sshd/ssh_config"
        fh, abs_path = mkstemp()
        with fdopen(fh, "w") as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(pattern, substr))
        copymode(file_path, abs_path)
        remove(file_path)
        move(abs_path, file_path)

        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        job = manager.RestartUnit('sshd.service', 'fail')

    def SetFTPPort(self, port):
        pass

    def DisableSSH(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        job = manager.RestartUnit('sshd.service', 'fail')

    def DisableFTP(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        job = manager.RestartUnit('sshd.service', 'fail')

    def WhoisIP(self):
        pass

    def ApplySSHAndFTPChanges(self):
        service = self.SSHAndFTPOptions.currentIndex()

        try:
            port = int(self.SSHAndFTPPortEdit.text())
        except ValueError:
            print("Please enter a valid port number")

        if service == 0:
            self.SetSSHPort(int(self.SSHAndFTPPortEdit.text()))
            print("Set SSHd port")
        elif service == 1:
            self.SetFTPPort(int(self.SSHAndFTPPortEdit.text()))
            print("Set FTPd port")



if __name__ == "__main__":
    app = QApplication(sys.argv)

    #elevate.elevate()

    mainWindow = LinuxTool()
    mainWindow.SetupUI()
    mainWindow.show()

    sys.exit(app.exec_())
