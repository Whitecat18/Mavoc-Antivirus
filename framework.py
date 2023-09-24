'''
Mavoc-Antivirus Tool
By Smukx 
My Opensource Codes :https://github.com/Whitecat18
For Work : https://www.linkedin.com/in/smukx/
'''

from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui  
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
import os
from select import select
import sys 
import shutil 
import ctypes 
import hashlib 
import tempfile 
from turtle import update 
import typing 
from PyQt5 import QtCore 
import requests 
import subprocess 
from send2trash import send2trash 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import psutil
from datetime import datetime
import self
import time
import threading
from antivirus.ui_design import show_help_menu


'''
        self.status_text_edit.clear()
        self.hash_text_edit.clear()

Theses mode is used to clear the screen of the black ones . To clear the screen , append the module at front

certutil -hashfile Example.txt MD5
certutil -hashfile Example.txt SHA256

'''



## Password autherntication

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mavoc Login")
        self.setGeometry(100, 100, 200, 200)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        image_label = QLabel(self)
        pixmap = QPixmap("core\mavoc_banner.jpg")  
       # pixmap = QPixmap("mavoc-anti.png")
        pixmap = pixmap.scaledToWidth(500)  
        image_label.setPixmap(pixmap)
        layout.addWidget(image_label)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)
        login_button = QPushButton("Login", self)
        login_button.clicked.connect(self.check_password)

        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        central_widget.setLayout(layout)

    def check_password(self):
        entered_password = self.password_input.text()

        if entered_password == "qwerty":
            self.close()
            self.run_antivirus_tool()
        else:
            self.show_wrong_password_message()
            sys.exit()


    def run_antivirus_tool(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Info from Smukx")
        msgbox.setText("<b><center>Welcome to Mavoc Antivitus .</center></b>")
        msgbox.setFixedSize(300, 150)
        msgbox.exec_()
        #print("Welcome to Mavoc Antivirus!")

    def show_wrong_password_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Wrong Password")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Incorrect password. Please try again.")
        msg_box.setFixedSize(300, 150)
        msg_box.exec_()



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


class fullscantypedialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Scanning Method ...")
        self.setMinimumWidth(300)
        self.setMinimumHeight(100)


        layout = QVBoxLayout()

        self.recursive_radio = QRadioButton("Full Scan")
        self.nonrecursive_radio = QRadioButton("Partition Scan")

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.recursive_radio)
        radio_layout.addWidget(self.nonrecursive_radio)

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

    def full_scan_selected_options(self):
        if self.recursive_radio.isChecked():
            return "full_scan"
        elif self.nonrecursive_radio.isChecked():
            return "partition_scan"
        else:
            return None

class networkProtectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Network Protection")
        self.setMinimumWidth(300)
        self.setMinimumHeight(150)

        layout = QVBoxLayout()

        self.enable_radio = QRadioButton("Enable Protection")
        self.disable_radio = QRadioButton("Disable Protection")

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.enable_radio)
        radio_layout.addWidget(self.disable_radio)

        layout.addLayout(radio_layout)

        # Button to open the hosts file
        self.open_hosts_button = QPushButton("Open BlackList File")
        self.open_hosts_button.clicked.connect(self.open_hosts_file)

        layout.addWidget(self.open_hosts_button)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def network_protection_selected_option(self):
        if self.enable_radio.isChecked():
            return "enable"
        elif self.disable_radio.isChecked():
            return "disable"
        else:
            return None

    def open_hosts_file(self):
        hosts_path = r'network\blacklist.txt'
        if os.path.exists(hosts_path):
            os.system(f'notepad.exe {hosts_path}')
        else:
            QMessageBox.critical(self, "Error", "The hosts file does not exist.")


## SHEDULE CLASS PROGRAMMING 
class ScheduleScanDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Schedule Scan")
        self.setMinimumWidth(300)
        self.setMinimumHeight(150)

        layout = QVBoxLayout()

        self.enable_radio = QRadioButton("Enable Schedule Scan")
        self.disable_radio = QRadioButton("Disable Schedule Scan")

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.enable_radio)
        radio_layout.addWidget(self.disable_radio)

        layout.addLayout(radio_layout)

        # Button to open the schedule scan log file
        self.open_log_button = QPushButton("Open Schedule Scan Log")
        self.open_log_button.clicked.connect(self.open_schedule_scan_log)

        layout.addWidget(self.open_log_button)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

    def schedule_scan_selected_option(self):
        if self.enable_radio.isChecked():
            return "enable"
        elif self.disable_radio.isChecked():
            return "disable"
        else:
            return None



"""
class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mavoc Antivirus Login")
        self.setGeometry(100, 100, 400, 200)

        self.password_label = QLabel("Enter Password:")
        self.password_input = QLineEdit()
        self.login_button = QPushButton("Login")

        layout = QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

        self.login_button.clicked.connect(self.check_password)

        self.correct_password = "qwerty"

    def check_password(self):
        entered_password = self.password_input.text()

        if entered_password == self.correct_password:
            self.close()  # Close the login window
            self.run_antivirus_tool()
        else:
            self.show_wrong_password_message()
            sys.exit()

    def run_antivirus_tool(self):
        # Your Mavoc Antivirus functionality logic goes here
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Info from Smukx")
        msgbox.setText("Welcome to Mavoc Antivitus")
        msgbox.setFixedSize(400, 200)
        msgbox.exec_()
        #print("Welcome to Mavoc Antivirus!")

    def show_wrong_password_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Wrong Password")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Incorrect password. Please try again.")
        msg_box.exec_()
"""

 
## PASSWORD AUTH LOGIN !!

"""
class PasswordDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(PasswordDialog, self).__init__(parent)

        self.setWindowTitle("Enter Password")
        self.setGeometry(200, 200, 200)

        self.passwordLineEdit = QtWidgets.QLineEdit(self)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

        self.submitButton = QtWidgets.QPushButton("Submit", self)

        self.connect(self.submitButton, QtCore.SIGNAL("clicked()"), self.onSubmitButtonClicked)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.passwordLineEdit)
        layout.addWidget(self.submitButton)

        self.setLayout(layout)

    def password_auth(self):
        self.passwordLineEdit.clear()
        self.submitButton.setText("Authenticate")

    def onSubmitButtonClicked(self):
        password = self.passwordLineEdit.text()

        # Do something with the password here.

        self.accept()

def password_auth():
    app = QtWidgets.QApplication(sys.argv)

    dialog = PasswordDialog()
    dialog.password_auth()
    dialog.show()

    sys.exit(app.exec_())
"""

# PROGRAM FOR FULL MOUNTING USING psutil MODULE

#import psutil
### PSUTIL PROGRAM TO AUTOMOUNT ALL PARTITION 

