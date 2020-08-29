# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
import threading
from tkinter import *
import tkinter.filedialog
import os
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import QUrl
import sys
import struct
import inspect
import ctypes
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


class Ui_MainWindow(object):
    def __init__(self):
        self.socket = None
        self.picture = 0
        self.id = ""
        self.group_title = ""
        self.file_path = ""
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_source/image/myicon_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.frame = QtWidgets.QFrame(self.centralwidget)
        #self.frame.setGeometry(QtCore.QRect(0, 0, 100, 500))
        #self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.frame.setObjectName("frame")
        #self.listWidget = QtWidgets.QListWidget(self.frame)
        #self.listWidget.setGeometry(QtCore.QRect(0, 50, 100, 450))
        #self.listWidget.setIconSize(QtCore.QSize(40, 40))
        #self.listWidget.setGridSize(QtCore.QSize(40, 40))
        #self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main_source/image/Icon_logger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        #self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon1)
        #self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon1)
        #self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon1)
        #self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon1)
        #self.listWidget.addItem(item)
        #self.label = QtWidgets.QLabel(self.frame)
        #self.label.setGeometry(QtCore.QRect(0, 10, 100, 31))
        #self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 30, 400, 370))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 380, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 230, 380, 90))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(290, 330, 60, 30))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 330, 60, 30))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        
        self.pushButton_file = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_file.setGeometry(QtCore.QRect(10, 320, 20, 10))
        self.pushButton_file.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_file.setObjectName("pushButton_file")
        
        
        
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 400, 30))
        self.frame_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(150, 5, 100, 20))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QQ群聊"))
        #__sortingEnabled = self.listWidget.isSortingEnabled()
        #self.listWidget.setSortingEnabled(False)
        '''item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "2062683161"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "2062683162"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "2062683163"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "2062683164"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "2062683165"))
        '''
        #self.listWidget.setSortingEnabled(__sortingEnabled)
        #self.label.setText(_translate("MainWindow", "群聊人员："))
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.pushButton_file.setText(_translate("MainWindow", "图片"))
        self.pushButton_file.clicked.connect(self.file_send)
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">TCP群聊</span></p></body></html>"))
# import frist_rc
    
    def file_send(self):
        root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
        root.withdraw()       # 将Tkinter.Tk()实例隐藏
        default_dir = r"文件路径"
        file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
        self.file_path = file_path
        self.picture = 1
        
        
        print('client filepath: {0}'.format(file_path))
        we_text = ['group']
        we_text.append(self.group_title)
        we_text.append(self.id)
        text = "file"
        if text != '':
            we_text.append(text)
            we_text_str = '*'.join(we_text)
            self.socket.send(we_text_str.encode('utf-8'))
            '''
            self_mess = str(we_text[2]) + ":"
            self.textBrowser.append(self_mess + "\n")
            '''
            image = QImage(file_path)
            cursor = self.textEdit.textCursor()
            document = self.textEdit.document()
            document.addResource(QTextDocument.ImageResource, QUrl("image"), image)
            self.textEdit.setText(file_path)
            cursor.insertImage("image")
            path = "<img src=\"" + file_path + "\" />"
            
            
        else:
            QtWidgets.QMessageBox.information(self.MainWindow, '警告', '输入消息为空！', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Close)
    
    def recv_thread(self, my_socket):
        buffsize = 1024
        def recv():
            while True:
                recvdata = my_socket.recv(buffsize).decode('utf-8')
                recvdata = recvdata.split('*')
                print('group接收到：' + str(recvdata))
                if recvdata[0] == "file":
                    fileinfo_size = struct.calcsize('128sl')
                    buf = my_socket.recv(fileinfo_size)
                    if buf:
                        filename, filesize = struct.unpack('128sl', buf)
                        fn = filename.decode().strip('\x00')
                        new_filename = os.path.join('./downloads', fn)

                        recvd_size = 0
                        fp = open(new_filename, 'wb')

                        while not recvd_size == filesize:
                            if filesize - recvd_size > 1024:
                                data = my_socket.recv(1024)
                                recvd_size += len(data)
                            else:
                                data = my_socket.recv(1024)
                                recvd_size = filesize
                            fp.write(data)
                        fp.close()
                    self.textBrowser.append(recvdata[1] + "\n")
                    path = "<img src=\"" + new_filename + "\" />"
                    self.textBrowser.insertHtml(path)
                else:
                    self.textBrowser.append(recvdata[0] + "\n")
        self.re = threading.Thread(target=recv)  # 创建线程
        self.re.start()

    def infor_send(self, my_socket, group_title, id):
        self.socket = my_socket
        self.id = id
        self.group_title = group_title
        def send():
            if self.picture == 1:
                '''
                we_text = ['group']
                we_text.append(self.group_title)
                we_text.append(self.id)
                self_mess = str(we_text[2])+":"
                self.textBrowser.append(self_mess + "\n")
            
                path = "<img src=\"" + self.file_path + "\" />"
                self.textBrowser.insertHtml(path)
                '''
                fhead = struct.pack(b'128sl', bytes(os.path.basename(self.file_path), encoding='utf-8'), os.stat(self.file_path).st_size)
                self.socket.send(fhead)
                fp = open(self.file_path, 'rb')
                while 1:
                    data = fp.read(1024)
                    if not data:
                        print('{0} file send over...'.format(self.file_path))
                        break
                    my_socket.send(data)
                self.textEdit.clear()
                self.picture = 0
            else:
                we_text = ['group']
                we_text.append(group_title)
                we_text.append(id)
                text = self.textEdit.toPlainText()
                if text != '':
                    we_text.append(text)
                    we_text_str = '*'.join(we_text)
                    print('group发送出去：' + we_text_str)
                    my_socket.send(we_text_str.encode('utf-8'))
                    self_mess = str(we_text[1])+":"+str(we_text[3])
                    #self.textBrowser.append(self_mess + "\n")
                else:
                    QtWidgets.QMessageBox.information(self.MainWindow, '警告', '输入消息为空！', QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Close)
                self.textEdit.clear()
        self.pushButton.clicked.connect(send)

    def infor_quit(self, ui2):
        def quit():
            stop_thread(self.re)
            print('关闭了group对话框')
            ui2.close()
            
        self.pushButton_2.clicked.connect(quit)