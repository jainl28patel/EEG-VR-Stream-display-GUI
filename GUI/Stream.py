
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.pyplot import text
from main import MainWindow
from PyQt5.QtWidgets import QApplication
import sys

from pylsl import StreamInfo, StreamInlet, resolve_stream

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        ################################################################################################
        # Setting main window
        ################################################################################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 644)
        MainWindow.setStyleSheet("background-color : rgb(48,48,48)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ################################################################################################
        # labels to set the text displayed on the screen
        ################################################################################################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 831, 131))
        self.label.setStyleSheet("background-color: rgb(80, 71, 225);\n"
"border-radius : 10px;\n"
"width : 100%")
        self.label.setText("")
        self.label.setObjectName("label")

        ################################################################################################
        # User Image
        ################################################################################################
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 121))
        self.label_2.setStyleSheet("background-color : rgb(80, 71, 225)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("user.png"))
        self.label_2.setObjectName("label_2")

        ################################################################################################
        # welcome message
        ################################################################################################
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 150, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color : white;\n"
"background-color :rgb(80, 71, 225)")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

        ################################################################################################
        # displaying the username
        ################################################################################################
        self.UserName = QtWidgets.QLabel(self.centralwidget)
        self.UserName.setGeometry(QtCore.QRect(120, 60, 250, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.UserName.setFont(font)
        self.UserName.setStyleSheet("color : white;\n"
"background-color :rgb(80, 71, 225)")
        self.UserName.setObjectName("UserName")

        ################################################################################################
        # Search for stream label
        ################################################################################################
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 160, 350, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("color : white;")

        ################################################################################################
        # EEG pushbutton
        ################################################################################################
        self.EEG_button = QtWidgets.QPushButton(self.centralwidget)
        self.EEG_button.setGeometry(QtCore.QRect(100, 240, 191, 61))
        self.EEG_button.setStyleSheet("background-color: rgb(32, 20, 231);\n"
"border : 1px solid balck;\n"
"border-radius : 10px;\n"
"color : white;")
        self.EEG_button.setObjectName("EEG_button")

        ################################################################################################
        # VR Pushbutton
        ################################################################################################
        self.VR_button = QtWidgets.QPushButton(self.centralwidget)
        self.VR_button.setGeometry(QtCore.QRect(100, 320, 191, 61))
        self.VR_button.setStyleSheet("background-color: rgb(39, 0, 232);\n"
"border : 1px solid black;\n"
"border-radius : 10px;\n"
"color : white\n"
"")
        self.VR_button.setObjectName("VR_button")

        ################################################################################################
        # Red / Green status displayer of EEG and VR
        ################################################################################################
        self.EEG_status = QtWidgets.QLabel(self.centralwidget)
        self.EEG_status.setGeometry(QtCore.QRect(320, 260, 21, 21))
        self.EEG_status.setStyleSheet("background-color :red;\n"
"border : 1px solid black;\n"
"border-radius : 10px;")
        self.EEG_status.setText("")
        self.EEG_status.setObjectName("EEG_status")
        self.VR_status = QtWidgets.QLabel(self.centralwidget)
        self.VR_status.setGeometry(QtCore.QRect(320, 340, 21, 20))
        self.VR_status.setStyleSheet("background-color: red;\n"
"border : 1px solid black;\n"
"border-radius : 10px;")
        self.VR_status.setText("")
        self.VR_status.setObjectName("VR_status")

        self.EEG_followup_text = QtWidgets.QLabel(self.centralwidget)
        self.EEG_followup_text.setGeometry(QtCore.QRect(360, 240, 900, 50))
        self.EEG_followup_text.setObjectName("EEG_followup_text")
        self.EEG_followup_text.setStyleSheet("color : white;")

        self.VR_followup_text = QtWidgets.QLabel(self.centralwidget)
        self.VR_followup_text.setGeometry(QtCore.QRect(360, 320, 900, 50))
        self.VR_followup_text.setObjectName("VR_followup_text")
        self.VR_followup_text.setStyleSheet("color : white;")
        self.VR_followup_text.setWordWrap(False)
        ################################################################################################
        # Next page Button
        ################################################################################################
        self.Next_button = QtWidgets.QPushButton(self.centralwidget)
        self.Next_button.setGeometry(QtCore.QRect(350, 450, 101, 41))
        self.Next_button.setStyleSheet("border-radius :10px;\n"
"background-color : rgb(186, 45, 68);\n"
"color : white")
        self.Next_button.setObjectName("Next_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################################################################################################
        # Event listner for EEG button
        ################################################################################################
        self.EEG_button.clicked.connect(self.eegLSLDetect)

        ################################################################################################
        # Event listner for VR button
        ################################################################################################
        self.VR_button.clicked.connect(self.vrLSLDetect)

        ################################################################################################
        # Event listner for Next page button
        ################################################################################################
        self.Next_button.clicked.connect(self.nextpage)

    ################################################################################################
    # Function to open Next page
    ################################################################################################
    def nextpage(self):
        self.app = QApplication(sys.argv)
        self.window = MainWindow()
        self.window.show()

    ################################################################################################
    # Function to detect signal for EEG stream
    ################################################################################################
    def greensignalEEG(self):
        self.EEG_status.setStyleSheet("background-color :green;\n"
                                      "border : 1px solid black;\n"
                                      "border-radius : 10px;")

    ################################################################################################
    # Function to detect lsl stream for EEG stream
    ################################################################################################
    textEEG = ""
    def eegLSLDetect(self):
        _translate = QtCore.QCoreApplication.translate
        results = resolve_stream("type", "EEG")
        if len(results) > 0:
                inlet = StreamInlet(results[0])
                info = inlet.info()
                self.textEEG = "Name: " + info.name() + "\t" + "Channel Count: " + str(info.channel_count()) + "\t" + "Sapmpling Rate: " + str(info.nominal_srate())  
                self.greensignalEEG()
        else:
                self.textEEG = "EEG Not Detected"
        self.EEG_followup_text.setText((_translate("MainWindow", self.textEEG)))
        
    ################################################################################################
    # Function to detect lsl stream for VR stream
    ################################################################################################
    textVR = ""
    def vrLSLDetect(self):
        _translate = QtCore.QCoreApplication.translate
        results = resolve_stream("type", "Stimuli_Trigger")
        if len(results) > 0:
                inlet = StreamInlet(results[0])
                info = inlet.info()
                self.textVR = "Name: " + info.name()
                self.greensignalVR()
        else:
                self.textVR = "VR Not Detected"
        self.VR_followup_text.setText((_translate("MainWindow", self.textVR)))

    ################################################################################################
    # Fuction to detect signal for VR stream
    ################################################################################################
    def greensignalVR(self):
        self.VR_status.setStyleSheet("background-color :green;\n"
                                      "border : 1px solid black;\n"
                                      "border-radius : 10px;")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Welcome"))
        self.UserName.setText(_translate("MainWindow", "Name aayega isme "))
        self.label_5.setText(_translate("MainWindow", "Search for Streams"))
        self.EEG_button.setText(_translate("MainWindow", "Connect to EEG"))
        self.VR_button.setText(_translate("MainWindow", "Connect to VR"))
        self.Next_button.setText(_translate("MainWindow", "Next"))
        self.EEG_followup_text.setText((_translate("MainWindow", self.textEEG)))
        self.VR_followup_text.setText((_translate("MainWindow", self.textVR)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
