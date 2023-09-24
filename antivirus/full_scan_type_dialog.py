from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

class FullScanTypeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Scanning Method...")
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)

        layout = QVBoxLayout()

        self.full_scan_radio = QRadioButton("Full Scan")
        self.partition_scan_radio = QRadioButton("Partition Scan")

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.full_scan_radio)
        radio_layout.addWidget(self.partition_scan_radio)

        layout.addLayout(radio_layout)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def full_scan_selected_option(self):
        if self.full_scan_radio.isChecked():
            return "full_scan"
        elif self.partition_scan_radio.isChecked():
            return "partition_scan"
        else:
            return None

