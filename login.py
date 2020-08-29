# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import threading
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(400, 350)
        self.MainWindow.setMinimumSize(QtCore.QSize(360, 350))
        self.MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/myicon_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_id = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_id.setGeometry(QtCore.QRect(120, 150, 191, 30))
        self.lineEdit_id.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lineEdit_id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_id.setText("2062683161")
        self.lineEdit_id.setMaxLength(32767)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pass.setGeometry(QtCore.QRect(120, 210, 191, 31))
        self.lineEdit_pass.setInputMask("")
        self.lineEdit_pass.setText("123456")
        self.lineEdit_pass.setMaxLength(32767)
        self.lineEdit_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pass.setCursorPosition(0)
        self.lineEdit_pass.setObjectName("lineEdit_pass")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 250, 221, 41))
        self.pushButton.setStyleSheet("background-color: rgb(7, 85, 240);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 150, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 51, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 261, 41))
        self.label_3.setLineWidth(1)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 71, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_ipAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ipAddress.setGeometry(QtCore.QRect(80, 70, 141, 31))
        self.lineEdit_ipAddress.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lineEdit_ipAddress.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_ipAddress.setText("127.0.0.1")
        self.lineEdit_ipAddress.setMaxLength(32767)
        self.lineEdit_ipAddress.setObjectName("lineEdit_ipAddress")
        self.lineEdit_port = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_port.setGeometry(QtCore.QRect(300, 70, 71, 30))
        self.lineEdit_port.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.lineEdit_port.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_port.setText("6337")
        self.lineEdit_port.setMaxLength(32767)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 70, 41, 31))
        self.label_5.setObjectName("label_5")
        self.regist = QtWidgets.QLabel(self.centralwidget)
        self.regist.setGeometry(QtCore.QRect(160, 300, 200, 20))
        self.regist.setStyleSheet("")
        self.regist.setObjectName("regist")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "登录"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "账号："))
        self.label_2.setText(_translate("MainWindow", "密码："))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">局域网实时通讯工具</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "address:"))
        self.label_5.setText(_translate("MainWindow", "port:"))
        self.regist.setText(_translate("MainWindow", "<html><head/><body><p>注册账号：<a href=\"127.0.0.1/regsit.html\"><span style=\" text-decoration: underline; color:#0000ff;\">点击注册</span></a></p></body></html>"))

    def login(self):
        #连接
        ipAddress = self.lineEdit_ipAddress.text()
        port = int(self.lineEdit_port.text())
        self.socket_connect(ipAddress, port)

        #第一次检查账号密码格式
        debug_message = ['login']
        self.id = self.lineEdit_id.text()
        self.password = self.lineEdit_pass.text()
        password_length = len(str(self.password))
        if self.id == '':
            QMessageBox.information(self.MainWindow, '提示您', '账号不可为空',
                                    QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        elif password_length < 5 or password_length > 10:
            QMessageBox.information(self.MainWindow, '提示您', '账号长度不对',
                                    QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        else:
            if self.password == '':
                QMessageBox.information(self.MainWindow, '提示您', '口令不可为空',
                                        QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            else:
                debug_message.append(self.id)
                debug_message.append(self.password)
                debug_message = '*'.join(debug_message)
                #使用空格间隔每个元素
                print(debug_message)
                self.my_socket.send(str(debug_message).encode('utf-8'))
                self.return_mess()
        return

    def socket_connect(self, ipAddress, port):
        #连接socket
        self.buffsize = 1024
        self.my_socket = socket(AF_INET, SOCK_STREAM)
        self.my_socket.connect((ipAddress, port))
        return

    def return_mess(self):
        recv_message = self.my_socket.recv(self.buffsize).decode('utf-8')
        print(recv_message)
        if str(recv_message) == 'OK':

            ui_main.my_socket = self.my_socket
            #widget_main.exec_()

            QMessageBox.information(self.MainWindow, 'success', '您成功登陆',
                                    QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
            widget_login.hide()
            #print('login_hide')
            widget_main.show()
            #print('main_show')
            ui_main.label.setText(self.id)
        elif str(recv_message) == 'error_id':
            QMessageBox.information(self.MainWindow, 'fail', '这个账号不存在',
                                    QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        elif str(recv_message) == 'error_password':
            QMessageBox.information(self.MainWindow, 'fail', '口令错误',
                                    QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        elif str(recv_message) == 'error_login':
            QMessageBox.information(self.MainWindow, 'fail', '这个账号已经登陆',
                                    QMessageBox.Ok | QMessageBox.Close, QMessageBox.Close)
        return


if __name__ == "__main__":

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    widget_login = QtWidgets.QMainWindow()
    ui_login = Ui_MainWindow()
    ui_login.setupUi(widget_login)
    widget_login.show()
    import main_interface
    widget_main = QtWidgets.QWidget()
    my_socket = socket(AF_INET, SOCK_STREAM)
    ui_main = main_interface.Ui_MainWindowt(my_socket)
    ui_main.setupUit(widget_main)
    sys.exit(app.exec_())