"""

def run_full_computer_scan(self):
    self.status_text_edit.clear()
    self.hash_text_edit.clear()

    self.log("Running Full Computer Scan ...")

    partitions = psutil.disk_partitions(all=True)

    self.status("Scanning for malicious files...\n")

    signature_hashes_md5 = set()
    signature_hashes_sha256 = set()
    with open("hashes/md5_hashes.txt", "r") as hash_file_md5, open("hashes/sha256_hashes.txt", "r") as hash_file_sha256:
        for line_md5, line_sha256 in zip(hash_file_md5, hash_file_sha256):
            signature_hashes_md5.add(line_md5.strip())
            signature_hashes_sha256.add(line_sha256.strip())

    virus_extensions = set()
    with open("hashes/virus-extensions.txt", "r") as ext_file:
        for line in ext_file:
            virus_extensions.add(line.strip())

    detected_malicious_files = []
    for partition in partitions:
        detected_malicious_files.extend(self.scan_directory_recursive(partition.mountpoint, signature_hashes_md5, signature_hashes_sha256, virus_extensions))

    if detected_malicious_files:
        self.log("Detected malicious files:\n")
        self.hash_text_edit.insertPlainText("Hash Information:\n")
        for file_info in detected_malicious_files:
            file_path, checksum_md5, checksum_sha256, extension = file_info
            self.log(f"File: {file_path}, Extension: {extension}\n")
            self.hash_text_edit.insertPlainText(f"File: {file_path}\nMD5 Hash: {checksum_md5}\nSHA256 Hash: {checksum_sha256}\nExtension: {extension}\n\n")
            self.confirm_and_remove_file(file_path, os.path.basename(file_path))
        self.status("Malicious files detected. Review hash information.")
    else:
        self.log("No malicious files detected.\n")
        self.status("No malicious files detected.")

    self.log("\nFull Computer Scan completed.")
    self.hash_text_edit.verticalScrollBar().setValue(self.hash_text_edit.verticalScrollBar().maximum())

"""

class TextViewDialog(QDialog):
    def __init__(self, title, content, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        
        layout = QVBoxLayout(self)
        
        text_browser = QTextBrowser(self)
        text_browser.setPlainText(content)
        layout.addWidget(text_browser)
        
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)
        
        self.setLayout(layout)

class MaliciousFilesDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Detected Malicious Files")
        layout = QVBoxLayout()
        self.text_browser = QTextBrowser(self)
        layout.addWidget(self.text_browser)
        self.setLayout(layout)

    def set_malicious_files(self, files):
        self.text_browser.setPlainText("\n".join(files))

# Progress bar to scan malicious files 

class ScanThread(QThread):
    progress_updated = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.stopped = False

    def run(self):
        total_files = 100  # Example total number of files to scan
        for file_num in range(1, total_files + 1):
            if self.stopped:
                break
            # Simulate scanning a file
            self.progress_updated.emit(int(file_num * 100 / total_files))
            self.msleep(100)  # Simulate the scan process

class LoadingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scanning...")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        layout.addWidget(self.progress_bar)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_scan)
        layout.addWidget(self.cancel_button)

        self.setLayout(layout)

    def set_progress(self, percentage):
        self.progress_bar.setValue(percentage)

    def cancel_scan(self):
        self.parent_thread.stopped = True
        self.close()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.scan_thread = ScanThread()

        self.loading_window = LoadingWindow()
        self.loading_window.parent_thread = self.scan_thread

        self.scan_thread.progress_updated.connect(self.loading_window.set_progress)

        start_scan_button = QPushButton("Start Scan")
        start_scan_button.clicked.connect(self.start_scan)
        self.setCentralWidget(start_scan_button)

    def start_scan(self):
        self.loading_window.show()
        self.scan_thread.start()

### ------------------------------------------------------------------------###
###                         MAIN CLASS STARTS HERE                          ###
###                     BE CAREFUL TO EDIT THIS CLASS                       ###
###         THIS MAY HARM SYSTEM IF FILE CONFIGS ARE NOT PROPER             ###
###-------------------------------------------------------------------------###


class AntivirusUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        show_help_menu(self)
#        self.detected_malicious_files = []
        self.malicious_files_dialog = MaliciousFilesDialog(self)
        
        ## SHEDULE SCAN PROGRAM USING SUBPROCESS 
 
        self.start_schedule_scan_action = QAction("Start Schedule Scan", self)
        self.start_schedule_scan_action.triggered.connect(self.start_schedule_scan)
        self.addAction(self.start_schedule_scan_action)

    def start_schedule_scan(self):
        try:
            # Start the CLI program as a subprocess
            self.schedule_scan_process = subprocess.Popen([sys.executable, "schedule-scanning.py", "1"])

        except Exception as e:
            # Handle any exceptions if the subprocess fails to start
            print(f"Failed to start the schedule scan: {str(e)}")

    def closeEvent(self, event):
        # This method is called when the GUI program is closed
        # You can use it to terminate the subprocess and close the program gracefully
        if hasattr(self, 'schedule_scan_process') and self.schedule_scan_process.poll() is None:
            # If the subprocess is still running, terminate it
            self.schedule_scan_process.terminate()
            self.schedule_scan_process.wait()

        event.accept()  # Close the GUI program


