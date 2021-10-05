
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import QPoint, Qt
import os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Drawing Rectangle"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500


        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


    def paintEvent(self, e):
        st = os.popen("xrandr --listmonitors")
        output = st.read()
        painter = []
        i = 0
        t = 350
        l = 20
        for monitor in output.split('\n'):
            if(monitor.startswith("Monitors:") or monitor == ""):
                continue
            monitor_size = monitor.split('/')[1]
            h = int(monitor_size.split('x')[0])
            w = int(monitor_size.split('x')[1])
            painter.append(QPainter(self))
            painter[i].setPen(QPen(Qt.black, 5))
            # painter[i].setBrush(QBrush(Qt.red, Qt.SolidPattern))
            # painter[i].setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))
            painter[i].drawText(QPoint(l + 15,(h/6)+ t),str(h)+"px")
            painter[i].drawText(QPoint((w/6)+l,t + 15),str(w)+"px")

            painter[i].drawRect(l, t, w/3,h/3)
            i += 1
            l += w/3
            
