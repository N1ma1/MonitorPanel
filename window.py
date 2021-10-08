
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow, QPushButton
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
        self.design_layout()
        self.monitor_list = QListWidget(self)
        self.monitor_list.setGeometry(150,20,200,80)
        self.m_list()

    def m_list(self):
        st = os.popen('xrandr --listmonitors')
        output = st.read()
        i = 0
        for monitor in output.split('\n'):
            if(monitor.startswith("Monitors:") or monitor == ""):
                continue
            self.monitor_list.insertItem(i,monitor.split('/')[0])
            i += 1

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
            painter[i].setPen(QPen(Qt.black, 2.5))
            painter[i].drawText(QPoint(l + 15, (h/6) + t), str(h)+"px")
            painter[i].drawText(QPoint((w/6)+l, t + 15), str(w)+"px")

            painter[i].drawRect(l, t, w/3, h/3)
            i += 1
            l += (w/3) + 5
        if l > 680 :
            # we need a Vertical scrool bar
            pass
    
    def design_layout(self):
        move_monitor_right = QPushButton("move monitor right",self)
        move_monitor_right.setGeometry(20,20,100,20)
        move_monitor_right.setFont(QtGui.QFont("Arial", 8))
        # move_monitor_right.clicked.connect(self.move_monitor_right)

        move_monitor_left = QPushButton("move monitor left",self)
        move_monitor_left.setGeometry(20,45,100,20)
        move_monitor_left.setFont(QtGui.QFont("Arial", 8))
        # move_monitor_left.clicked.connect(self.move_monitor_left)

