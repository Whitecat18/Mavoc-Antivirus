from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap
import sys

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
        pixmap = QPixmap("mavoc_banner.jpg")
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

    def show_wrong_password_message(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Wrong Password")
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setText("Incorrect password. Please try again.")
        msg_box.setFixedSize(300, 150)
        msg_box.exec_()