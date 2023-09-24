from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QRadioButton, QFileDialog, QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap, QFont, QPalette
from PyQt5.QtCore import Qt, QTimer
import sys
from antivirus.mavoc_time import DateTimeWidget


def init_ui(self):
        self.setWindowTitle("Mavoc Antivirus")
        self.setGeometry(200, 200, 1400, 750)

        # Set background picture
        background_label = QLabel(self)
        pixmap = QPixmap("mavoc-ui.png")
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        # Date and time of mavoc
        self.datetime_widget = DateTimeWidget()
        self.setCentralWidget(self.datetime_widget)

        label = self.datetime_widget.datetime_label
        label.setStyleSheet("color: white;")  # Set text color to white
        label.setFont(QFont("monospace", 14))  # Set the font size and family
        label.setAlignment(Qt.AlignTop | Qt.AlignRight)  # Align label to the top-right corner

        # Set the label's size and position
        label.setGeometry(self.width() -  348, 50, 350, 20)  # Adjust the position and size as needed



        #  design elements
 #       label = QLabel("", self)
  #      label.setGeometry(280, 100, 200, 50)
   #     label.setStyleSheet("color: white; ;font-family: monospace; font-size: 27px;text-shadow: 3px 3px 5px black;")


        # Use QPushButton instead of QOpenGLWidget
        scan_button = QPushButton("Quick Scan", self)
        scan_button.setGeometry(275, 200, 200, 50)
        scan_button.setStyleSheet(
            "QPushButton { border : 2px solid black; border-radius : 20px; background-color: green; color: white; font-size: 18px; }"
            "QPushButton:hover { background-color: darkgreen; }"
        )

        scan_button.clicked.connect(self.run_quick_scan)

        fullscan_button = QPushButton("Full Scan", self)
        fullscan_button.setGeometry(275, 300, 200, 50)
        fullscan_button.setStyleSheet(
            "QPushButton { border : 2px solid black; border-radius : 20px; background-color: #3498DB; color: white; font-size: 18px; }"
            "QPushButton:hover { background-color: #1c689c }"
        )
        fullscan_button.clicked.connect(self.run_full_scan)

        cloudbasedscan_button = QPushButton("Cloud Frim Scan", self)
        cloudbasedscan_button.setGeometry(275, 400, 200, 50)
        cloudbasedscan_button.setStyleSheet(
            "QPushButton { border : 2px solid black; border-radius : 20px; background-color: #ba1e1e; color: white; font-size: 18px;}"
            "QPushButton:hover { background-color: #961717 }"
        )
        cloudbasedscan_button.clicked.connect(self.run_cloud_scan)

        deltempfiles_button = QPushButton("Clean System", self)
        deltempfiles_button.setGeometry(275, 500, 200, 50)
        deltempfiles_button.setStyleSheet(
            "QPushButton {border : 2px solid black; border-radius : 20px; background-color: darkviolet; color: white; font-size: 18px;}"
            "QPushButton:hover  { background-color: #691199 }"
        )
        deltempfiles_button.clicked.connect(self.delete_temp_files)

        network_security_button = QPushButton("Network Protection", self)
        network_security_button.setGeometry(275 , 600 , 200 , 50)
        network_security_button.setStyleSheet(
            "QPushButton {border : 2px solid black; border-radius : 20px; background-color: #1dafbf; color: white; font-size: 18px; }"
            "QPushButton:hover { background-color: #1e7f8a }"
            )
        network_security_button.clicked.connect(self.network_security)
#        network_security_button.clicked.connect(self)


## 1ST BLACK BOX CONTENT

        self.hash_text_edit = QTextEdit(self)
        self.hash_text_edit.setGeometry(600, 150, 500, 200)
       # self.hash_text_edit.setStyleSheet(
       #     "background-color: lightgray; color: black; font-size: 14px;"
       # )
        self.hash_text_edit.setStyleSheet("background-color: black; color: #00FF00; font-size: 14px;")


