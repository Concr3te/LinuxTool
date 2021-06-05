import binascii
import time
import math
import csv
import datetime
import apt
import getpass
import sqlite3
import time
import apt_pkg
from time import strftime
import hashlib
import ipaddress
import os
import subprocess
import sys
import elevate
import dbus
import secrets
import string
import smtplib, ssl
import subprocess
import pandas as pd
from subprocess import run
from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove
from PyQt5.QtWidgets import QApplication, QPlainTextEdit
from PyQt5.QtWidgets import QTableWidget, QGraphicsView,  QGraphicsPixmapItem
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, QEvent, QThread
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QStandardItem, QFontMetrics
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from pyqtgraph.widgets.GraphicsView import GraphicsView

try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen

import urllib
import json

CountryList = ["Afghanistan,AF", "Åland Islands,AX", "Albania,AL", "Algeria,DZ","American Samoa,AS","Andorra,AD", "Angola,AO", "Anguilla,AI", "Antarctica,AQ", "Antigua and Barbuda,AG", "Argentina,AR", "Armenia,AM", "Aruba,AW", "Australia,AU", "Austria,AT","Azerbaijan,AZ","Bahamas,BS", "Bahrain,BH", "Bangladesh,BD", "Barbados,BB", "Belarus,BY", "Belgium,BE", "Belize,BZ", "Benin,BJ", "Bermuda,BM","Bhutan,BT", 'Bolivia "Plurinational State of",BO','Bonaire, Sint Eustatius and Saba",BQ',"Bosnia and Herzegovina,BA", "Botswana,BW","Bouvet Island,BV","Brazil,BR","British Indian Ocean Territory,IO","Brunei Darussalam,BN","Bulgaria,BG","Burkina Faso,BF","Burundi,BI","Cambodia,KH","Cameroon,CM","Canada,CA","Cape Verde,CV","Cayman Islands,KY","Central African Republic,CF", "Chad,TD", "Chile,CL", "China,CN", "Christmas Island,CX", "Cocos (Keeling) Islands,CC", "Colombia,CO", "Comoros,KM", "Congo,CG",'Congo, the Democratic Republic of the",CD', "Cook Islands,CK", "Costa Rica,CR", "Côte d'Ivoire,CI", "Croatia,HR", "Cuba,CU", "Curaçao,CW", "Cyprus,CY", "Czech Republic,CZ", "Denmark,DK", "Djibouti,DJ", "Dominica,DM", "Dominican Republic,DO", "Ecuador,EC", "Egypt,EG", "El Salvador,SV", "Equatorial Guinea,GQ", "Eritrea,ER", "Estonia,EE", "Ethiopia,ET", "Falkland Islands (Malvinas),FK", "Faroe Islands,FO", "Fiji,FJ", "Finland,FI", "France,FR", "French Guiana,GF", "French Polynesia,PF", "French Southern Territories,TF", "Gabon,GA", "Gambia,GM" "Georgia,GE" "Germany,DE" "Ghana,GH","Gibraltar,GI", "Greece,GR", "Greenland,GL", "Grenada,GD","Guadeloupe,GP", "Guam,GU","Guatemala,GT","Guernsey,GG","Guinea,GN","Guinea-Bissau,GW","Guyana,GY","Haiti,HT","Heard Island and McDonald Islands,HM","Holy See (Vatican City State),VA","Honduras,HN","Hong Kong,HK","Hungary,HU","Iceland,IS","India,IN","Indonesia,ID",'Iran, Islamic Republic of",IR',"Iraq,IQ","Ireland,IE","Isle of Man,IM","Israel,IL","Italy,IT","Jamaica,JM","Japan,JP","Jersey,JE", "Jordan,JO", "Kazakhstan,KZ","Kenya,KE","Kiribati,KI", """Korea, Democratic People's Republic of",KP""",'Korea, Republic of",KR',"Kuwait,KW","Kyrgyzstan,KG","Lao People's Democratic Republic,LA","Latvia,LV","Lebanon,LB","Lesotho,LS","Liberia,LR","Libya,LY","Liechtenstein,LI","Lithuania,LT","Luxembourg,LU","Macao,MO",'Macedonia, the Former Yugoslav Republic of",MK' ,"Madagascar,MG" ,"Malawi,MW" ,"Malaysia,MY" ,"Maldives,MV" ,"Mali,ML" ,"Malta,MT" ,"Marshall Islands,MH" ,"Martinique,MQ" ,"Mauritania,MR" ,"Mauritius,MU" ,"Mayotte,YT" ,"Mexico,MX" ,'Micronesia, Federated States of",FM' ,'Moldova, Republic of",MD', "Monaco,MC" ,"Mongolia,MN" ,"Montenegro,ME" ,"Montserrat,MS" ,"Morocco,MA" ,"Mozambique,MZ" ,"Myanmar,MM" ,"Namibia,NA" ,"Nauru,NR" ,"Nepal,NP" ,"Netherlands,NL" ,"New Caledonia,NC" ,"New Zealand,NZ" ,"Nicaragua,NI" ,"Niger,NE" ,"Nigeria,NG" ,"Niue,NU" ,"Norfolk Island,NF" ,"Northern Mariana Islands,MP" ,"Norway,NO" ,"Oman,OM" ,"Pakistan,PK" ,"Palau,PW" ,'Palestine, State of",PS' ,"Panama,PA" ,"Papua New Guinea,PG" ,"Paraguay,PY" ,
        "Peru,PE" ,"Philippines,PH" ,"Pitcairn,PN" ,"Poland,PL" ,"Portugal,PT" ,"Puerto Rico,PR" ,"Qatar,QA" ,"Réunion,RE" ,"Romania,RO" ,"Russian Federation,RU" ,"Rwanda,RW" ,"Saint Barthélemy,BL" ,'Saint Helena, Ascension and Tristan da Cunha",SH' ,"Saint Kitts and Nevis,KN" ,"Saint Lucia,LC" ,"Saint Martin (French part),MF" ,"Saint Pierre and Miquelon,PM" ,"Saint Vincent and the Grenadines,VC" ,"Samoa,WS" ,"San Marino,SM" ,"Sao Tome and Principe,ST" ,"Saudi Arabia,SA" ,"Senegal,SN" ,"Serbia,RS" ,"Seychelles,SC" ,"Sierra Leone,SL" ,"Singapore,SG" ,"Sint Maarten (Dutch part),SX" ,"Slovakia,SK" ,"Slovenia,SI" ,"Solomon Islands,SB" ,"Somalia,SO" ,"South Africa,ZA" ,"South Georgia and the South Sandwich Islands,GS" ,"South Sudan,SS" ,"Spain,ES" ,"Sri Lanka,LK" ,"Sudan,SD" ,"Suriname,SR" ,"Svalbard and Jan Mayen,SJ" ,"Swaziland,SZ" ,"Sweden,SE" ,"Switzerland,CH" ,"Syrian Arab Republic,SY" ,'Taiwan, Province of China",TW' ,"Tajikistan,TJ" ,'Tanzania, United Republic of",TZ' ,"Thailand,TH" ,"Timor-Leste,TL" ,"Togo,TG" ,"Tokelau,TK" ,"Tonga,TO" ,"Trinidad and Tobago,TT" ,"Tunisia,TN" ,"Turkey,TR", "Turkmenistan,TM", "Turks and Caicos Islands,TC","Tuvalu,TV", "Uganda,UG", "Ukraine,UA","United Arab Emirates,AE","United Kingdom,GB","United States,US","United States Minor Outlying Islands,UM", "Uruguay,UY","Uzbekistan,UZ", "Vanuatu,VU", 'Venezuela, Bolivarian Republic of,VE',"Viet Nam,VN",'Virgin Islands, British",VG','Virgin Islands,VI',"Wallis and Futuna,WF","Western Sahara,EH","Yemen,YE","Zambia,ZM","Zimbabwe,ZW"]

class CheckableComboBox(QComboBox):

    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        # Make the lineedit the same color as QPushButton
        #palette = qApp.palette()
        #palette.setBrush(QPalette.Base, palette.button())
        #self.lineEdit().setPalette(palette)

        # Use custom delegate
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.updateText)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.closeOnLineEditClick = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def resizeEvent(self, event):
        # Recompute text to elide as needed
        self.updateText()
        super().resizeEvent(event)

    def eventFilter(self, object, event):

        if object == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if self.closeOnLineEditClick:
                    self.hidePopup()
                else:
                    self.showPopup()
                return True
            return False

        if object == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == QtCore.Qt.Checked:
                    item.setCheckState(QtCore.Qt.Unchecked)
                else:
                    item.setCheckState(QtCore.Qt.Checked)
                return True
        return False

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.closeOnLineEditClick = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.updateText()

    def timerEvent(self, event):
        # After timeout, kill timer, and reenable click on line edit
        self.killTimer(event.timerId())
        self.closeOnLineEditClick = False

    def updateText(self):
        texts = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == QtCore.Qt.Checked:
                texts.append(self.model().item(i).text())
        text = ", ".join(texts)

        # Compute elided text (with "...")
        metrics = QFontMetrics(self.lineEdit().font())
        elidedText = metrics.elidedText(text, QtCore.Qt.ElideRight, self.lineEdit().width())
        self.lineEdit().setText(elidedText)

    def addItem(self, text, data=None):
        item = QStandardItem()
        item.setText(text)
        if data is None:
            item.setData(text)
        else:
            item.setData(data)
        item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable)
        item.setData(QtCore.Qt.Unchecked, QtCore.Qt.CheckStateRole)
        self.model().appendRow(item)

    def addItems(self, texts, datalist=None):
        for i, text in enumerate(texts):
            try:
                data = datalist[i]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def currentData(self):
        # Return the list of selected items data
        res = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == QtCore.Qt.Checked:
                res.append(self.model().item(i).data())
        return res


