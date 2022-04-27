import os
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget , QApplication
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import QTimer
from sympy import false, true
from interface import *
import random
import threading
import time

#os.system("pyuic5 -o interface.py interface.ui")

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        ################################################################################################
        # to display green-yellow-red bar as per the position of arrow
        ################################################################################################
        self.ui.workload.enableBarGraph = false
        self.ui.attention.enableBarGraph = False
        self.ui.situation_awareness.enableBarGraph = False
        self.ui.engagement.enableBarGraph = False
        self.ui.fatigue.enableBarGraph = False
        self.ui.stress.enableBarGraph = False

        # self.ui.workload.use_timer_event = True
        # self.ui.attention.use_timer_event = True
        # self.ui.situation_awareness.use_timer_event = True
        # self.ui.engagement.use_timer_event = True
        # self.ui.fatigue.use_timer_event = True
        # self.ui.stress.use_timer_event = True
        # for i in range(1, 100, 10):
        #     self.ui.workload.updateValue(i)
        
        self.timer = QTimer()  
        self.timer.timeout.connect(lambda: self.movement())  
        self.timer.start(1000)  


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
        self.ui.workload.updateValue(random.randint(20,60))
        self.ui.attention.updateValue(random.randint(50,80))
        self.ui.situation_awareness.updateValue(random.randint(40,60))
        self.ui.engagement.updateValue(random.randint(60,90))
        self.ui.fatigue.updateValue(random.randint(10,30))
        self.ui.stress.updateValue(random.randint(20,40))
    


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())