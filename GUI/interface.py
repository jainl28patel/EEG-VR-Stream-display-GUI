# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color : rgb(48,48,48)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.workload = AnalogGaugeWidget(self.centralwidget)
        self.workload.setGeometry(QtCore.QRect(30, 110, 281, 241))
        self.workload.setObjectName("workload")
        self.situation_awareness = AnalogGaugeWidget(self.centralwidget)
        self.situation_awareness.setGeometry(QtCore.QRect(489, 110, 281, 241))
        self.situation_awareness.setObjectName("situation_awareness")
        self.attention = AnalogGaugeWidget(self.centralwidget)
        self.attention.setGeometry(QtCore.QRect(20, 410, 161, 131))
        self.attention.setObjectName("attention")
        self.engagement = AnalogGaugeWidget(self.centralwidget)
        self.engagement.setGeometry(QtCore.QRect(230, 410, 151, 131))
        self.engagement.setObjectName("engagement")
        self.fatigue = AnalogGaugeWidget(self.centralwidget)
        self.fatigue.setGeometry(QtCore.QRect(420, 410, 151, 131))
        self.fatigue.setObjectName("fatigue")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(219, 30, 415, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color : white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 360, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color : white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(540, 370, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color : white;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 550, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color : white;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 550, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color : white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(470, 550, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color : white;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(670, 550, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color : white;")
        self.label_7.setObjectName("label_7")
        self.stress = AnalogGaugeWidget(self.centralwidget)
        self.stress.setGeometry(QtCore.QRect(620, 410, 141, 131))
        self.stress.setObjectName("stress")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Activity Monitoring Panel"))
        self.label_2.setText(_translate("MainWindow", "Workload"))
        self.label_3.setText(_translate("MainWindow", "Situation Awareness"))
        self.label_4.setText(_translate("MainWindow", "Attention"))
        self.label_5.setText(_translate("MainWindow", "Engagement"))
        self.label_6.setText(_translate("MainWindow", "Fatigue"))
        self.label_7.setText(_translate("MainWindow", "Stress"))
from AnalogGaugeWidget import AnalogGaugeWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