### 2ND BLACK BOX CONTENT 

        self.status_text_edit = QTextEdit(self)
        self.status_text_edit.setGeometry(600, 450, 500, 250)
        self.status_text_edit.setStyleSheet(
            "background-color: darkblue; color: white; font-size: 14px;"
        )

        # Add progress bar
        self.show()

        ## Adding Bar
        #### For File Menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Files")
        add_menu_md5 = QAction("Add Single MD5 Hash", self)
        add_menu_sha = QAction("Add Single SHA-256 Hash", self)
        view_menu_md5 = QAction("View MD5 DB", self)
        view_menu_sha = QAction("View SHA256 DB",self)
        add_file_md5 = QAction("Add MD5 File", self)
        add_file_sha = QAction("Add SHA256 File", self)



        add_menu_md5.triggered.connect(self.add_md5_to_database)
        add_menu_sha.triggered.connect(self.add_sha256_to_database)
        view_menu_md5.triggered.connect(self.view_md5_database)
        view_menu_sha.triggered.connect(self.view_sha256_database)
        add_file_md5.triggered.connect(self.add_md5_database)
        add_file_sha.triggered.connect(self.add_sha256_database)

        file_menu.addAction(add_menu_md5)
        file_menu.addAction(add_menu_sha)
        file_menu.addAction(add_file_md5)
        file_menu.addAction(add_file_sha)
        file_menu.addAction(view_menu_md5)
        file_menu.addAction(view_menu_sha)

        ## For Special Options !

        options_menu = menu_bar.addMenu("Options")
        update_menu = QAction("Update", self)
        add_menu = QAction("Contact", self)
        update_menu.triggered.connect(self.update_info)
        add_menu.triggered.connect(self.contact_info)
        options_menu.addAction(update_menu)
        options_menu.addAction(add_menu)
        

        ## For File Menu !
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("Info", self)
        about_help = QAction("Help", self)
        about_action.triggered.connect(self.show_about_dialog)
        about_help.triggered.connect(self.show_help_menu)
        help_menu.addAction(about_action)
        help_menu.addAction(about_help)


        self.show()

def show_help_menu(self):
            about_text1 =  """ 
    <title>Mavoc Antivirus Guide</title>
    <style>
    body {
    font-family: "MonoSans", sans-serif;
    }

    h1, h2, h3, p {
    margin: 0 0 10px 0;
    }

    h1 {
    font-size: 24px;
    }

    h2 {
    font-size: 20px;
    }

    h3 {
    font-size: 18px;
    }

    p {
    line-height: 1.5;
    }
    </style>
    </head>
    <body>
    <center><h2>Guide to use Mavoc Antivirus tool</h2></center>
    <p>
    There are three options you can use in this tool:
    </p>
    <ul>
    <li>Quick Scan</li>
    <li>Full Scan</li>
    <li>Cloud Scan</li>
    <li>Clean System</li>
    </ul>
    <h2>Quick Scan</h2>
    <p>
    Quick scan allows you scan specfic paths to search for malicious code and after the process completion the result of the scan will be displayed and request permission to remove it from the disk if any malware is found.
    </p>
    <h2>Full Scan</h2>
    <p>
    Full scan allows you to select a particular directory or A complete Partition can be scanned to verify the presence of malware and request permission to be removed from the system disk if any malware is found.
    Partition Scan Allows you scan specifc partiton and directories . It will List out once if the Malicious files has been found .
    </p>
    <h2>Cloud Firm Scan</h2>
    <p>
    Cloud from scan allows you to select cloud storage by selecting the directory from the network section in the file manager or Files section in MAC.
    Please Contact <b><a href="https://github.com/Whitecat18" > Smukx </a></b> for Implementing Cloud Databases </p>
    <h2>Clean System</h2>
    <p>
    This Option allows you to remove Unwanted Temp files as well as any Unwanted Malicious files in your system and makes your system fast . 
    </p>
    </body>
    </html>
    """
            QMessageBox.about(self, "Mavoc Help" , about_text1)