## RUN WITH ADMIN PRIVILAGE 


    def run_with_elevated_privileges(command):
        runas_command = ["runas", "/user:Administrator", "powershell", "-Command", command]
        subprocess.run(runas_command, shell=True)

    def run_as_admin():
        if ctypes.windll.shell32.IsUserAnAdmin() == 0:
            print("Requesting admin privileges...")
            command = "Remove-Item -Path 'C:\\Path\\To\\Your\\Suspicious\\Files\\*' -Recurse -Force"
            run_with_elevated_privileges(command)
        else:
            print("Running with admin privileges.")



    def password_auth(self):
        self.setWindowTitle("Mavoc Autherntication")
        self.setGeometry(200,200.200,200)
        

    def show_malicious_files(self, files):
        self.malicious_files_dialog.set_malicious_files(files)
        self.malicious_files_dialog.exec_()

    ## UI OF THE MAVOC-ANTIVIRUS 

    ## MAIN BUTTONS
    
    def init_ui(self):
        self.setWindowTitle("Mavoc Antivirus")
        self.setGeometry(200, 200, 1500, 750)

        # Set background picture
        background_label = QLabel(self)
        pixmap = QPixmap("core\Mavoc antivirus.png")
        background_label.setPixmap(pixmap)
        background_label.setGeometry(0, 0, pixmap.width(), pixmap.height())

        app_icon = QIcon("core\mavoc_icon.png")
        self.setWindowIcon(app_icon)

        #  design elements
        label = QLabel("", self)
        label.setGeometry(280, 100, 200, 50)
        label.setStyleSheet("color: white; ;font-family: monospace; font-size: 27px;text-shadow: 3px 3px 5px black;")


        # Use QPushButton instead of QOpenGLWidget
        scan_button = QPushButton(" Quick Scan", self)

        # Set the size of the icon
        scan_button.setIconSize(QSize(43, 43))

        # Set the icon for the button
        icon = QIcon("core\stopwatch.png")
        scan_button.setIcon(icon)

        scan_button.setGeometry(200, 110,  304, 120)
        scan_button.setStyleSheet(
           "QPushButton { border: 3px solid black; border-radius: 18px; background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #E8E8E8, stop: 1 #E8E8E8); color: #00008B; font-size: 23px; font-weight: bold; font-family: 'League Spartan', sans-serif; }"
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #D9D9DD, stop: 1 #D9D9DD); }"


        )

        scan_button.clicked.connect(self.run_quick_scan)

        # SHEDULE SCAN CHANGE
        scan_button = QPushButton(" Schedule Scan", self)

        # Set the size of the icon
        scan_button.setIconSize(QSize(43, 43))

        # Set the icon for the button
        icon = QIcon("core\schedule.png")
        scan_button.setIcon(icon)

        scan_button.setGeometry(631, 110,  304, 120)
        scan_button.setStyleSheet(
              "QPushButton { border: 3px solid black; border-radius: 18px; background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #E8E8E8, stop: 1 #E8E8E8); color: #00008B; font-size: 23px; font-weight: bold; font-family: 'League Spartan', sans-serif; }"
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #D9D9DD, stop: 1 #D9D9DD); }"
        )
        scan_button.clicked.connect(self.open_schedule_scan_log)

        # Full Scan
        fullscan_button = QPushButton(" Full Scan", self)

        # Set the size of the icon
        fullscan_button.setIconSize(QSize(43, 43))

        # Set the icon for the button
        icon = QIcon("core\error.png")
        fullscan_button.setIcon(icon)

        # Set the geometry for the button
        fullscan_button.setGeometry(1050, 110, 304, 120)

        # Set the stylesheet for the button
        fullscan_button.setStyleSheet(
            "QPushButton { border: 3px solid black; border-radius: 18px; background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #E8E8E8, stop: 1 #E8E8E8); color: #00008B; font-size: 23px; font-weight: bold; font-family: 'League Spartan', sans-serif; }"
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #D9D9DD, stop: 1 #D9D9DD); }"
        )
        fullscan_button.clicked.connect(self.run_full_scan)

        #   NETWORK SCAN

        network_security_button = QPushButton(" Network Protection", self)

        # Set the size of the icon
        network_security_button.setIconSize(QSize(43, 43))

        # Set the icon for the button
        icon = QIcon("core\globe-grid.png")
        network_security_button.setIcon(icon)

        # Set the geometry for the button
        network_security_button.setGeometry(200, 260, 304, 120)

        # Set the stylesheet for the button
        network_security_button.setStyleSheet(
            "QPushButton { border: 3px solid black; border-radius: 18px; background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #E8E8E8, stop: 1 #E8E8E8); color: #00008B; font-size: 23px; font-weight: bold; font-family: 'League Spartan', sans-serif; }"
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #D9D9DD, stop: 1 #D9D9DD); }"
        )
        network_security_button.clicked.connect(self.show_network_protection_dialog)

        #   CLOUD SCAN

        cloudbasedscan_button = QPushButton("Cloud Frim Scan", self)

        # Set the size of the icon
        cloudbasedscan_button.setIconSize(QSize(43, 43))

        # Set the icon for the button
        icon = QIcon("core\security.png")
        cloudbasedscan_button.setIcon(icon)

        # Set the geometry for the button
        cloudbasedscan_button.setGeometry(631, 260, 304, 120)

        # Set the stylesheet for the button
        cloudbasedscan_button.setStyleSheet(
            "QPushButton { border: 3px solid black; border-radius: 18px; background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #E8E8E8, stop: 1 #E8E8E8); color: #00008B; font-size: 23px; font-weight: bold; font-family: 'League Spartan', sans-serif; }"
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #D9D9DD, stop: 1 #D9D9DD); }"
        )
        cloudbasedscan_button.clicked.connect(self.run_cloud_scan)

        #   CLEAN System

        # Create a QPushButton widget for the clean system button
        deltempfiles_button = QPushButton(" Clean System", self)

        # Set the size of the icon
        deltempfiles_button.setIconSize(QSize(43, 43))

        # Set the icon for the button
        icon = QIcon("core\system.png")
        deltempfiles_button.setIcon(icon)

        # Set the geometry for the button
        deltempfiles_button.setGeometry(1050, 260, 304, 120)

        # Set the stylesheet for the button
        deltempfiles_button.setStyleSheet(
            "QPushButton { border: 3px solid black; border-radius: 18px; background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #E8E8E8, stop: 1 #E8E8E8); color: #00008B; font-size: 23px; font-weight: bold; font-family: 'League Spartan', sans-serif; }"
            "QPushButton:hover { background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #D9D9DD, stop: 1 #D9D9DD); }"
        )
        deltempfiles_button.clicked.connect(self.delete_temp_files)


## 1ST BLACK BOX CONTENT

        self.hash_text_edit = QTextEdit(self)
        self.hash_text_edit.setGeometry(200, 420, 500, 250)
       # self.hash_text_edit.setStyleSheet(
       #     "background-color: lightgray; color: black; font-size: 14px;"
       # )
        self.hash_text_edit.setStyleSheet("border : 2px solid black; border-radius : 20px; background-color: #00008B; color: white; font-size: 18px; ")


