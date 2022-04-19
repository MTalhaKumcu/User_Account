import sys
import sqlite3
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):

        super().__init__()

        self.connect_creat()

        self.init_ui()

    def connect_creat(self):

        connection = sqlite3.connect("database.db")
        self.cursor = connection.cursor()
        self.cursor.execute("Create Table If not exists subscribers (user_name TEXT,password TEXT)")
        connection.commit()
    def init_ui(self):
        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Login =  QtWidgets.QPushButton(" LOGIN ")
        self.text_area = QtWidgets.QLabel("")

        #vertical box

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.text_area)
        v_box.addStretch()
        v_box.addWidget(self.Login)
        #horizontal box
        h_box= QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle(" Login ")
        self.Login.clicked.connect(self.login)

        self.show()
    def login(self):
        name =self.user_name.text()
        pas =self.password.text()

        self.cursor.execute("Select * From subscribers where user_name = ? and password = ?",(name,pas))
        data = self.cursor.fetchall()
        if len(data) == 0:
            self.text_area.setText("Has no users \n please try again... ")
        else:
             self.text_area.setText("Welcome "+name)


app = QtWidgets.QApplication(sys.argv)
pencere = Window()
sys.exit(app.exec_())