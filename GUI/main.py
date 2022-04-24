import os
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget , QApplication
from PyQt5.QtGui import QFont, QFontDatabase
from interface import *
import random
import threading
import time

os.system("pyuic5 -o interface.py interface.ui")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        ################################################################################################
        # to display green-yellow-red bar as per the position of arrow
        ################################################################################################
        self.ui.workload.enableBarGraph = False
        self.ui.attention.enableBarGraph = False
        self.ui.situation_awareness.enableBarGraph = False
        self.ui.engagement.enableBarGraph = False
        self.ui.fatigue.enableBarGraph = False
        self.ui.stress.enableBarGraph = False


        ################################################################################################
        # Setting the theme for Analog meter
        ################################################################################################
        self.ui.workload.setGaugeTheme(2)
        self.ui.attention.setGaugeTheme(2)
        self.ui.situation_awareness.setGaugeTheme(2)
        self.ui.engagement.setGaugeTheme(2)
        self.ui.fatigue.setGaugeTheme(2)
        self.ui.stress.setGaugeTheme(2)



    def movement(self):
        i = 0
        while i < 1000:
            self.ui.workload.value = i
            i += 100
            time.sleep(1)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())