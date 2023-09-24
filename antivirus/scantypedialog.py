from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 


class ScanTypeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Scan Type")
        self.setMinimumWidth(300) 
        self.setMinimumHeight(100)
        layout = QVBoxLayout()
        
        self.recursive_radio = QRadioButton("Quick Recursive Scan")
        self.non_recursive_radio = QRadioButton("Quick Non-Recursive Scan")
        
        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.recursive_radio)
        radio_layout.addWidget(self.non_recursive_radio)

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

    def get_selected_option(self):
        if self.recursive_radio.isChecked():
            return "recursive"
        elif self.non_recursive_radio.isChecked():
            return "non_recursive"
        else:
            return None