class LinuxTool(QMainWindow):
    #window = QWidget()
    def __init__(self, appdir, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.appdir = appdir 
        self.venvdir = self.appdir + "/.venv"

        self.SYNAPTIC_PINFILE = "/var/lib/synaptic/preferences"
        self.DISTRO = subprocess.check_output(["lsb_release", "-c", "-s"],
                                 universal_newlines=True).strip()

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
        self.setWindowTitle("Linux Tool Login")

        self.AppUserName = QLineEdit()
        self.AppUserNameInputLabel = QLabel("Username")
        self.AppUserPassword = QLineEdit()
        self.AppUserPasswordInputLabel = QLabel("Password")
        self.AppUserPassword.setEchoMode(QLineEdit.Password)

        self.AppLoginButton = QPushButton("&Login")
        self.AppLoginButtonPadding = QPushButton()

        self.AppLoginButton.setFixedSize(100, 25)
        self.AppLoginButton.clicked.connect(self.AppLogin)
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

    def GetNetwork(self):
        INTERVAL = 5            #   1 second
        AVG_LOW_PASS = 0.2      #   Simple Complemetary Filter
        self.idata = self.GetNetworkInterfaces()
        allvalues = []
        txvalues = []
        rxvalues = []
        data = [["RX", "TX"]]
        for eth in self.idata:
            self.ifaces[eth["interface"]]["rxrate"]      =   (eth["rx"]["bytes"] - self.ifaces[eth["interface"]]["recvbytes"]) / INTERVAL
            self.ifaces[eth["interface"]]["txrate"]      =   (eth["tx"]["bytes"] - self.ifaces[eth["interface"]]["sendbytes"]) / INTERVAL
            self.ifaces[eth["interface"]]["recvbytes"]   =   eth["rx"]["bytes"]
            self.ifaces[eth["interface"]]["sendbytes"]   =   eth["tx"]["bytes"]
            self.ifaces[eth["interface"]]["avgrx"]       =   int(self.ifaces[eth["interface"]]["rxrate"] * AVG_LOW_PASS + self.ifaces[eth["interface"]]["avgrx"] * (1.0-AVG_LOW_PASS))
            self.ifaces[eth["interface"]]["avgtx"]       =   int(self.ifaces[eth["interface"]]["txrate"] * AVG_LOW_PASS + self.ifaces[eth["interface"]]["avgtx"] * (1.0-AVG_LOW_PASS))
            self.ifaces[eth["interface"]]["toprx"]       =   self.ifaces[eth["interface"]]["rxrate"] if self.ifaces[eth["interface"]]["rxrate"] > self.ifaces[eth["interface"]]["toprx"] else self.ifaces[eth["interface"]]["toprx"]
            self.ifaces[eth["interface"]]["toptx"]       =   self.ifaces[eth["interface"]]["txrate"] if self.ifaces[eth["interface"]]["txrate"] > self.ifaces[eth["interface"]]["toptx"] else self.ifaces[eth["interface"]]["toptx"]
            rxvalues.append(self.ifaces[eth["interface"]]["rxrate"])
            txvalues.append(self.ifaces[eth["interface"]]["txrate"])

        allvalues.append(rxvalues)
        allvalues.append(txvalues)

        self.NetworkStatus.setRowCount(len(allvalues))

        for row in range(len(allvalues)):
                for column in range(len(allvalues[0])):
                    self.NetworkStatus.setItem(row, column + 1,  QTableWidgetItem(str(allvalues[row][column])))

        self.NetworkStatus.setItem(0, 0, QTableWidgetItem("RX"))
        self.NetworkStatus.setItem(1, 0, QTableWidgetItem("TX"))

    def applogin(self, username, password):
        conn = sqlite3.connect(self.appdir + "/database.db")
        cur = conn.cursor()
        query = 'SELECT password from login WHERE username = "{username}"'.format(username=username)
        with open("logfile.txt", "w") as f:
            f.write(query)
        cur.execute(query)
        thispassword = cur.fetchall()
        stored_password = thispassword[0][0]
        if not stored_password:
            return
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    def AppLogin(self):
        login = self.applogin(self.AppUserName.text(), self.AppUserPassword.text())
        if login:
            self.LoginWidget.hide()
            self.SetupUI()

    def SetupUI(self):
        self.setWindowTitle("Linux Tool App")
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        self.MainWidget = QWidget(self)
        #self.MainWidget.setStyleSheet("background-color: grey;");
        self.setCentralWidget(self.MainWidget)
        self.MainWidget.setWindowTitle("PyQt5 App")
        self.MainWidget.setGeometry(0, 0, 800, 600)

        self.UpdateTimer = QTimer()
        self.UpdateTimer.timeout.connect(self.UpdateResourcesTab)
        self.UpdateTimer.start(1000)

        self.ConnectionsUpdateTimer = QTimer()
        self.ConnectionsUpdateTimer.timeout.connect(self.GetConnections)
        self.ConnectionsUpdateTimer.start(5000)

        self.NetworkTimerTrigger = QTimer()
        self.NetworkTimerTrigger.timeout.connect(self.GetNetwork)
        self.NetworkTimerTrigger.start(1000)

        self.EmailSendTimer = QTimer()
        self.EmailSendTimer.timeout.connect(self.SendEmail)
        self.EmailSendTimer.start(1000 * 60 * 30)

        fixedSize = QSize(800,600);
        self.setMinimumSize(fixedSize);
        self.setMaximumSize(fixedSize);
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed);

        self.MainWidget.layout = QVBoxLayout(self.MainWidget)
        self.tabWidget = QTabWidget(self.MainWidget)

        self.overviewTab =  QWidget()
        self.servicesTab =  QWidget()
        self.networkTab =  QWidget()
        self.updatesTab =  QWidget()
        self.resourcesTab =  QWidget()
        self.emailTab = QWidget()
        self.logsTab = QWidget()
        #self.whoisTab = QWidget()
        self.aboutTab = QWidget()
        self.connectionsTab = QWidget()

        self.tabWidget.addTab(self.overviewTab, "Overview")
        self.tabWidget.addTab(self.servicesTab, "Manage")
        self.tabWidget.addTab(self.networkTab, "Network")
        self.tabWidget.addTab(self.resourcesTab, "Resources")
        self.tabWidget.addTab(self.emailTab, "Email")
        self.tabWidget.addTab(self.updatesTab, "Updates")
        self.tabWidget.addTab(self.logsTab, "Logs")
        #self.tabWidget.addTab(self.whoisTab, "Whois")
        self.tabWidget.addTab(self.connectionsTab, "Connections")
        self.tabWidget.addTab(self.aboutTab, "About")

        self.Icon = QPixmap("/usr/share/icons/Humanity/apps/128/access.svg")
        #self.Icon = self.Icon.scaledToHeight(100)
        self.IconLabel = QLabel(self.aboutTab)
        self.IconLabel.setPixmap(self.Icon)
        self.IconLabel.setGeometry(300, 100, 128, 128)

        self.AboutInformation = QLabel(self.aboutTab)
        self.AboutInformation.setGeometry(200, 250, 350, 200)

        text = """
                
               This application was developed by 
                        David Kiarie.

               """

        self.AboutInformation.setText(text)

        self.overviewTab.layout = QVBoxLayout(self)

        self.OverviewServicesLabel = QLabel("Service", self.overviewTab)
        self.OverviewServicesLabel.setGeometry(50, 50, 100, 25)

        self.OverviewServicesStatusLabel = QLabel("Status", self.overviewTab)
        self.OverviewServicesStatusLabel.setGeometry(200, 50, 100, 25)

        self.OverviewPortLabel = QLabel("Port", self.overviewTab)
        self.OverviewPortLabel.setGeometry(400, 50, 100, 25)

        self.OverviewActionLabel = QLabel("Action", self.overviewTab)
        self.OverviewActionLabel.setGeometry(600, 50, 100, 25)

        self.OverviewSSHService = QLabel("SSH", self.overviewTab)
        self.OverviewSSHService.setGeometry(50, 100, 100, 25)

        self.OverviewFTPService = QLabel("FTP", self.overviewTab)
        self.OverviewFTPService.setGeometry(50, 200, 100, 25)

        self.OverviewSSHStatus = QLineEdit(self.overviewTab)
        self.OverviewSSHStatus.setReadOnly(True)
        self.OverviewSSHStatus.setGeometry(200, 100, 150, 25)
        self.OverviewSSHStatus.setText(self.GetSSHStatus())

        self.OverviewFTPStatus = QLineEdit(self.overviewTab)
        self.OverviewFTPStatus.setReadOnly(True)
        self.OverviewFTPStatus.setGeometry(200, 200, 150, 25)
        self.OverviewFTPStatus.setText(self.GetFTPStatus())

        self.OverviewSSHPort = QLineEdit(self.overviewTab)
        self.OverviewSSHPort.setReadOnly(True)
        self.OverviewSSHPort.setGeometry(400, 100, 150, 25)
        self.OverviewSSHPort.setText(str(self.GetSSHPort()))

        self.OverviewFTPPort = QLineEdit(self.overviewTab)
        self.OverviewFTPPort.setReadOnly(True)
        self.OverviewFTPPort.setGeometry(400, 200, 150, 25)
        self.OverviewFTPPort.setText(str(self.GetFTPPort()))

        self.OverviewSSHAction = QPushButton(self.getSSHAction(), self.overviewTab)
        self.OverviewSSHAction.setGeometry(600, 100, 100, 25)
        self.OverviewSSHAction.clicked.connect(self.SSHAction)

        self.OverviewFTPAction = QPushButton(self.getFTPAction(), self.overviewTab)
        self.OverviewFTPAction.setGeometry(600, 200, 100, 25)
        self.OverviewFTPAction.clicked.connect(self.FTPAction)

        self.SSHAndFTPOptions = QComboBox(self.overviewTab)
        self.SSHAndFTPOptions.addItem("SSH")
        self.SSHAndFTPOptions.addItem("FTP")
        self.SSHAndFTPOptions.setGeometry(50, 300, 100, 25)

        self.SSHAndFTPPortEdit = QLineEdit(self.overviewTab)
        self.SSHAndFTPPortEdit.setGeometry(400, 300, 100, 25) 
        self.SSHAndFTPPortEditLabel = QLabel("Desired Port", self.overviewTab)
        self.SSHAndFTPPortEditLabel.setGeometry(250, 300, 100, 25)

        self.SSHPortApply = QPushButton("&Apply Changes", self.overviewTab)
        self.SSHPortApply.setGeometry(600, 300, 150, 25)
        self.SSHPortApply.clicked.connect(self.ApplySSHAndFTPChanges)

        self.ConfigImport = QPushButton("&Import Configuration", self.overviewTab)
        self.ConfigImport.setGeometry(50, 400, 200, 25)
        self.ConfigImport.clicked.connect(self.ImportConfigFiles)

        self.ConfigExport = QPushButton("&Export Configuration", self.overviewTab)
        self.ConfigExport.setGeometry(50, 500, 200, 25)
        self.ConfigExport.clicked.connect(self.ExportConfigFiles)

        #resources tab
        self.CPULoadValues = []
        self.VirtualMemoryValues = []
        self.SwapMemoryValues = []
        self.NetworkTransferedValues = []
        self.NetworkRecievedValues = []
        self.PlotAgainstValues = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

        self.CPULoadGraphLabel = QLabel("CPU load", self.resourcesTab)
        self.CPULoadGraphLabel.setGeometry(300, 10, 100, 15)

        self.CPULoadGraph = PlotWidget(self.resourcesTab)
        self.CPULoadGraph.setGeometry(80, 30, 600, 150)
        self.CPULoadGraph.setXRange(0, 60)
        self.CPULoadGraph.setYRange(0, 100)

        self.VirtualMemoryUsageLabel = QLabel("Memory Usage", self.resourcesTab)
        self.VirtualMemoryUsageLabel.setGeometry(300, 200, 100, 15)

        self.VirtualMemoryUsage = PlotWidget(self.resourcesTab)
        self.VirtualMemoryUsage.setGeometry(80, 220, 600, 150)
        self.VirtualMemoryUsage.setXRange(0, 60)
        self.VirtualMemoryUsage.setYRange(0, 100)

        self.DiskUsageTimer = QTimer()
        self.DiskUsageTimer.timeout.connect(self.getDiskSpace)
        #Don't run this one too often
        self.DiskUsageTimer.start(20000)

        self.DiskUsageLabel = QLabel("Disk Usage", self.resourcesTab)
        self.DiskUsageLabel.setGeometry(80, 500, 100, 25)

        self.DiskUsagePercentage = QLineEdit(self.resourcesTab)
        self.DiskUsagePercentage.setGeometry(200, 500, 100, 25)
        #run once at start
        self.getDiskSpace()

        self.overviewTab.setLayout(self.overviewTab.layout)
        self.MainWidget.layout.addWidget(self.tabWidget)
        self.MainWidget.setLayout(self.MainWidget.layout)
        self.ifaces = {}
        self.idata = self.GetNetworkInterfaces()
        for eth in self.idata:
            self.ifaces[eth["interface"]] = {
                "rxrate"    :   0,
                "txrate"    :   0,
                "avgrx"     :   0,
                "avgtx"     :   0,
                "toptx"     :   0,
                "toprx"     :   0,
                "sendbytes" :   eth["tx"]["bytes"],
                "recvbytes" :   eth["rx"]["bytes"]
                }

        tablelabels = ["RX/TX"]
        for eth in self.idata:
            tablelabels.append(eth["interface"])

        self.NetworkStatus = QTableWidget(0, len(tablelabels), self.resourcesTab)
        self.NetworkStatus.horizontalHeader().setStretchLastSection(True)
        self.NetworkStatus.setGeometry(80, 400, 600, 80)
        self.NetworkStatus.setHorizontalHeaderLabels(tablelabels)

        #self.NetworkStatus.setColumnWidth(2, 200)
        #self.NetworkStatus.setColumnWidth(1, 200)
        self.NetworkStatus.setColumnWidth(0, 150)


        #email tab
        self.SenderEmailLabel = QLabel("Sender Email", self.emailTab)
        self.SenderEmailLabel.setGeometry(50, 60, 100, 25)
        self.SenderEmailEdit = QLineEdit(self.emailTab)
        self.SenderEmailEdit.setGeometry(250, 60, 100, 25)

        self.SenderPasswordLabel = QLabel("Sender Password", self.emailTab)
        self.SenderPasswordLabel.setGeometry(400, 60, 150, 25)
        self.SenderPasswordEdit = QLineEdit(self.emailTab)
        self.SenderPasswordEdit.setGeometry(550, 60, 100, 25)

        self.SMTPServerLabel = QLabel("SMTP Server address", self.emailTab)
        self.SMTPServerLabel.setGeometry(50, 190, 150, 25)
        self.SMTPServerEdit = QLineEdit(self.emailTab)
        self.SMTPServerEdit.setGeometry(250, 190, 100, 25)

        self.SMTPPortLabel = QLabel("SMTP Server Port", self.emailTab)
        self.SMTPPortLabel.setGeometry(400, 190, 150, 25)
        self.SMTPPortEdit = QLineEdit(self.emailTab)
        self.SMTPPortEdit.setGeometry(550, 190, 100, 25)

        self.RecieverEmailLabel = QLabel("Recipient Email", self.emailTab)
        self.RecieverEmailLabel.setGeometry(50, 310, 150, 25)
        self.RecieverEmailEdit = QLineEdit(self.emailTab)
        self.RecieverEmailEdit.setGeometry(250, 310, 100, 25)

        self.EmailNotificationsLabel = QLabel("Enable Notifications", self.emailTab)
        self.EmailNotificationsLabel.setGeometry(50, 400, 150, 25)
        self.EmailNotificationCheckBox = QCheckBox(self.emailTab)
        self.EmailNotificationCheckBox.setGeometry(250, 400, 100, 25)

        self.SaveEmailSettingsButton = QPushButton(self.emailTab)
        self.SaveEmailSettingsButton.setText("Save Settings")
        self.SaveEmailSettingsButton.setGeometry(50, 500, 100, 25)
        self.SaveEmailSettingsButton.clicked.connect(self.SaveEmailSettings)

        #services
        self.ChangePasswordLabel = QLabel("Change Password", self.servicesTab)
        self.ChangePasswordLabel.setGeometry(50, 10, 150, 25)
        self.InputUserNameLabel = QLabel("Username", self.servicesTab)
        self.InputUserNameLabel.setGeometry(50, 50, 100, 25)
        self.InputUserNameEdit = QLineEdit(self.servicesTab)
        self.InputUserNameEdit.setGeometry(200, 50, 100, 25)
        self.InputOldPasswordLabel = QLabel("Old password", self.servicesTab)
        self.InputOldPasswordLabel.setGeometry(310, 50, 120, 25)
        self.InputOldPasswordEdit = QLineEdit(self.servicesTab)
        self.InputOldPasswordEdit.setEchoMode(QLineEdit.Password)
        self.InputOldPasswordEdit.setGeometry(420, 50, 100, 25)
        self.InputNewPasswordLabel = QLabel("New password", self.servicesTab)
        self.InputNewPasswordLabel.setGeometry(530, 50, 120, 25)
        self.InputNewPasswordEdit = QLineEdit(self.servicesTab)
        self.InputNewPasswordEdit.setEchoMode(QLineEdit.Password)
        self.InputNewPasswordEdit.setGeometry(640, 50, 100, 25)
        self.NewPasswordApply = QPushButton("Apply", self.servicesTab)
        self.NewPasswordApply.setGeometry(50, 100, 100, 25)
        self.NewPasswordApply.clicked.connect(self.ChangePassword)
        self.NewPasswordGenerate = QPushButton("Generate Password", self.servicesTab)
        self.NewPasswordGenerate.setGeometry(200, 100, 150, 25)
        self.NewPasswordGenerate.clicked.connect(self.GeneratePassword)

        self.ChangeUsernameLabel = QLabel("Change username", self.servicesTab)
        self.ChangeUsernameLabel.setGeometry(50, 155, 150, 25)
        self.InputUserNameLabel = QLabel("Current Username", self.servicesTab)
        self.InputUserNameLabel.setGeometry(50, 205, 150, 25)
        self.InputUserNameCurrent = QLineEdit(self.servicesTab)
        self.InputUserNameCurrent.setGeometry(200, 205, 100, 25)
        self.InputNewUsernameLabel = QLabel("New Username", self.servicesTab)
        self.InputNewUsernameLabel.setGeometry(305, 205, 120, 25)
        self.InputNewUserName = QLineEdit(self.servicesTab)
        self.InputNewUserName.setGeometry(420, 205, 100, 25)
        self.InputPasswordLabel = QLabel("Password", self.servicesTab)
        self.InputPasswordLabel.setGeometry(530, 205, 100, 25)
        self.InputPasswordEdit = QLineEdit(self.servicesTab)
        self.InputPasswordEdit.setEchoMode(QLineEdit.Password)
        self.InputPasswordEdit.setGeometry(620, 205, 100, 25)
        self.NewUserNameApply = QPushButton("Apply", self.servicesTab)
        self.NewUserNameApply.setGeometry(50, 260, 100, 25)
        self.NewUserNameApply.clicked.connect(self.ChangeUsername)

        self.DisableShellAccessLabel = QLabel(self.GetShellAccessAction(), self.servicesTab)
        self.DisableShellAccessLabel.setGeometry(50, 310, 300, 25)
        self.DisableShellAccessButton = QPushButton(self.GetShellAccessAction(), self.servicesTab)
        self.DisableShellAccessButton.setGeometry(50, 350, 200, 25)
        self.DisableShellAccessButton.clicked.connect(self.ShellAccessAction)

        self.FactoryResetLabel = QLabel("Factory Reset", self.servicesTab)
        self.FactoryResetLabel.setGeometry(400, 310, 300, 25)
        self.FactoryResetButton = QPushButton("Factory Reset", self.servicesTab)
        self.FactoryResetButton.setGeometry(400, 350, 200, 25)
        self.FactoryResetButton.clicked.connect(self.FactoryResetAction)

        self.LetsEncryptLabel = QLabel("Let's Encrypt", self.servicesTab)
        self.LetsEncryptLabel.setGeometry(400, 400, 100, 25)
        self.LetsEncryptButton = QPushButton("Let's Encrypt", self.servicesTab)
        self.LetsEncryptButton.setGeometry(400, 450, 100, 25)
        self.LetsEncryptButton.clicked.connect(self.LetsEncrypt)

        self.LetsEncryptDomain = QLineEdit(self.servicesTab)
        self.LetsEncryptDomain.setGeometry(600, 450, 100, 25)

        #logs
        self.LiveLog = QPlainTextEdit(self.logsTab)
        self.LiveLog.setGeometry(10, 10, 750, 600)
        self.LiveLog.setReadOnly(True)
        #self.LiveLog.appendPlainText("Log")

        #connections
        self.CurrentConnectionsLabel = ["Netid", "Connection State", "Local Port/A#ddress", "Peer IP/Port", "Peer Country"]
        self.CurrentConnections = QTableWidget(0, len(self.CurrentConnectionsLabel), self.connectionsTab)
        self.CurrentConnections.setGeometry(10, 10, 750, 600)
        self.CurrentConnections.setColumnWidth(2, 200)
        self.CurrentConnections.setColumnWidth(1, 200)
        self.CurrentConnections.horizontalHeader().setStretchLastSection(True)
        self.CurrentConnections.setHorizontalHeaderLabels(self.CurrentConnectionsLabel)

        #updates
        self.CheckForUpdates = QPushButton("&Check", self.updatesTab)
        self.CheckForUpdates.setGeometry(550, 50, 100, 25)
        self.CheckForUpdates.clicked.connect(self.get_update_packages)

        self.CheckForUpdates = QPushButton("&Lock/Unlock", self.updatesTab)
        self.CheckForUpdates.setGeometry(350, 50, 100, 25)

        self.UpdatePackages = QPushButton("&Update", self.updatesTab)
        self.UpdatePackages.setGeometry(150, 50, 100, 25)
        self.UpdatePackages.clicked.connect(self.UpdateSelectedPackages)

        self.UpdatesLabels = ['name', 'security', 'current', 'candidate', 'priority', 'locked']
        self.PossibleUpdates = QTableWidget(0, len(self.UpdatesLabels), self.updatesTab)
        self.PossibleUpdates.setHorizontalHeaderLabels(self.UpdatesLabels)
        self.PossibleUpdates.setGeometry(50, 100, 650, 400)

        self.get_update_packages()
        #networking

        self.UpdatesAction = QPushButton(self.updatesTab)
        self.UpdatesAction.setText(self.UpdateActionText())
        self.UpdatesAction.setGeometry(350, 510, 100, 25)
        self.UpdatesAction.clicked.connect(self.ApplyUpdatesAction)

        self.CountryListLabel = QLabel("Country", self.networkTab)
        self.CountryListLabel.setGeometry(50, 10, 150, 25)
        self.CountryListCombo = CheckableComboBox(self.networkTab)
        for country in CountryList:
            self.CountryListCombo.addItem(country)
        self.CountryListCombo.setGeometry(50, 50, 150, 25)
        self.BanOrUnbanPortLabel = QLabel("Target Port", self.networkTab)
        self.BanOrUnbanPortLabel.setGeometry(250, 10, 150, 25)
        self.BanOrUnbanPort = QLineEdit(self.networkTab)
        self.BanOrUnbanPort.setGeometry(250, 50, 50, 25)
        self.ExcludeAction = QPushButton("&Exclude", self.networkTab)
        self.ExcludeAction.setGeometry(350, 50, 100, 25)
        self.ExcludeAction.clicked.connect(self.ExcludeCountries)
        self.BanAction = QPushButton("&Ban", self.networkTab)
        self.BanAction.setGeometry(500, 50, 100, 25)
        self.BanAction.clicked.connect(self.BanCountries)
        self.UnBanAction = QPushButton("&Unban", self.networkTab)
        self.UnBanAction.setGeometry(650, 50, 100, 25)
        self.UnBanAction.clicked.connect(self.UnBanCountries)

        self.ServiceListLabel = QLabel("Service", self.networkTab)
        self.ServiceListLabel.setGeometry(50, 100, 100, 25)
        self.ServiceListCombo = QComboBox(self.networkTab)
        self.ServiceListCombo.addItem("SSH")
        self.ServiceListCombo.addItem("FTP")
        self.ServiceListCombo.setGeometry(50, 150, 100, 25)
        self.AttemptsDurationLabel = QLabel("Time/Seconds", self.networkTab)
        self.AttemptsDurationLabel.setGeometry(250, 100, 100, 25)
        self.AttemptsDuration = QLineEdit(self.networkTab)
        self.AttemptsDuration.setGeometry(250, 150, 100, 25)
        self.AttemptsCount = QLabel("# Attempts", self.networkTab)
        self.AttemptsCount.setGeometry(400, 100, 100, 25)
        self.AttemptsCount = QLineEdit(self.networkTab)
        self.AttemptsCount.setGeometry(400, 150, 100, 25)
        self.ApplyServiceFilter = QPushButton("Filter", self.networkTab)
        self.ApplyServiceFilter.setGeometry(550, 150, 100, 25)
        self.ApplyServiceFilter.clicked.connect(self.ApplyServiceFilterNow)

        self.WhiteListIpLabel = QLabel("Whitelist IP", self.networkTab)
        self.WhiteListIpLabel.setGeometry(50, 200, 100, 25)
        self.WhiteListIpEdit = QLineEdit(self.networkTab)
        self.WhiteListIpEdit.setGeometry(50, 250, 100, 25)
        self.WhiteListIpButton = QPushButton("Whitelist IP", self.networkTab)
        self.WhiteListIpButton.setGeometry(200, 250, 100, 25)
        #whois
        self.WhoisIpLabel = QLabel("Whois IP", self.networkTab)
        self.WhoisIpLabel.setGeometry(50, 300, 100, 25)
        self.WhoisIpEdit = QLineEdit(self.networkTab)
        self.WhoisIpEdit.setGeometry(50, 350, 100, 25)
        self.WhoisIpButton = QPushButton("Whois IP", self.networkTab)
        self.WhoisIpButton.setGeometry(200, 350, 100, 25)
        self.WhoisIpButton.clicked.connect(self.WhoisIP)

        self.CountryFromLabel = QLabel("Country", self.networkTab)
        self.CountryFromLabel.setGeometry(50, 400, 100, 25)
        self.CountryFrom = QLineEdit(self.networkTab)
        self.CountryFrom.setReadOnly(True)
        self.CountryFrom.setGeometry(50, 450, 100, 25)
        self.CityFromLabel = QLabel("City", self.networkTab)
        self.CityFromLabel.setGeometry(200, 400, 100, 25)
        self.CityFrom = QLineEdit(self.networkTab)
        self.CityFrom.setReadOnly(True)
        self.CityFrom.setGeometry(200, 450, 100, 25)
        self.TimezoneFromLabel = QLabel("Timezone", self.networkTab)
        self.TimezoneFromLabel.setGeometry(350, 400, 150, 25)
        self.TimezoneFrom = QLineEdit(self.networkTab)
        self.TimezoneFrom.setReadOnly(True)
        self.TimezoneFrom.setGeometry(350, 450, 150, 25)
        self.IpHostNameLabel = QLabel("Hostname", self.networkTab)
        self.IpHostNameLabel.setGeometry(550, 400, 150, 25)
        self.IpHostName = QLineEdit(self.networkTab)
        self.IpHostName.setReadOnly(True)
        self.IpHostName.setGeometry(550, 450, 200, 25)
        
    def GetNetworkInterfaces(self):
        ifaces = []
        f = open("/proc/net/dev")
        data = f.read()
        f.close()
        data = data.split("\n")[2:]
        for i in data:
            if len(i.strip()) > 0:
                x = i.split()
            # Interface |                        Receive                          |                         Transmit
            #   iface   | bytes packets errs drop fifo frame compressed multicast | bytes packets errs drop fifo frame compressed multicast
                k = {
                    "interface" :   x[0][:len( x[0])-1],   
                    "tx"        :   {
                        "bytes"         :   int(x[1]),
                        "packets"       :   int(x[2]),
                        "errs"          :   int(x[3]),
                        "drop"          :   int(x[4]),
                        "fifo"          :   int(x[5]),
                        "frame"         :   int(x[6]),
                        "compressed"    :   int(x[7]),
                        "multicast"     :   int(x[8])
                        },
                    "rx"        :   {
                        "bytes"         :   int(x[9]),
                        "packets"       :   int(x[10]),
                        "errs"          :   int(x[11]),
                        "drop"          :   int(x[12]),
                        "fifo"          :   int(x[13]),
                        "frame"         :   int(x[14]),
                        "compressed"    :   int(x[15]),
                        "multicast"     :   int(x[16])
                        }
                    }
                ifaces.append(k)
        return ifaces

    def LetsEncrypt(self):
        domain = self.LetsEncryptDomain.text()

        os.system("./getssl.sh -d " + domain)

    def ApplyUpdatesAction(self):
        action = self.CheckUpdatesStatus()

        if action:
            self.DisableUpdates()
            self.UpdatesAction.setText("Enable")
        else:
            self.EnableUpdates()
            self.UpdatesAction.setText("Disable")

    def FactoryResetAction(self):
        # Flush all Iptables rules
        os.system("iptables -P INPUT ACCEPT")
        os.system("iptables -P FORWARD ACCEPT")
        os.system("iptables -P OUTPUT ACCEPT")
        os.system("iptables -F")
        os.system("iptables -X")
        os.system("iptables -Z ")
        os.system("iptables -t nat -F")
        os.system("iptables -t nat -X")
        os.system("iptables -t mangle -F")
        os.system("iptables -t mangle -X")
        os.system("iptables -t raw -F")
        os.system("iptables -t raw -X")
        os.system("iptables -P INPUT ACCEPT")
        os.system("iptables -P FORWARD ACCEPT")
        os.system("iptables -P OUTPUT ACCEPT")
        os.system("iptables -F")
        os.system("iptables -X")
        os.system("iptables -Z ")
        os.system("iptables -t nat -F")
        os.system("iptables -t nat -X")
        os.system("iptables -t mangle -F")
        os.system("iptables -t mangle -X")
        os.system("iptables -t raw -F")
        os.system("iptables -t raw -X")

        os.system("ip6tables -P INPUT ACCEPT")
        os.system("ip6tables -P FORWARD ACCEPT")
        os.system("ip6tables -P OUTPUT ACCEPT")
        os.system("ip6tables -F")
        os.system("ip6tables -X")
        os.system("ip6tables -Z ")
        os.system("ip6tables -t nat -F")
        os.system("ip6tables -t nat -X")
        os.system("ip6tables -t mangle -F")
        os.system("ip6tables -t mangle -X")
        os.system("ip6tables -t raw -F")
        os.system("ip6tables -t raw -X")
        os.system("ip6tables -P INPUT ACCEPT")
        os.system("ip6tables -P FORWARD ACCEPT")
        os.system("ip6tables -P OUTPUT ACCEPT")
        os.system("ip6tables -F")
        os.system("ip6tables -X")
        os.system("ip6tables -Z ")
        os.system("ip6tables -t nat -F")
        os.system("ip6tables -t nat -X")
        os.system("ip6tables -t mangle -F")
        os.system("ip6tables -t mangle -X")
        os.system("ip6tables -t raw -F")
        os.system("ip6tables -t raw -X")

        self.SetFTPPort(21)
        self.EnableFTP()
        self.SetSSHPort(22)
        self.EnableSSH()

        #drop all databases except users
        con = sqlite3.connect(self.appdir + "/database.db")
        cursor = con.cursor()

        check_locked = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="locked")
        cursor.execute(check_locked)

        result = cursor.fetchall()

        if result:
            query = "DROP TABLE locked"
            cursor.execute(query)
        check_email = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="email")
        cursor.execute(check_email)

        result = cursor.fetchall()

        if result:
            query = "DROP TABLE email"
            cursor.execute(query)

        con.close()

        self.UpdatesDefault()

        text = "{time} The application has been reset \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def GetConnections(self):
        print(self.appdir)
        os.system("ss -taun > " + self.appdir + "/connections.txt")
        connections = []
        with open(self.appdir + "/connections.txt") as connections_file:
            lines = connections_file.readlines()
            for line in lines:
                tmp_list = line.split(" ")
                tmp_list = [x for x in tmp_list if x]
                connections.append(tmp_list)

        #delete the first row which are the labels
        del connections[0]
        for connection in connections:
            connection.remove("\n")
            del connection[2]
            del connection[2]

        os.remove(self.appdir + "/connections.txt")

        self.CurrentConnections.setRowCount(len(connections))

        for connection in connections:
            country = self.PeerToCountry(connection[3])
            connection.append(country)

        for row in range(len(connections)):
                for column in range(len(connections[0])):
                    self.CurrentConnections.setItem(row, column, QTableWidgetItem((connections[row][column])))


    def clean(self, cache, depcache):
        """ unmark (clean) all changes from the given depcache """
        # mvo: looping is too inefficient with the new auto-mark code
        # for pkg in cache.Packages:
        #    depcache.MarkKeep(pkg)
        depcache.init()

    def saveDistUpgrade(self, cache, depcache):
        """ this functions mimics a upgrade but will never remove anything """
        depcache.upgrade(True)
        if depcache.del_count > 0:
            self.clean(cache,depcache)
        depcache.upgrade()

    def PeerToCountry(self, peer):
        ip = peer.split(":")[0]

        if ip == "[":
            ip = "::"

        if ip == "*":
            ip = "0.0.0.0"

        con = sqlite3.connect(self.appdir + "/database.db")

        cur = con.cursor()

        #SELECT country_name from ipv4 WHERE CAST(start_range AS INT) <= 578108241 AND CAST(end_range AS INT) >= 578108241

        query = 'SELECT country_name from ipv4 WHERE CAST(start_range as INT) <= {ip} AND CAST(end_range as INT) >= {ip}'.format(ip=int(ipaddress.ip_address(ip)))
        cur.execute(query)

        status = cur.fetchall()

        status = status[0][0]

        if status == '-':
            return "N/A"
        else:
            return status

    def IsLocked(self, package):
        con = sqlite3.connect(self.appdir + "/database.db")

        cur = con.cursor()

        check_locked = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="locked")
        cur.execute(check_locked)

        result = cur.fetchall()

        if not result:
            return "NO"

        query = 'SELECT package from locked WHERE package == "{package}"'.format(package=package)

        cur.execute(query)

        status = cur.fetchall()

        if status:
            return "Yes"
        else:
            return "No"

    def isSecurityUpgrade(self, pkg, depcache):
        def isSecurityUpgrade_helper(ver):
            """ check if the given version is a security update (or masks one) """
            security_pockets = [("Ubuntu", "%s-security" % self.DISTRO),
                                ("gNewSense", "%s-security" % self.DISTRO),
                                ("Debian", "%s-updates" % self.DISTRO)]
            for (file, index) in ver.file_list:
                for origin, archive in security_pockets:
                    if (file.archive == archive and file.origin == origin):
                        return True
            return False

        inst_ver = pkg.current_ver
        cand_ver = depcache.get_candidate_ver(pkg)

        if isSecurityUpgrade_helper(cand_ver):
            return True

        # now check for security updates that are masked by a
        # canidate version from another repo (-proposed or -updates)
        for ver in pkg.version_list:
            if (inst_ver and
                    apt_pkg.version_compare(ver.ver_str, inst_ver.ver_str) <= 0):
                #print "skipping '%s' " % ver.VerStr
                continue
            if isSecurityUpgrade_helper(ver):
                return True
        return False

    def get_update_packages(self):
        """
        Return a list of dict about package updates
        """

        #packages = '{ "packages" :{}}'

        pkgs = [] 

        apt_pkg.init()
        # force apt to build its caches in memory for now to make sure
        # that there is no race when the pkgcache file gets re-generated
        apt_pkg.config.set("Dir::Cache::pkgcache","")

        try:
            cache = apt_pkg.Cache(apt.progress.base.OpProgress())
        except SystemError as e:
            sys.stderr.write("Error: Opening the cache (%s)" % e)
            sys.exit(-1)

        depcache = apt_pkg.DepCache(cache)
        # read the pin files
        depcache.read_pinfile()
        # read the synaptic pins too
        if os.path.exists(self.SYNAPTIC_PINFILE):
            depcache.read_pinfile(self.SYNAPTIC_PINFILE)
            # init the depcache
        depcache.init()

        try:
            self.saveDistUpgrade(cache,depcache)
        except SystemError as e:
            sys.stderr.write("Error: Marking the upgrade (%s)" % e)
            sys.exit(-1)

        # use assignment here since apt.Cache() doesn't provide a __exit__ method
        # on Ubuntu 12.04 it looks like
        # aptcache = apt.Cache()
        for pkg in cache.packages:
            if not (depcache.marked_install(pkg) or depcache.marked_upgrade(pkg)):
                continue
            inst_ver = pkg.current_ver
            cand_ver = depcache.get_candidate_ver(pkg)
            if cand_ver == inst_ver:
                continue
            record = {"name": pkg.name,
                      "security": self.isSecurityUpgrade(pkg, depcache),
                      #"section": pkg.section,
                      "current_version": inst_ver.ver_str if inst_ver else '-',
                      "candidate_version": cand_ver.ver_str  if cand_ver else '-',
                      "priority": cand_ver.priority_str,
                      "locked":self.IsLocked(pkg.name)}
            pkgs.append(record)
        packages = []
        for item in pkgs:
            tmp = []
            for key, value in item.items():
                tmp.append(value)
            packages.append(tmp)

        #self.PossibleUpdates.setColumnCount(len(packages[0]))
        self.PossibleUpdates.setRowCount(len(packages))

        for row in range(len(packages)):
                for column in range(len(packages[0])):
                    self.PossibleUpdates.setItem(row, column, QTableWidgetItem((packages[row][column])))

        text = "{time} Checked for updates \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def RemoveIPFromBan(self):
        #iptables -I INPUT -s <allowed_ip> -j ACCEPT 
        self.WhiteListIpEdit = QLineEdit(self.networkTab)

        rule = "iptables -I INPUT -s {ip} -j ACCEPT".format(int(self.WhiteListIpEdit()))

        os.system(rule)

        text = "{time} Whitelisted IP: {ip} \n".format(time = datetime.datetime.now(), ip = int(self.WhiteListIpEdit.text()))
        self.LiveLog.appendPlainText(text)

    def ApplyServiceFilterNow(self):
         #sudo iptables -A INPUT  -p tcp -m tcp --dport 22 -m state \ --state NEW -m recent --update --seconds 60 --hitcount 4 --name DEFAULT --rsource -j LOG --log-prefix='[netfilter] '
        service = self.SSHAndFTPOptions.currentIndex()

        try:
            port = int(self.SSHAndFTPPortEdit.text())
        except ValueError:
            self.LiveLog.appendPlainText("Please enter a valid port number \n")

        if service == 0:
            rule = "iptables -A INPUT -p tcp -m tcp --dport {port} -m state --state NEW -m recent --update --second {time} --hitcount {hits} --name DEFAULT --rsource -j LOG --log-prefix='[netfilter] '".format(port=int(self.GetFTPPort()), time=int(self.AttemptsDuration.text()), hits=int(self.AttemptsCount.text()))
            os.system(rule)
        elif service == 1:
            rule = "iptables -A INPUT -p tcp -m tcp --dport {port} -m state --state NEW -m recent --update --second {time} --hitcount {hits} --name DEFAULT --rsource -j LOG --log-prefix='[netfilter] '".format(port=int(self.GetSSHPort()), time=int(self.AttemptsDuration.text()), hits=int(self.AttemptsCount.text()))
            os.system(rule)

        if service == 0:
           text = "{time} Filtering packets to and from port {port} \n".format(time= datetime.datetime.now(), port=int(self.GetFTPPort()))
           self.LiveLog.appendPlainText(text)
        if service == 1:
           text = "Filtering packets to and from port {port} \n".format(time= datetime.datetime.now(), port=int(self.GetFTPPort()))
           self.LiveLog.appendPlainText(text)

    def BanCountries(self):
        countries = self.CountryListCombo.currentData()

        country_codes = []
        port = None

        try:
            port = int(self.BanOrUnbanPort.text())
        except ValueError:
            pass

        for country in countries:
            country_code = country.split(",")[1]
            if country_code.isupper():
                country_codes.append(country_code)
            if port:
                text = "{time} Banned country {country_code} from {port}\n".format(time = datetime.datetime.now(), country_code=country, port=port)
                self.LiveLog.appendPlainText(text)
            else:
                text = "{time} Banned country {country_code} at ALL ports \n".format(time = datetime.datetime.now(), country_code=country)
                self.LiveLog.appendPlainText(text)

        if len(country_codes) > 0:
            self.BanCountry(country_codes, port)

    def BanCountry(self, country_code, port=None):
        #iptables -A
        con = sqlite3.connect(self.appdir + "/database.db")
        cursor = con.cursor()
        print(country_code)
        for country in country_code:
            query = 'SELECT start_range, end_range FROM ipv4 WHERE country_code == "{code}"'.format(code=country)
            cursor.execute(query)
            ipv4rows = cursor.fetchall()
            for row in ipv4rows:
                if port:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -A INPUT -m iprange --src-range {start}-{end} --dport {port} -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])), port=port)
                        print(rule)
                        os.system(rule)
                    except ValueError:
                        continue
                else:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -A INPUT -m iprange --src-range {start}-{end} -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])))
                        print(rule)
                        os.system(rule)
                    except ValueError:
                        continue
        for country in country_code:
            query = 'SELECT start_range, end_range FROM ipv6 WHERE country_code == "{code}"'.format(code=country)
            cursor.execute(query)
            ipv6rows = cursor.fetchall()
            for row in ipv6rows:
                if port:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -A INPUT -m iprange --src-range {start}-{end} --dport -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])), port=port)
                        print(rule)
                        os.system(rule)
                    except ValueError:
                        continue
                else:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP --destination port 22
                        rule = 'iptables -A INPUT -m iprange --src-range {start}-{end} -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])))
                        print(rule)
                        os.system(rule)
                    except ValueError:
                        continue
    
    def UnBanCountries(self):
        countries = self.CountryListCombo.currentData()

        country_codes = []
        port = None

        try:
            port = int(self.BanOrUnbanPort.text())
        except ValueError:
            pass

        for country in countries:
            country_code = country.split(",")[1]
            country_codes.append(country_code)
            if port:
                text = "{time} UnBanned country {country_code} from {port}\n".format(time=datetime.datetime.now(), country_code=country, port=port)
                self.LiveLog.appendPlainText(text)
            else:
                text = "{time} UnBanned country {country_code} at ALL ports \n".format(time=datetime.datetime.now(), country_code=country)
                self.LiveLog.appendPlainText(text)

        if len(country_codes) > 0:
            self.UnBanCountry(country_codes, port)

    def UnBanCountry(self, country_code, port=None):
        #iptables -D
        con = sqlite3.connect(self.appdir + "/database.db")
        cursor = con.cursor()
        for country in country_code:
            query = 'SELECT start_range, end_range FROM ipv4 WHERE country_code == "{code}"'.format(code=country)
            cursor.execute(query)
            ipv4rows = cursor.fetchall()
            for row in ipv4rows:
                if port:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -D INPUT -m iprange --src-range {start}-{end} --destination-port {port} -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])), port=port)
                        os.system(rule)
                    except ValueError:
                        continue
                else:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -D INPUT -m iprange --src-range {start}-{end} --destination-port -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])))
                        os.system(rule)
                    except ValueError:
                        continue
        for country in country_code:
            query = 'SELECT start_range, end_range FROM ipv6 WHERE country_code == "{code}"'.format(code=country)
            cursor.execute(query)
            ipv6rows = cursor.fetchall()
            for row in ipv6rows:
                if port:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -D INPUT -m iprange --src-range {start}-{end} --destination-port -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])), port=port)
                        os.system(rule)
                    except ValueError:
                        continue
                else:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP --destination port 22
                        rule = 'iptables -D INPUT -m iprange --src-range {start}-{end} --destination-port {port} -j DROP'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])))
                        os.system(rule)
                    except ValueError:
                        continue

    def ExcludeCountries(self):
        countries = self.CountryListCombo.currentData()

        country_codes = []
        port = None

        try:
            port = int(self.BanOrUnbanPort.text())
        except ValueError:
            pass

        #make sure there actually are countries in the list
        if len(countries) > 0:
            #flush any existing rules
            os.system("iptables -F")
            os.system("iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT")
            os.system("iptables -A INPUT -p icmp -j ACCEPT")

        for country in countries:
            country_code = country.split(",")[1]
            if port:
                text = "{time} Rejecting all traffic except from {country_code} at {port}\n".format(time=datetime.datetime.now(), country_code=country, port=port)
                self.LiveLog.appendPlainText(text)
            else:
                text = "{time} Rejecting all traffic except from {country_code} at ALL ports \n".format(time=datetime.datetime.now(), country_code=country)
                self.LiveLog.appendPlainText(text)

            if country_code.isupper():
                country_codes.append(country_code)

        con = sqlite3.connect(self.appdir + "/database.db")
        cursor = con.cursor()


        for country_code in country_codes:
            query = 'SELECT start_range, end_range FROM ipv4 WHERE country_code == "{code}"'.format(code=country_code)
            print(query)
            cursor.execute(query)
            ipv4rows = cursor.fetchall()
            print(ipv4rows)
            print(country_code)
            for row in ipv4rows:
                if port:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -A INPUT -m iprange --src-range {start}-{end} --destination-port {port} -j ACCEPT'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])), port=port)
                        os.system(rule)
                    except ValueError:
                        continue
                else:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'iptables -A INPUT -m iprange --src-range {start}-{end} -j ACCEPT'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])))
                        os.system(rule)
                    except ValueError:
                        continue
        for country in country_code:
            query = 'SELECT start_range, end_range FROM ipv6 WHERE country_code == "{code}"'.format(code=country_code)
            cursor.execute(query)
            ipv6rows = cursor.fetchall()
            for row in ipv6rows:
                if port:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j DROP
                        rule = 'ip6tables -A INPUT -m iprange --src-range {start}-{end} -destination-port {port} -j ACCEPT'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])), port=port)
                        os.system(rule)
                    except ValueError:
                        continue
                else:
                    try:
                        #iptables -A INPUT -m iprange --src-range 2xx.3x.1xx.125-2xx.3x.1xx.225 -j ACCEPT --destination port 22
                        rule = 'ip6tables -A INPUT -m iprange --src-range {start}-{end} -j ACCEPT'.format(start=ipaddress.IPv4Address(int(row[0])), end=ipaddress.IPv4Address(int(row[1])))
                        os.system(rule)
                    except ValueError:
                        continue
        #Did we actually set any rules?
        if len(country_codes) > 0:
            os.system("iptables -A INPUT -i lo -j ACCEPT")
            os.system("iptables -A INPUT -j REJECT")

    def ChangeUsername(self):
        login = self.applogin(self.InputUserNameCurrent.text(), self.InputPasswordEdit.text())

        if login:
            conn = sqlite3.connect(self.appdir + "/database.db")
            cur = conn.cursor()
            statement = 'UPDATE login SET username "{new_username}" WHERE username = "{old_username}"'.format(new_username=self.InputUserNameCurrent.text(), old_username=self.InputUserNameCurrent.text())
            print(statement)
            cur.execute(statement)
            conn.commit()
            conn.close()


    def ChangePassword(self):
        username = self.InputUserNameEdit.text()
        old_password = self.InputOldPasswordEdit.text()
        new_password = self.InputNewPasswordEdit.text()

        login = self.applogin(username, old_password)

        if login:
            salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
            pwdhash = hashlib.pbkdf2_hmac('sha512', new_password.encode('utf-8'), 
                                salt, 100000)
            pwdhash = binascii.hexlify(pwdhash)
            pwdhash = (salt + pwdhash).decode('ascii')
            conn = sqlite3.connect(self.appdir + "./database.db")
            cursor = conn.cursor()
            query = 'UPDATE login SET password ="{pwdhash}" WHERE username ="{username}"'.format(pwdhash=pwdhash,username=username)
            cursor.execute(query)
            conn.commit()
            text = "Password for user {username} set to {new_password}".format(username=username, new_password=new_password)
            self.LiveLog.appendPlainText(text)

    def SaveEmailSettings(self):
        sender_email = self.SenderEmailEdit.text()
        sender_pass = self.SenderPasswordEdit.text()
        smtp_server = self.SMTPServerEdit.text()
        smtp_port = self.SMTPPortEdit.text()
        recipient_email = self.RecieverEmailEdit.text() 
        notifications_receive = self.EmailNotificationCheckBox.checkState()

        conn = sqlite3.connect(self.appdir +"/database.db")
        cursor = conn.cursor()
        check_email = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="email")
        cursor.execute(check_email)

        result = cursor.fetchall()

        if result:
           drop_existing = "DROP TABLE email"
           cursor.execute(drop_existing)

        create_new = "CREATE TABLE email(sender_email, sender_pass, smtp_server, smtp_port, recipient_email, notifications_receive)"
        cursor.execute(create_new)

        save_values = 'INSERT INTO email(sender_email, sender_pass, smtp_server, smtp_port, recipient_email, notifications_receive) VALUES ("{sender_email}", "{sender_pass}", "{smtp_server}", "{smtp_port}", "{recipient_email}", "{notifications_receive}")'.format(sender_email=sender_email, sender_pass=sender_pass, smtp_server=smtp_server, smtp_port=smtp_port, recipient_email=recipient_email, notifications_receive=notifications_receive)

        cursor.execute(save_values)

        conn.commit()

        text = "{time} Updated email databased to the indicated values".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

        conn.close()

    def apt_install(self, pkgs):
        cmd = ['pkexec', 'apt-get', 'install', '-y'] + pkgs
        print('Running command: {}'.format(' '.join(cmd)))
        result = run(
                cmd,
                stdout=sys.stdout,
                stderr=sys.stderr,
                encoding='utf8',
                env={**os.environ, 'DEBIAN_FRONTEND': 'noninteractive'}
                )
        result.check_returncode()

    def accept_eula(self):
        cmd = 'echo msttcorefonts msttcorefonts/{}-mscorefonts-eula {} | pkexec debconf-set-selections'
        run(cmd.format("present", "note ''"), stdout=sys.stdout, stderr=sys.stderr, shell=True)
        run(cmd.format("accepted", "select true"), stdout=sys.stdout, stderr=sys.stderr, shell=True)

    def UpdatePackage(self, package):
        # testing with configured licenses, one simple and one complicated package

        locked = self.IsLocked(package)

        if locked:
            text = "{time} Attempted to update a locked package : {package} \n".format(time=datetime.datetime.now(), package=package)
            self.LiveLog.appendPlainText()
            return
        self.accept_eula()
        self.apt_install([package])

    def UpdateSelectedPackages(self):
        selected = self.PossibleUpdates.selectionModel()

        status = selected.hasSelection()

        model = self.PossibleUpdates.model()

        if status:
            selection = selected.selectedIndexes()
            for item in selection:
                self.UpdatePackage(item.data())
                text = "{time} updated package {package}".format(time=datetime.datetime.now(), package=item.data())


    def UpdateResourcesTab(self):
        import psutil

        self.CPULoadValues.append(psutil.cpu_percent())
        self.VirtualMemoryValues.append(psutil.virtual_memory()[2])

        if len(self.CPULoadValues) > len(self.PlotAgainstValues):
            del self.CPULoadValues[0]

        self.CPULoadGraph.clear()
        self.CPULoadGraph.plot(self.PlotAgainstValues[:len(self.CPULoadValues)], self.CPULoadValues)

        if len(self.VirtualMemoryValues) > len(self.PlotAgainstValues):
            del self.VirtualMemoryValues[0]

        self.VirtualMemoryUsage.clear()
        self.VirtualMemoryUsage.plot(self.PlotAgainstValues[:len(self.VirtualMemoryValues)], self.VirtualMemoryValues)

    def getDiskSpace(self):
        os.system('df -h | grep /$ > abs_path.txt')

        usage = None

        with open("abs_path.txt", "r") as f:
            line = f.readline()
            words = line.split(" ")
            usage = words[len(words) - 2]
        
        self.DiskUsagePercentage.setText(usage)


    def getSSHAction(self):

        status = self.GetSSHStatus()

        if "Enabled" in status:
            return "Disable"
        else:
            return "Enable"

    def getFTPAction(self):

        status = self.GetFTPStatus()

        if "Enabled" in status:
            return "Disable"
        else:
            return "Enable"

    def ImportConfigFiles(self):
        filedialog = QFileDialog()
        filedialog.setFileMode(QFileDialog.DirectoryOnly)
        directory = filedialog.getExistingDirectory()

        #restore iptables save

        self.FactoryResetAction()

        iptables_restore = "iptables-restore <"+ directory + "/iptables.save"
        os.system(iptables_restore)

        con = sqlite3.connect(self.appdir +"/database.db")

        cur = con.cursor()

        cur.execute("CREATE TABLE users(username, password)")
        cur.execute("CREATE TABLE locked(package)")
        create_new = "CREATE TABLE email(sender_email, sender_pass, smtp_server, smtp_port, recipient_email, notifications_receive)"
        cur.execute(create_new)

        print(directory)

        if os.path.exists(directory + "/users.csv"):
            with open(directory +"/users.csv") as fin:
                dr = csv.DictReader(fin)
                to_db = [(i['username'],i['password']) for i in dr]
                cur.executemany("INSERT INTO users (username, password) VALUES(?,?)", to_db)
                con.commit()

        if os.path.exists(directory + "/locked.csv"):
            with open(directory +"/locked.csv") as fin:
                dr = csv.DictReader(fin)
                to_db = [(i['package']) for i in dr]
                cur.executemany("INSERT INTO locked (package) VALUES(?)", to_db)
                con.commit()

        if os.path.exists(directory + "/email.csv"):
            with open(directory +"/email.csv") as fin:
                dr = csv.DictReader(fin)
                to_db = [(i['sender_email'],i['sender_pass'], i['smtp_server'], i['smtp_port'], i['recipient_email'], i['notifications_receive']) for i in dr]
                cur.executemany("INSERT INTO email (sender_email, sender_pass, smtp_server, smtp_port, recipient_email, notifications_receive) VALUES(?,?,?,?,?,?)", to_db)
                con.commit()

        text = "{time} Imported Configuration \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def ExportConfigFiles(self):
        filedialog = QFileDialog()
        filedialog.setFileMode(QFileDialog.DirectoryOnly);
        directory = filedialog.getExistingDirectory()

        iptables_save = "iptables-save >"+ directory +"/iptables.save"
        os.system(iptables_save)

        conn = sqlite3.connect(self.appdir+"/database.db", isolation_level=None,
                       detect_types=sqlite3.PARSE_COLNAMES)

        cursor = conn.cursor()

        check_locked = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="locked")
        cursor.execute(check_locked)

        result = cursor.fetchall()

        if result:
            db_df = pd.read_sql_query("SELECT * FROM locked", conn)
            filename = directory + "/locked.csv"
            db_df.to_csv(filename, index=False)

        check_email = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="email")
        cursor.execute(check_email)

        result = cursor.fetchall()

        if result:
            filename = directory + "/email.csv"
            db_df = pd.read_sql_query("SELECT * FROM email", conn)
            db_df.to_csv(filename, index=False)

        check_users = "SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'".format(table_name="users")
        cursor.execute(check_users)

        result = cursor.fetchall()

        if result:
            filename = directory + "/users.csv"
            db_df = pd.read_sql_query("SELECT * FROM users", conn)
            db_df.to_csv(filename, index=False)

        text = "{time} Exported Configuration \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def SendEmail(self):
        with open("/var/log/iptables.log", "r") as f:
            line = f.readline()

        #nothing has been logged so far so good
        if not line:
            return

        os.truncate("/var/log/iptables.log")

        sqlite3.connect(self.appdir +"/database.db")
        con = sqlite3.connect(self.appdir + "/database.db")
        cursor = con.cursor()
        query = "SELECT * FROM email"
        cursor.execute(query)
        email_variables = cursor.fetchall()

        sender_email =  email_variables[0][0]
        sender_password = email_variables[0][1]
        smtp_server =  email_variables[0][2]
        port = email_variables[0][3]
        receiver_email = email_variables[0][4]
        message = """
                  
                  It looks like there was a brute force attempt on the Computer/Server.
                  
                  The exactly log in the iptables files is as follows.

                  {line}
                  """.format(line=line)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        text = "{time} Sent out an email after a failed brute force attempt \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def UpdatesDefault(self):
        default_config = 'APT::Periodic::Update-Package-Lists "1"; \nAPT::Periodic::Unattended-Upgrade "1";'
        with open("/etc/apt/apt.conf.d/20auto-upgrades", "w+") as f:
            f.write(default_config)
        text = "Set updates setting to default\n"
        self.LiveLog.appendPlainText(text)

    def UpdateActionText(self):
        status = self.CheckUpdatesStatus()

        if status:
            return "Enable"
        else:
            return "Disable"

    def CheckUpdatesStatus(self):
        value = int()
        with open("/etc/apt/apt.conf.d/20auto-upgrades") as f:
            line = f.readline()
            print(line)
            value = str(line.split(" ")[1][1])
            return value

    def EnableUpdates(self):
        file_path = "/etc/apt/apt.conf.d/20auto-upgrades"
        substitute = 'APT::Periodic::Update-Package-Lists "1";'
        pattern = 'APT::Periodic::Update-Package-Lists "0";'

        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(pattern, substitute))
        copymode(file_path, abs_path)
        remove(file_path)
        move(abs_path, file_path)
        text = "{time} Enabled automatic updates \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def DisableUpdates(self):
        file_path = "/etc/apt/apt.conf.d/20auto-upgrades"
        substitute = 'APT::Periodic::Update-Package-Lists "0";'
        pattern = 'APT::Periodic::Update-Package-Lists "1";'

        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    new_file.write(line.replace(pattern, substitute))
        copymode(file_path, abs_path)
        remove(file_path)
        move(abs_path, file_path)
        text = "{time} Disabled automatic updates \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def GeneratePassword(self):
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))

        self.InputNewPasswordEdit.setText(password)

        self.InputNewPasswordEdit.setEchoMode(QLineEdit.Normal)

    def GetShellAccessAction(self):
        os.system("echo $SHELL > file.txt")
        
        with open("file.txt") as f:
            line = f.readline()
            os.remove("file.txt")

            if "bash" in line:
                return "Disable Shell Access"
            else:
                return "Enable Shell Access"

    def ShellAccessAction(self):
        status = self.GetShellAccessAction()

        if "Enable" in status:
            self.EnableShellAccess("root")
            self.DisableShellAccessButton.setText("Disable")
        else:
            self.DisableShellAccess("root")
            self.DisableShellAccessButton.setText("Enable")

    def DisableShellAccess(self, username):
        test = subprocess.Popen(["usermod","-s","/sbin/nologin", username], stdout=subprocess.PIPE)
        output = test.communicate()[0]
        text = "{time} Disabled shell access for user {username} \n".format(time=datetime.datetime.now(), username=username)
        self.LiveLog.appendPlainText(text)

    def EnableShellAccess(self, username):
        test = subprocess.Popen(["usermod","-s","/bin/bash", username], stdout=subprocess.PIPE)
        output = test.communicate()[0]
        text = "{time} Enabled shell access for user {username} \n".format(time=datetime.datetime.now(), username=username)
        self.LiveLog.appendPlainText(text)

    def GetSSHStatus(self):
        status = os.system('service ssh status > abs_path.txt')

        if status == 0:
            result = "Running"
        else:
            result = "Down"
        with open("abs_path.txt", 'r') as output:
            for line in output:
                if 'enabled;' in line:
                    result += "/Enabled"
                    break
        os.remove("abs_path.txt")
        if "/" in result:
            return result
        else:
            return result + "/Disabled"

    def GetFTPStatus(self):
        status = os.system('service vsftpd status > abs_path.txt')

        if status == 0:
            result = "Running"
        else:
            result = "Down"
        with open("abs_path.txt", 'r') as output:
            for line in output:
                if 'enabled;' in line:
                    result += "/Enabled"
                    break
        os.remove("abs_path.txt")
        if "/" in result:
            return result
        else:
            return result + "/Disabled"

    def GetFTPPort(self):
        config_file = "/etc/vsftpd.conf"
        search_string = "listen_port"
        with open(config_file, 'r') as read_obj:
            for line in read_obj:
                if search_string in line:
                    words = line.split('=')
                    return int(words[-1])
        return 21

    def GetSSHPort(self):
        config_file = "/etc/ssh/sshd_config"
        search_string = "Port"
        with open(config_file, 'r') as read_obj:
            for line in read_obj:
                if search_string in line:
                    words = line.split(' ')
                    port = int(words[-1])
                    return port

    def SetSSHPort(self, port, current_port):
        pattern = "Port "+ str(current_port)
        substr = "Port "+ str(port) + "\n"
        file_path = "/etc/ssh/sshd_config"
        fh, abs_path = mkstemp()
        with fdopen(fh, "w") as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                    if pattern in line:
                        new_file.write(substr)
                    else:
                        new_file.write(line)
        copymode(file_path, abs_path)
        remove(file_path)
        move(abs_path, file_path)

        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        job = manager.RestartUnit('ssh.service', 'fail')
        self.OverviewSSHPort.setText(str(port))
        text = "{time} Set SSH port to {port} with systemd \n".format(time=datetime.datetime.now(), port=port)
        self.LiveLog.appendPlainText(text)

    def SetFTPPort(self, port):
        current_port = self.GetFTPPort()
        pattern = "listen_port=" + str(current_port)
        substr = "listen_port=" + str(port)
        file_path = "/etc/vsftpd.conf"
        fh, abs_path = mkstemp()
        found = False

        if current_port == 21:
            with fdopen(fh, "w") as new_file:
                with open(file_path) as old_file:
                    for line in old_file:
                        if pattern in line:
                            new_file.write(line.replace(pattern, substr))
                            found = True
                        else:
                            new_file.write(line)
                    if not found:
                        new_file.write(substr)
            copymode(file_path, abs_path)
            remove(file_path)
            move(abs_path, file_path)
        else:
            pattern = "listen_port="+str(port)
            with open(file_path, "a+") as old_file:
                old_file.write(pattern)

        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        job = manager.RestartUnit('vsftp.service', 'fail')
        self.OverviewFTPPort.setText(str(port))
        text = "{time} Set FTP port to {port} with systemd \n".format(time=datetime.datetime.now(), port=port)
        self.LiveLog.appendPlainText(text)

    def SSHAction(self):
        status = self.OverviewSSHStatus.text()

        if  "Enabled" in status:
            self.DisableSSH()
            if "Running" in status:
                self.OverviewSSHStatus.setText("Disabled/Running")
            else:
                self.OverviewSSHStatus.setText("Disabled/Down")

            self.OverviewSSHAction.setText("Enable")
        else:
            self.EnableSSH()
            if "Running" in status:
                self.OverviewSSHStatus.setText("Enabled/Running")
            else:
                self.OverviewSSHStatus.setText("Enabled/Down")
            self.OverviewSSHAction.setText("Disable")

    def DisableSSH(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        manager.DisableUnitFiles(['ssh.service'], False)
        manager.Reload()
        #job = manager.RestartUnit('ssh.service', 'fail')
        text = "{time} Disabled SSH with systemd \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def EnableSSH(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        manager.EnableUnitFiles(['ssh.service'], False, True)
        manager.Reload()
        job = manager.RestartUnit('ssh.service', 'fail')
        text = "{time} Enabled SSH with systemd \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def FTPAction(self):
        status = self.OverviewFTPStatus.text()

        if  "Enabled" in status:
            self.DisableFTP()
            if "Running" in status:
                self.OverviewFTPStatus.setText("Disabled/Running")
            else:
                self.OverviewFTPStatus.setText("Disabled/Down")

            self.OverviewFTPAction.setText("Enable")
        else:
            self.EnableFTP()
            if "Running" in status:
                self.OverviewFTPStatus.setText("Enabled/Running")
            else:
                self.OverviewFTPStatus.setText("Enabled/Down")
            self.OverviewFTPAction.setText("Disable")

    def DisableFTP(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        manager.DisableUnitFiles(['vsftpd.service'], False)
        manager.Reload()
        #job = manager.RestartUnit('ssh.service', 'fail')
        text = "{time} Disabled FTP with systemd \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def EnableFTP(self):
        sysbus = dbus.SystemBus()
        systemd1 = sysbus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
        manager = dbus.Interface(systemd1, 'org.freedesktop.systemd1.Manager')
        manager.EnableUnitFiles(['vsftpd.service'], False, True)
        manager.Reload()
        job = manager.RestartUnit('vsftpd.service', 'fail')
        text = "{time} Enabled FTP with systemd \n".format(time=datetime.datetime.now())
        self.LiveLog.appendPlainText(text)

    def WhoisIP(self):
        ip_address = self.WhoisIpEdit.text()
        url = "https://ipinfo.io/"
        url = url + ip_address
        req = Request(url)
        req.add_header('Accept', 'application/json')
        req_results = json.loads(urlopen(req).read())

        if req_results['country']:
            self.CountryFrom.setText(req_results['country'])
        else:
            self.CountryFrom.setText("null")

        if req_results['city']:
            self.CityFrom.setText(req_results['city'])
        else:
            self.CountryFrom.setText("null")
        
        if req_results['timezone']:
            self.TimezoneFrom.setText(req_results['timezone'])
        else:
            self.CountryFrom.setText("null")

        if req_results['hostname']:
            self.IpHostName.setText(req_results['hostname'])
        else:
            self.CountryFrom.setText("null")

        text = "{time} Performed IP lookup from ipinfo.io for IP ".format(time=datetime.datetime.now()) + self.WhoisIpEdit.text() + "\n"
        self.LiveLog.appendPlainText(text)

    def ApplySSHAndFTPChanges(self):
        service = self.SSHAndFTPOptions.currentIndex()

        try:
            port = int(self.SSHAndFTPPortEdit.text())
        except ValueError:
            self.LiveLog.appendPlainText("Please enter a valid port number \n")

        if service == 0:
            print(int(self.SSHAndFTPPortEdit.text()))
            self.SetSSHPort(int(self.SSHAndFTPPortEdit.text()), self.GetSSHPort())
            text = "Set SSH port to " + self.SSHAndFTPPortEdit.text() + "\n"
            self.LiveLog.appendPlainText(text)
        elif service == 1:
            self.SetFTPPort(int(self.SSHAndFTPPortEdit.text()))
            text = "Set FTPd port to " + self.SSHAndFTPPortEdit.text() + "\n"
            self.LiveLog.appendPlainText(text)


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

if __name__ == "__main__":
    variables = GetVariables()

    root = is_root()
    if not root:
        os.system("xhost +")

    elevate.elevate()

    if root:
        os.environ["DISPLAY"] = ":0"

    app = QApplication(sys.argv)

    mainWindow = LinuxTool(variables[0])
    #mainWindow.SetupUI()
    mainWindow.show()

    sys.exit(app.exec_())
