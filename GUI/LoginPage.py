################################################################################################
# Imports
################################################################################################
from PyQt5 import QtCore, QtGui, QtWidgets
from Stream import Ui_MainWindow2

################################################################################################
# Main class
################################################################################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        ################################################################################################
        # background and screen size
        ################################################################################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color : rgb(48, 48, 48)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ################################################################################################
        # IITR Icon
        ################################################################################################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 161))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("iitricon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        ################################################################################################
        # DRDO Icon
        ################################################################################################
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(619, 20, 171, 171))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("drdoLogo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        ################################################################################################
        # Main heading
        ################################################################################################
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 420, 140))
        font = QtGui.QFont()
        font.setFamily(".New York")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color : white;")

        ################################################################################################
        # User Image
        ################################################################################################
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 160, 111, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")

        ################################################################################################
        # Log on text
        ################################################################################################
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 280, 120, 41))
        self.label_5.setStyleSheet("color : white;")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

        ################################################################################################
        # Line edit to take input of User ID
        ################################################################################################
        self.UserID = QtWidgets.QLineEdit(self.centralwidget)
        self.UserID.setGeometry(QtCore.QRect(310, 350, 171, 31))
        self.UserID.setStyleSheet("border : 1px solid white;")
        self.UserID.setObjectName("UserID")
        self.UserID.setStyleSheet("color : white")

        ################################################################################################
        # Line Edit to take input of Password in masked format
        ################################################################################################
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(310, 410, 171, 31))
        self.Password.setStyleSheet("border : 1px solid white;")
        self.Password.setObjectName("Password")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setStyleSheet("color :white")

        ################################################################################################
        # label_6 and label_7 to set text of UserId and Password
        ################################################################################################
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(310, 330, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("color : white;")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 390, 60, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color : white;")

        ################################################################################################
        # Pushbutton for logon
        ################################################################################################
        self.LogON = QtWidgets.QPushButton(self.centralwidget)
        self.LogON.setGeometry(QtCore.QRect(330, 470, 131, 41))

        ################################################################################################
        # warning label incase of invalid username or password
        ################################################################################################
        self.warning = QtWidgets.QLabel(self.centralwidget)
        self.warning.setGeometry(QtCore.QRect(310, 450, 60, 16))
        self.warning.setObjectName("warning")
        self.warning.setStyleSheet("color : white;")
        self.warning.resize(200, 10)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.LogON.setFont(font)
        self.LogON.setStyleSheet("background-color : rgb(83, 79, 226) ;\n"
"color : white")
        self.LogON.setObjectName("LogON")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################################################################################################
        # Onclick listner for Logon button
        ################################################################################################
        self.LogON.clicked.connect(self.gotoWindow2)

################################################################################################
# Function to check for password and UserId and opening new window if valid
################################################################################################
    def gotoWindow2(self):
        if (self.UserID.text() == "" or self.Password.text() == ""):
            self.warning.setText("Enter valid UserId & Password")
        else :
            self.MainWindow2 = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow2()
            self.ui.setupUi(self.MainWindow2)
            self.MainWindow2.show()
            self.ui.UserName.setText(self.UserID.text())
            MainWindow.close()

    ################################################################################################
    # function to set text of the labels
    ################################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Human Machine Collaboration \nOperator Monitoring System"))
        self.label_5.setText(_translate("MainWindow", "Log on"))
        self.label_6.setText(_translate("MainWindow", "User ID"))
        self.label_7.setText(_translate("MainWindow", "Password"))
        self.LogON.setText(_translate("MainWindow", "Log on"))
        self.warning.setText(_translate("MainWindow", ""))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
