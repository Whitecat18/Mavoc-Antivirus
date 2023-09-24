from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, QTime
import sys


class DateTimeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        layout = QVBoxLayout()
        
        # Create a label to display the date and time
        self.datetime_label = QLabel(self)
        layout.addWidget(self.datetime_label)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000) 
        self.setLayout(layout)

        self.updateDateTime()

    def updateDateTime(self):

        current_datetime = QTime.currentTime().toString("Sync : hh:mm:ss")
        
        self.datetime_label.setText(current_datetime)