### 2ND BLACK BOX CONTENT 

        self.status_text_edit = QTextEdit(self)
        self.status_text_edit.setGeometry(850, 420, 500, 250)
        self.status_text_edit.setStyleSheet(
            "border : 2px solid black; border-radius : 20px; background-color: #00008B; color: white; font-size: 18px;"
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
        view_logs = QAction("View Logs", self)
        update_menu.triggered.connect(self.update_info)
        add_menu.triggered.connect(self.contact_info)
        view_logs.triggered.connect(self.view_hash)
        options_menu.addAction(update_menu)
        options_menu.addAction(add_menu)
        options_menu.addAction(view_logs)
        

        ## For File Menu !
        help_menu = menu_bar.addMenu("Help")
        about_action = QAction("Info", self)
        about_help = QAction("Help", self)
        summary_guide = QAction("Summary",self)
        about_action.triggered.connect(self.show_about_dialog)
        about_help.triggered.connect(self.show_help_menu)
        summary_guide.triggered.connect(self.summary_page)
        help_menu.addAction(about_action)
        help_menu.addAction(about_help)
        help_menu.addAction(summary_guide)

        ## LOG VIEWER

        log_analysis = menu_bar.addMenu("Logs")

        log_quick_recursive = QAction("Quick Scan Logs", self)
        log_non_recursive = QAction("Partition Scan Log", self)
        log_cloud_scan = QAction("Cloud Logs", self)
        log_shedule_scan = QAction("Scheduled Logs", self)

        log_quick_recursive.triggered.connect(self.quickscan_logs)
        log_non_recursive.triggered.connect(self.non_recursive_logs)
        log_cloud_scan.triggered.connect(self.cloud_logs)
        log_shedule_scan.triggered.connect(self.shedule_logs)
        
        log_analysis.addAction(log_quick_recursive)
        log_analysis.addAction(log_non_recursive)
        log_analysis.addAction(log_cloud_scan)
        log_analysis.addAction(log_shedule_scan)


        self.show()

    def contact_info(self):
        contact_box = """
        <h3> Contact of Creators</h3>
        Smukx -> <b> Framework and Core Creator </b>
        """
        QMessageBox.about(self, "Mavoc Help" , contact_box)

    def update_info(self):
        update_box = """
        <center><h4> Update Module </h4></center><br>
        <b> Antivirus Version 1.0.0 </b><br>

        """ 
        QMessageBox.about(self, "Update", update_box)

#    def view_hash(self):
#        log_history = self.read_file_content("log-file.txt")
#        self.show_text_dialog("Log History", log_history )

# SUMMARY OPENING PAGE BOX 

    def summary_page(self):
        os.system("powershell.exe Start-Process https://github.com/Whitecat18/Mavoc-Antivirus")

# QUICK SCAN VIEW BUTTONS 

    def view_hash(self):
        log_history = self.read_file_content("logfiles/log-file-nonrecursive-quick-scan.txt")
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Quick Scan Result")
        dialog.setGeometry(100, 100, 800, 600)
        
        text_edit = QTextEdit(dialog)
        text_edit.setPlainText(log_history)
        text_edit.setFontPointSize(15)  # Set the font size to 12 (customize as needed)
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()
        
    def quickscan_logs(self):
        log_history = self.read_file_content("logfiles/log-file-nonrecursive-quick-scan.txt")
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Quick Scan Result")
        dialog.setGeometry(100, 100, 800, 600)
        
        text_edit = QTextEdit(dialog)
        text_edit.setPlainText(log_history)
        text_edit.setFontPointSize(15)  # Set the font size to 12 (customize as needed)
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()

# LOG VIEWER BUTTON MODULES !

    def non_recursive_logs(self):
        log_history = self.read_file_content("logfiles/log-file.txt")
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Partition Scan Result")
        dialog.setGeometry(100, 100, 800, 600) 
        
        text_edit = QTextEdit(dialog)
        text_edit.setPlainText(log_history)
        text_edit.setFontPointSize(15)  # Set the font size to 12 (customize as needed)
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()

    # CLOUD LOG VIEWER
        
    def cloud_logs(self):
        log_history = self.read_file_content("logfiles/log-file-cloud-scan.txt")
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Cloud Log Result")
        dialog.setGeometry(100, 100, 800, 600) 
        
        text_edit = QTextEdit(dialog)
        text_edit.setPlainText(log_history)
        text_edit.setFontPointSize(15)  # Set the font size to 12 (customize as needed)
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()

    # SHEDULE SCAN LOG VIEWER

    def shedule_logs(self):
        log_history = self.read_file_content("logfiles/schedule-log.txt")
        
        dialog = QDialog(self)
        dialog.setWindowTitle("Shedule Scan Log")
        dialog.setGeometry(100, 100, 800, 600) 
        
        text_edit = QTextEdit(dialog)
        text_edit.setPlainText(log_history)
        text_edit.setFontPointSize(15)  # Set the font size to 12 (customize as needed)
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()

#    def view_md5_database(self):
#        content = self.read_file_content("md5_hashes.txt")
#        self.show_text_dialog("MD5 Hashes", content)



    def show_about_dialog(self):
        about_text = """ 
        <h2>Mavoc Antivirus.inc</h2> 
        <p> An Opensource Mini Antivirus Tool Written By Smukx<p>
        Created By <b><a href="https://github.com/Whitecat18" > Smukx</a></b>
        <p> Follow me at <a href="https://twitter.com/Smukx07" > Twitter </a></p>

        """
        QMessageBox.about(self, "About Mavoc Antivirus", about_text)

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
<li>schedule Scan</li>
<li>Full Scan</li>
<li>Cloud Scan</li>
<li>Network Scan</li>
<li>Clean System</li>
</ul>
<h2>Quick Scan</h2>
<p>
Quick scan allows you to select a particular file that needs to be scanned for the presence of malicious code and after the process completion the result of the scan will be displayed and request permission to remove it from the disk if any malware is found.
</p>
<h2>Schedule Scan</h2>
<p>Schedule Scan is used to scan for an particular time when antivirus starts running</p>
<h2>Full Scan</h2>
<p>
Full scan allows you to select a particular directory or A complete Partition can be scanned to verify the presence of malware and request permission to be removed from the system disk if any malware is found.
</p>
<h2>Cloud Firm Scan</h2>
<p>
Cloud from scan allows you to select cloud storage by selecting the file sending it to the largest databases to check with multiple checksums .
Please Contact <b><a href="https://github.com/Whitecat18" > Smukx </a></b> for Implementing Cloud Databases </p>
<h2>Clean System</h2>
<p>
This Option allows you to remove the temp in your system if any backdoor or any executable file that contains malware is installed in the temp file section of your computer. The unwanted executable file in the temp file of your system might pave the way for a hacker to easily penetrate into your system and can lead to a Data breach.
</p>
<h2> Network Scan </h2>
<p> Network Proctection prevents the user from reaching to malicious sites. This contains a list of vulnerable sites in a Database which could make the user's data more vulnerable, so the sites in the database will be written to the hosts files in the etc folder of Windows machines. So any browser on the windows system first checks for the hosts file before reaching the site </p>
<h2> Scheduled Scan</h2>
<p> This creates a ease for the user to scan their systems for malicious files without scanning maually</p>
</body>
</html>        
"""
        QMessageBox.about(self, "Mavoc Help" , about_text1)

    def add_md5_to_database(self):
        text, ok = QInputDialog.getText(self, "Add MD5 Hash", "Enter the MD5 Hash:")
        if ok and text:
            with open("hashes/md5_hashes.txt", "a") as md5_file:
                md5_file.write(text + "\n")

    def add_sha256_to_database(self):
        text, ok = QInputDialog.getText(self, "Add SHA256 Hash", "Enter the Hash:")
        if ok and text:
            with open("hashes/sha256_hashes.txt", "a") as sha256_file:
                sha256_file.write(text + "\n")

## HASH CONTENT DISPLAY ON FILE OPTION

#    def view_md5_database(self):
#      content = self.read_file_content("md5_hashes.txt")
#     self.show_text_dialog("MD5 Hashes", content)

    def view_md5_database(self):
        log_history = self.read_file_content("hashes/md5_hashes.txt")
        
        dialog = QDialog(self)
        dialog.setWindowTitle("MD5 Hashes")
        dialog.setGeometry(100, 200, 800, 600)  # Set the size of the dialog
        
        text_edit = QTextEdit(dialog)
        text_edit.setPlainText(log_history)
        text_edit.setFontPointSize(12)  # Set the font size to 12 (customize as needed)
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()

#    def view_sha256_database(self):
#        content = self.read_file_content("sha256_hashes.txt")
#        self.show_text_dialog("SHA-256 Hashes", content)

    def view_sha256_database(self):
        log_history = self.read_file_content("hashes/sha256_hashes.txt")
        
        dialog = QDialog(self)
        dialog.setWindowTitle("SHA-256 Hashes")
        dialog.setGeometry(100, 200, 800, 600)  # Set the size of the dialog
        
        text_edit = QTextEdit(dialog)
        text_edit.setPlainText(log_history)
        text_edit.setFontPointSize(12)  # Set the font size to 12 (customize as needed)
        text_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout = QVBoxLayout()
        layout.addWidget(text_edit)
        
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.close)
        
        layout.addWidget(close_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def read_file_content(self, filename):
        try:
            with open(filename, "r") as file:
                return file.read()
        except Exception as e:
            return str(e)

    def show_text_dialog(self, title, content):
        text_dialog = TextViewDialog(title, content, parent=self)
        text_dialog.exec_()

#### ADD HASHES TO THE DATABASE

    def add_md5_database(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select MD5 Database File", "", "Text Files (*.txt)")
        if file_path:
            self.add_hashes_to_database(file_path, "hashes/md5_hashes.txt")

    def add_sha256_database(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select SHA-256 Database File", "", "Text Files (*.txt)")
        if file_path:
            self.add_hashes_to_database(file_path, "hashes/sha256_hashes.txt")

    def add_hashes_to_database(self, source_file, target_file):
        try:
            with open(source_file, "r") as source:
                hashes = source.read()
                with open(target_file, "a") as target:
                    target.write("\n" + hashes)
            self.log(f"Added hashes from {source_file} to {target_file}\n")
        except Exception as e:
            self.log(f"Error adding hashes: {e}\n")

    ### RECURSIVE SCANNING METHODS

    def scan_directory_non_recursive(self, directory):
        print(f"Scanning directory: {directory}")
        found_files = []
        for root, _, files in os.walk(directory):
            for filename in files:
                _, extension = os.path.splitext(filename)
                if extension.lower() in suspicious_extensions:
                    print(f"Found suspicious file: {os.path.join(root, filename)}")
                    checksum_md5, checksum_sha256 = self.calculate_hashes(os.path.join(root, filename))
                    found_files.append((filename, checksum_md5, checksum_sha256, extension))

        return found_files 
    
    def scan_directory_recursive_for_full(self, directory_path, signature_hashes_md5, signature_hashes_sha256, virus_extensions):
        detected_malicious_files = []

        for root, _, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                _, file_extension = os.path.splitext(filename)
                checksum_md5, checksum_sha256 = self.calculate_hashes(file_path)
                if checksum_md5 is not None and checksum_sha256 is not None:
                    if checksum_md5 in signature_hashes_md5 or checksum_sha256 in signature_hashes_sha256 or file_extension[1:] in virus_extensions:
                        detected_malicious_files.append((file_path, checksum_md5, checksum_sha256, file_extension))

        return detected_malicious_files
    
    ### CLOUD SCAN USING VIRUS TOTAL API

    def run_cloud_scan(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File for Cloud Scan", "", "All Files (*)", options=options)

        if file_path:
            with open("logfiles/log-file-cloud-scan.txt", "w") as log_file:
                # Define a helper function to log messages both to the GUI and the file
                def log(message):
                    self.log(message)
                    log_file.write(message)

                log(f"Running Cloud Scan on: {file_path}\n")
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log(f"Current Scanning Time: {current_time}\n")

                self.status("Uploading file to Cloud Scanner...\n")


                api_key = "ea90cf7dc3935bb0a94a9842ae5e52b397b7fec79b6478c7ea655127d11e2c0f"
                scan_id = self.upload_to_virustotal(file_path, api_key)

                if scan_id:
                    self.status("File uploaded. Checking scan status...\n")
                    scan_results = self.check_scan_status(scan_id, api_key)

                    if scan_results:
                        log("Cloud scan results:\n")
                        self.status_text_edit.insertPlainText("Cloud Scan Results:\n")
                        for engine, result in scan_results.items():
                            result_text = f"Engine: {engine}, Result: {result['detected']}, Version: {result['version']}, Update: {result['update']}\n"
                            log(result_text)
                            self.status_text_edit.insertPlainText(result_text)
                    else:
                        log("Cloud scan failed or results not available.\n")
                        self.status("Cloud scan failed or results not available.")
                else:
                    log("Cloud scan upload failed.\n")
                    self.status("Cloud scan upload failed.")
        else:
            self.status("Cloud Scan cancelled !")



    def upload_to_virustotal(self, file_path, api_key):
        url = "https://www.virustotal.com/vtapi/v2/file/scan"
        params = {"apikey": api_key}
        
        with open(file_path, "rb") as file:
            files = {"file": (os.path.basename(file_path), file)}
            response = requests.post(url, files=files, params=params)
            if response.status_code == 200:
                return response.json()["scan_id"]
            return None

    def check_scan_status(self, scan_id, api_key):
        url = f"https://www.virustotal.com/vtapi/v2/file/report"
        params = {"apikey": api_key, "resource": scan_id}
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            scan_results = response.json()
            if scan_results["response_code"] == 1:
                return scan_results["scans"]
        return None


    def calculate_hashes(self, file_path, chunk_size=8192):
        hash_md5 = hashlib.md5()
        hash_sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as file:
                while chunk := file.read(chunk_size):
                    hash_md5.update(chunk)
                    hash_sha256.update(chunk)
            return hash_md5.hexdigest(), hash_sha256.hexdigest()
        except PermissionError:
            return None,None
        
    def scan_directory_for_signatures_and_extensions(self, directory_path, signature_hashes_md5, signature_hashes_sha256, virus_extensions):
        detected_malicious_files = []

        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(filename)
                checksum_md5, checksum_sha256 = self.calculate_hashes(file_path)
                if checksum_md5 in signature_hashes_md5 or checksum_sha256 in signature_hashes_sha256 or file_extension[1:] in virus_extensions:
                    detected_malicious_files.append((filename, checksum_md5, checksum_sha256, file_extension))

        return detected_malicious_files

    def run_full_scan(self):
        
        self.status_text_edit.clear()
        self.hash_text_edit.clear()

        self.log("Running FullScan ...\n")

        scan_type_dialog = fullscantypedialog(self)
        result = scan_type_dialog.exec_()

        if result == QDialog.Accepted:
            selected_options = scan_type_dialog.full_scan_selected_options()

            if selected_options == "full_scan":
                self.run_complete_full_scan()
            elif selected_options == "partition_scan":
                self.run_partition_full_scan()
            else:
                self.log("No Scan Selected ..\n")


    def run_partition_full_scan(self):
        self.status_text_edit.clear()
        self.hash_text_edit.clear()

        # Create or open the log file for writing
        with open("logfiles/log-file.txt", "a") as log_file:
            # Define a helper function to log messages both to the GUI and the file
            def log(message):
                self.log(message)  
                log_file.write(message)

            log("Running Partition Scan ...\n")

            options = QFileDialog.Options()
            options |= QFileDialog.ReadOnly
            directory_path = QFileDialog.getExistingDirectory(self, "Select Directory for Full Scan", options=options)

            if directory_path:
                log(f"Running Full Scan on: {directory_path}\n")
                self.status("Scanning for malicious files...\n")

                # EXT_NEW
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log(f"Current Scanning Time: {current_time}\n")

                signature_hashes_md5 = set()
                signature_hashes_sha256 = set()
                with open("hashes/md5_hashes.txt", "r") as hash_file_md5, open("hashes/sha256_hashes.txt", "r") as hash_file_sha256:
                    for line_md5, line_sha256 in zip(hash_file_md5, hash_file_sha256):
                        signature_hashes_md5.add(line_md5.strip())
                        signature_hashes_sha256.add(line_sha256.strip())

                virus_extensions = set()
                with open("hashes/virus-extensions.txt", "r") as ext_file:
                    for line in ext_file:
                        virus_extensions.add(line.strip())

                detected_malicious_files = self.scan_directory_recursive(directory_path, signature_hashes_md5, signature_hashes_sha256, virus_extensions)

                if detected_malicious_files:
                    log("Detected malicious files:\n")
                    self.hash_text_edit.insertPlainText("Hash Information:\n")
                    for file_info in detected_malicious_files:
                        file_path, checksum_md5, checksum_sha256, extension = file_info
                        log(f"File: {file_path}, Extension: {extension}\n")
                        self.hash_text_edit.insertPlainText(f"File: {file_path}\nMD5 Hash: {checksum_md5}\nSHA256 Hash: {checksum_sha256}\nExtension: {extension}\n\n")
                        self.confirm_and_remove_file(file_path, os.path.basename(file_path))
                    self.status("Malicious files detected. Review hash information.")
                else:
                    log("No malicious files detected.\n")
                    self.status("No malicious files detected.")

                log("\nFull Scan completed.")
                self.hash_text_edit.verticalScrollBar().setValue(self.hash_text_edit.verticalScrollBar().maximum())
            else:
                log("Full Scan canceled by user.\n")



# NETWORK SCANNING SELECTION STARTS ...

    def show_network_protection_dialog(self):
        self.log("Network Blocker")

        dialog = networkProtectionDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            selected_option = dialog.network_protection_selected_option()
            
            if selected_option == "enable":
                subprocess.Popen([sys.executable, "network/network_protection.py"])
                self.log("\nSuccessfully Enabled Network Protection\n")

            elif selected_option == "disable":
                subprocess.Popen([sys.executable, "network/network_reverser.py"])
                self.log("\n\nNetwork Protection Reset to Default\n")



# SHEDULE SCANNING DIALOGUE

    def open_schedule_scan_log(self):
        log_path = "logfiles/schedule-log.txt"
        if os.path.exists(log_path):
            os.system(f'notepad.exe {log_path}')
#            os.system(r'python3 shedule-scanning.py 1')
        else:
            QMessageBox.critical(self, "Error", "The schedule scan log file does not exist.")

# SCANNING OPTIONS SECTIONS


    def run_complete_full_scan(self):
        self.status_text_edit.clear()
        self.hash_text_edit.clear()

        self.log("Running Full Computer Scan ...")

        root_directories = [
            os.path.expanduser("~"),  # Home directory
#            "C:\\", "D:\\" , "E:\\"                  # Drive C: (you can add more drives if needed)
             "Z:\\"
        ]

        self.status("Scanning for malicious files...\n")

        signature_hashes_md5 = set()
        signature_hashes_sha256 = set()
        with open("hashes/md5_hashes.txt", "r") as hash_file_md5, open("hashes/sha256_hashes.txt", "r") as hash_file_sha256:
            for line_md5, line_sha256 in zip(hash_file_md5, hash_file_sha256):
                signature_hashes_md5.add(line_md5.strip())
                signature_hashes_sha256.add(line_sha256.strip())

        virus_extensions = set()
        with open("hashes/virus-extensions.txt", "r") as ext_file:
            for line in ext_file:
                virus_extensions.add(line.strip())

        detected_malicious_files = []
        for root_directory in root_directories:
            detected_malicious_files.extend(self.scan_directory_recursive_for_full(root_directory, signature_hashes_md5, signature_hashes_sha256, virus_extensions))

        if detected_malicious_files:
            self.log("Detected malicious files:\n")
            self.hash_text_edit.insertPlainText("Hash Information:\n")
            for file_info in detected_malicious_files:
                file_path, checksum_md5, checksum_sha256, extension = file_info
                self.log(f"File: {file_path}, Extension: {extension}\n")
                self.hash_text_edit.insertPlainText(f"File: {file_path}\nMD5 Hash: {checksum_md5}\nSHA256 Hash: {checksum_sha256}\nExtension: {extension}\n\n")
                self.confirm_and_remove_file(file_path, os.path.basename(file_path))
            self.status("Malicious files detected. Review hash information.")
        else:
            self.log("No malicious files detected.\n")
            self.status("No malicious files detected.")

        self.log("\nFull Computer Scan completed.")
        self.hash_text_edit.verticalScrollBar().setValue(self.hash_text_edit.verticalScrollBar().maximum())


    def scan_directory_recursive_for_full(self, directory_path, signature_hashes_md5, signature_hashes_sha256, virus_extensions):
        detected_malicious_files = []

        for root, _, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                _, file_extension = os.path.splitext(filename)
                checksum_md5, checksum_sha256 = self.calculate_hashes(file_path)
                if checksum_md5 is not None and checksum_sha256 is not None:
                    if checksum_md5 in signature_hashes_md5 or checksum_sha256 in signature_hashes_sha256 or file_extension[1:] in virus_extensions:
                        detected_malicious_files.append((file_path, checksum_md5, checksum_sha256, file_extension))

        return detected_malicious_files

    ## Recursive Scanning Technique for Full Scan 

    def scan_directory_recursive(self, directory_path, signature_hashes_md5, signature_hashes_sha256, virus_extensions):
        detected_malicious_files = []

        for root, _, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                _, file_extension = os.path.splitext(filename)
                checksum_md5, checksum_sha256 = self.calculate_hashes(file_path)
                if checksum_md5 in signature_hashes_md5 or checksum_sha256 in signature_hashes_sha256 or file_extension[1:] in virus_extensions:
                    detected_malicious_files.append((file_path, checksum_md5, checksum_sha256, file_extension))

        return detected_malicious_files

### FULL MODULE FOR QUICK SCAN FUCK 

    def run_quick_scan(self):
        self.status_text_edit.clear()
        self.hash_text_edit.clear()

        self.log("Running Quick options ..\n")
        
        scan_type_dialog = ScanTypeDialog(self)
        result = scan_type_dialog.exec_()

        if result == QDialog.Accepted:
            selected_options = scan_type_dialog.get_selected_option()

            if selected_options == "recursive":
                self.run_recursive_quick_scan()
            elif selected_options == "non_recursive": 
                self.run_nonrecursive_quick_scan()
            else:
                self.log("No scan type Selected .. \n")
            
            self.log("\nQuick Scan Completed")
            self.hash_text_edit.verticalScrollBar().setValue(self.hash_text_edit.verticalScrollBar().maximum())


    def run_nonrecursive_quick_scan(self):
        self.status_text_edit.clear()
        self.hash_text_edit.clear()

        self.log("Running Quick Scan ...\n")
        self.status("Scanning for suspicious files ...\n")

        suspicious_files = []

## Implementing the non recursive scan 

        for directory in non_quick_to_directories_scan:
            if os.path.exists(directory):
                directory_path = directory  # Define directory_path here
                suspicious_files.extend(self.scan_directory_non_recursive(directory))
            else:
                self.log(f"Directory not found: {directory}\n")

        if suspicious_files:
            self.log("\nSuspicious files found:\n")
            self.hash_text_edit.insertPlainText("Hash Information:\n")
            malicious_file_paths = [os.path.join(directory_path, filename) for filename, _, _, _ in suspicious_files]  # Use directory_path here
            self.show_malicious_files(malicious_file_paths)  # Show malicious file paths

            for file_info in suspicious_files:
                filename, checksum_md5, checksum_sha256, extension = file_info
                full_file_path = os.path.join(directory_path, filename)  # Construct the full file path
                self.log(f"File: {filename}, Extension: {extension}\n")
                self.hash_text_edit.insertPlainText(f"File: {filename}\nMD5 Hash: {checksum_md5}\nSHA256 Hash: {checksum_sha256}\nExtension: {extension}\n\n")
                self.confirm_and_remove_file_quick(full_file_path)  # Pass the full file path
            self.status("Suspicious files detected. Review hash information.")
        else:
            self.log("No suspicious files found.\n")
            self.status("No suspicious files detected.")

        self.log("\nQuick Scan completed")
        self.hash_text_edit.verticalScrollBar().setValue(self.hash_text_edit.verticalScrollBar().maximum())
    def scan_directory_non_recursive(self, directory):
        print(f"Scanning directory: {directory}")
        found_files = []
        for root, _, files in os.walk(directory):
            for filename in files:
                _, extension = os.path.splitext(filename)
                if extension.lower() in suspicious_extensions:
                    print(f"Found suspicious file: {os.path.join(root, filename)}")
                    checksum_md5, checksum_sha256 = self.calculate_hashes(os.path.join(root, filename))
                    found_files.append((filename, checksum_md5, checksum_sha256, extension))

        return found_files

    def run_recursive_quick_scan(self):
        self.status_text_edit.clear()
        self.hash_text_edit.clear()

        # Define a helper function to log messages to both the GUI and the log file
        def log(message):
            self.status_text_edit.append(message)
            with open("logfiles/log-file-nonrecursive-quick-scan.txt", "a") as log_file:
                log_file.write(message)

        log("Running Quick Scan ...\n")
        self.status("Scanning for suspicious files ...\n")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log(f"Current Scanning Time: {current_time}\n")


        suspicious_files = []

        for directory in directories_to_scan:
            if os.path.exists(directory):
                directory_path = directory  # Define directory_path here
                suspicious_files.extend(self.scan_directory_recursive_for_quick(directory))
            else:
                log(f"Directory not found: {directory}\n")

        if suspicious_files:
            log("\nSuspicious files found:\n")
            self.hash_text_edit.insertPlainText("Hash Information:\n")

            for file_info in suspicious_files:
                file_path, checksum_md5, checksum_sha256 = file_info
                log(f"File: {file_path}\n")
                log(f"MD5 Hash: {checksum_md5}\n")
                log(f"SHA256 Hash: {checksum_sha256}\n")
                log("\n")

                # Append hash information to hash_text_edit
                self.hash_text_edit.append(f"File: {file_path}")
                self.hash_text_edit.append(f"MD5 Hash: {checksum_md5}")
                self.hash_text_edit.append(f"SHA256 Hash: {checksum_sha256}")
                self.hash_text_edit.append("")  # Add an empty line

                self.confirm_and_remove_file_quick(file_path)
            self.status("Suspicious files detected. Review hash information.")
        else:
            log("No suspicious files found.\n")
            self.status("No suspicious files detected.")

        log("\nQuick Scan completed.")
        self.hash_text_edit.verticalScrollBar().setValue(self.hash_text_edit.verticalScrollBar().maximum())

    def run_quick_scan_periodically(self, interval_minutes=10):
        while True:
            self.run_nonrecursive_quick_scan()  # Execute the quick scan function
            time.sleep(interval_minutes * 60)
            self.status_text_edit.clear()
            self.hash_text_edit.clear()

            with open("logfiles/log-file-nonrecursive-quick-scan.txt", "w") as log_file:
                def log(message):
                    self.log(message)
                    log_file.write(message)

                log("Running Quick Scan ... ---\n")
                self.status("Scanning for suspicious files ...\n")

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log(f"Current Scanning Time: {current_time}\n")


                suspicious_files = []

                for directory in non_quick_to_directories_scan:
                    if os.path.exists(directory):
                        directory_path = directory  # Define directory_path here
                        suspicious_files.extend(self.scan_directory_non_recursive(directory))
                    else:
                        log(f"Directory not found: {directory}\n")

                if suspicious_files:
                    log("\nSuspicious files found:\n")
                    self.hash_text_edit.insertPlainText("Hash Information:\n")
                    malicious_file_paths = [os.path.join(directory_path, filename) for filename, _, _, _ in suspicious_files]  # Use directory_path here
                    self.show_malicious_files(malicious_file_paths)  # Show malicious file paths

                    for file_info in suspicious_files:
                        filename, checksum_md5, checksum_sha256, extension = file_info
                        full_file_path = os.path.join(directory_path, filename)  # Construct the full file path
                        log(f"File: {filename}, Extension: {extension}\n")
                        self.hash_text_edit.insertPlainText(f"File: {filename}\nMD5 Hash: {checksum_md5}\nSHA256 Hash: {checksum_sha256}\nExtension: {extension}\n\n")
                        self.confirm_and_remove_file_quick(full_file_path)  # Pass the full file path
                    self.status("Suspicious files detected. Review hash information.")
                else:
                    log("No suspicious files found.\n")
                    self.status("No suspicious files detected.")

                log("\nQuick Scan completed.")
                self.hash_text_edit.verticalScrollBar().setValue(self.hash_text_edit.verticalScrollBar().maximum())


    def scan_directory_recursive_for_quick(self, directory_path):
        detected_suspicious_files = []

        signature_hashes_md5 = set()
        signature_hashes_sha256 = set()
        with open("hashes/md5_hashes.txt", "r") as hash_file_md5, open("hashes/sha256_hashes.txt", "r") as hash_file_sha256:
            for line_md5, line_sha256 in zip(hash_file_md5, hash_file_sha256):
                signature_hashes_md5.add(line_md5.strip())
                signature_hashes_sha256.add(line_sha256.strip())

        virus_extensions = set()
        with open("hashes/virus-extensions.txt", "r") as ext_file:
            for line in ext_file:
                virus_extensions.add(line.strip())

        for root, _, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)
                _, file_extension = os.path.splitext(filename)
                checksum_md5, checksum_sha256 = self.calculate_hashes(file_path)
                if checksum_md5 in signature_hashes_md5 or checksum_sha256 in signature_hashes_sha256 or file_extension[1:] in virus_extensions:
                    detected_suspicious_files.append((file_path, checksum_md5, checksum_sha256))

        return detected_suspicious_files


    def confirm_and_remove_file_quick(self, full_file_path):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Suspicious File Detected")
        msg_box.setText(f"Suspicious file detected:\n{full_file_path}\nDo you want to delete it?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        result = msg_box.exec_()

        if result == QMessageBox.Yes:
            try:
                # Convert the path to the appropriate format for the operating system
                file_path = os.path.normpath(file_path)
                print(file_path)
                os.remove(file_path)  # Delete the file
                self.log(f"File removed: {file_path}\n")
            except Exception as e:
                self.log(f"Error removing {file_path}: {e}\n")
        else:
            self.log(f"Deletion of {file_path} canceled by user.\n")


    def scan_directory(self, directory, suspicious_extensions):
        print(f"Scanning directory: {directory}")
        found_files = []
        for root, _, files in os.walk(directory):
            for filename in files:
                _, extension = os.path.splitext(filename)
                if extension.lower() in suspicious_extensions:
                    print(f"Found suspicious file: {os.path.join(root, filename)}")
                    checksum_md5, checksum_sha256 = self.calculate_hashes(os.path.join(root, filename))
                    found_files.append((filename, checksum_md5, checksum_sha256, extension))

        return found_files

    def status(self, message):
        self.status_text_edit.insertPlainText(message)
        self.status_text_edit.verticalScrollBar().setValue(self.status_text_edit.verticalScrollBar().maximum())

    def log(self, message):
        self.status_text_edit.insertPlainText(message)
        self.status_text_edit.verticalScrollBar().setValue(self.status_text_edit.verticalScrollBar().maximum())

### Function to Remove file for Quick scan 

    def confirm_and_remove_file_quick(self, file_path):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Suspicious File Detected")
        msg_box.setText(f"Suspicious file detected:\n{file_path}\nDo you want to delete it?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        result = msg_box.exec_()

        if result == QMessageBox.Yes:
            try:
                # Use PowerShell to remove the file with elevated permissions21
                subprocess.run(['powershell', '-command', f'Remove-Item -Path "{file_path}" -Force -Confirm:$false'], check=True)
                self.log(f"File removed: {file_path}\n")
            except subprocess.CalledProcessError as e:
                self.log(f"Error removing {file_path}: {e}\n")
        else:
            self.log(f"Deletion of {file_path} canceled by user.\n")


### Function to delete Malicious file detected by Full Scan !

    def confirm_and_remove_file(self, file_path, filename):
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Suspicious File Detected")
        msg_box.setText(f"Suspicious file detected:\n{file_path}\nDo you want to delete it?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        result = msg_box.exec_()

        if result == QMessageBox.Yes:
            try:
                # Convert the path to the appropriate format for the operating system
                file_path = os.path.normpath(file_path)
                os.remove(file_path)  # Delete the file
                self.log(f"File removed: {file_path}\n")
            except Exception as e:
                self.log(f"Error removing {file_path}: {e}\n")
        else:
            self.log(f"Deletion of {file_path} canceled by user.\n")


    def calculate_checksum(file_path, hash_algorithm="md5", chunk_size=8192):
        hash_func = hashlib.new(hash_algorithm)
        with open(file_path, "rb") as file:
            while chunk := file.read(chunk_size):
                hash_func.update(chunk)
            return hash_func.hexdigest()
        

    def delete_temp_files(self):
        self.log("Deleting temporary files and folders...\n")

        temp_dir = tempfile.gettempdir()  
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path) 
                    self.log(f"Deleted file: {file_path}\n")
                except Exception as e:
                    self.log(f"Error deleting file: {file_path}, Error: {e}\n")

            for dir in dirs:
                dir_path = os.path.join(root, dir)
                try:
                    shutil.rmtree(dir_path) 
                    self.log(f"Deleted folder: {dir_path}\n")
                except Exception as e:
                    self.log(f"Error deleting folder: {dir_path}, Error: {e}\n")

        self.log("Cleanup completed.\n")

### Update Function

## $ COMING SOON ..$ ##


if __name__ == "__main__":

#    run_as_admin()
    app = QApplication([])
    
   # login_app = LoginWindow()
   # login_app.show()
   # app.exec_()
    
  #  app = QApplication(sys.argv)
 #   password_auth()


    suspicious_extensions = set()
    with open('hashes/virus-extensions.txt', 'r') as ext_file:
        for line in ext_file:
            suspicious_extensions.add(line.strip().lower())
    
    # DIRECTORY PATH FOR QUICK SCAN 

    directories_to_scan = [

        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp'),
   #    os.path.join(os.environ['USERPROFILE'], 'Desktop'),
        os.path.join(os.environ['USERPROFILE'], 'Pictures'),
        os.path.join(os.environ['USERPROFILE'], 'Music'),
   #    os.path.join(os.environ['USERPROFILE'], 'Downloads'),
        os.path.join(os.environ['USERPROFILE'], 'Documents'),
        os.path.join('C:\Windows\Temp')
        ]

    non_quick_to_directories_scan = [
        os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp'),
      #  os.path.join(os.environ['USERPROFILE'], 'Downloads'),
        os.path.join(os.environ['USERPROFILE'], 'Documents'),
      #  os.path.join(os.environ['USERPROFILE'], 'Desktop'),
        os.path.join(os.environ['USERPROFILE'], 'Pictures'),
      #  os.path.join(os.environ['USERPROFILE'], 'Music'),
        os.path.join('C', 'Windows', 'Temp')
    ]

    virus_extensions = set()
    with open("hashes/virus-extensions.txt", "r") as ext_file:
        for line in ext_file:
            virus_extensions.add(line.strip()) 
    
    antivirus_app = AntivirusUI()
    sys.exit(app.exec_())

