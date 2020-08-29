# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_person.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from PyQt5.QtGui import QImage
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


class Ui_Dialog(object):
    def __init__(self):
        self.socket = None
        self.picture = 0
        self.id = ""
        self.friend_title = ""
        self.file_path = ""
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setMaximumSize(QtCore.QSize(400, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_source/image/myicon_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 30))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(150, 5, 100, 20))
        self.label.setStyleSheet("font: 12pt \"Agency FB\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(365, 0, 35, 25))
        self.pushButton_close.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_hide = QtWidgets.QPushButton(self.frame)
        self.pushButton_hide.setGeometry(QtCore.QRect(330, 0, 35, 25))
        self.pushButton_hide.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 260, 380, 90))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 40, 380, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setGeometry(QtCore.QRect(50, 360, 60, 30))
        self.pushButton_cancel.setStyleSheet("background-color: rgb(255, 255, 230);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_send = QtWidgets.QPushButton(Dialog)
        self.pushButton_send.setGeometry(QtCore.QRect(290, 360, 60, 30))
        self.pushButton_send.setStyleSheet("background-color: rgb(255, 255, 230);\n"
"color: rgb(0,0, 0);")
        self.pushButton_send.setObjectName("pushButton_send")
        
        self.pushButton_file = QtWidgets.QPushButton(Dialog)
        self.pushButton_file.setGeometry(QtCore.QRect(10, 350, 20, 10))
        self.pushButton_file.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.pushButton_file.setObjectName("pushButton_file")
        
        
        self.retranslateUi(Dialog)
        self.pushButton_close.clicked.connect(Dialog.close)
        self.pushButton_hide.clicked.connect(Dialog.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "聊天"))
        self.label.setText(_translate("Dialog", "刘畅"))
        self.pushButton_close.setText(_translate("Dialog", "关闭"))
        self.pushButton_hide.setText(_translate("Dialog", "隐藏"))
        self.pushButton_cancel.setText(_translate("Dialog", "关闭"))
        self.pushButton_send.setText(_translate("Dialog", "发送"))
        self.pushButton_file.setText(_translate("MainWindow", "图片"))
        self.pushButton_file.clicked.connect(self.file_send)
# import frist_rc
    
    
    def file_send(self):
        root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
        root.withdraw()       # 将Tkinter.Tk()实例隐藏
        default_dir = r"文件路径"
        file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
        self.file_path = file_path
        self.picture = 1
        
        
        print('client filepath: {0}'.format(file_path))
        we_text = ['single_person']
        we_text.append(self.id)
        we_text.append(self.friend_title)
        
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
            QtWidgets.QMessageBox.information(self.MainWindow, '警告', '输入消息为空！', 
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close, QtWidgets.QMessageBox.Close)
    
    def infor_send(self, s, sendname, recvname):
        self.socket = s
        self.id = sendname
        self.friend_title = recvname
        def send():
            if self.picture == 1:
            #自己显示
                we_text = ['single_person']
                we_text.append(self.id)
                we_text.append(self.friend_title)
                self_mess = str(we_text[1])+":"
                self.textBrowser.append(self_mess + "\n")
            
                path = "<img src=\"" + self.file_path + "\" />"
                self.textBrowser.insertHtml(path)
                
            #发送给对方
                fhead = struct.pack(b'128sl', bytes(os.path.basename(self.file_path), encoding='utf-8'), os.stat(self.file_path).st_size)
                self.socket.send(fhead)
                fp = open(self.file_path, 'rb')
                while 1:
                    data = fp.read(1024)
                    if not data:
                        print('{0} file send over...'.format(self.file_path))
                        break
                    self.socket.send(data)
                self.textEdit.clear()
                self.picture = 0
            else:
                send_list = ['single_person']
                send_list.append(sendname)
                send_list.append(recvname)
                sendtext = self.textEdit.toPlainText()
                #print(sendtext)
                if sendtext != '':
                    send_list.append(sendtext)
                    textsend = '*'.join(send_list)
                    print('single发送出去' + textsend)
                    s.send(textsend.encode())
                self.textEdit.clear()
                self_mess = str(send_list[1])+":"+str(send_list[3])
                self.textBrowser.append(self_mess + "\n")
        self.pushButton_send.clicked.connect(send)

    def recv_thread(self, s):
        buffsize = 1024
        def recv():
            while True:
                recvtext = s.recv(buffsize).decode('utf-8')
                recvdata = recvtext.split('*')
                print('single接收到' + str(recvdata))
                if recvdata[0] == "file":
                    fileinfo_size = struct.calcsize('128sl')
                    buf = s.recv(fileinfo_size)
                    if buf:
                        filename, filesize = struct.unpack('128sl', buf)
                        fn = filename.decode().strip('\x00')
                        new_filename = os.path.join('./downloads', fn)

                        recvd_size = 0
                        fp = open(new_filename, 'wb')

                        while not recvd_size == filesize:
                            if filesize - recvd_size > 1024:
                                data = s.recv(1024)
                                recvd_size += len(data)
                            else:
                                data = s.recv(1024)
                                recvd_size = filesize
                            fp.write(data)
                        fp.close()
                    self.textBrowser.append(recvdata[1] + "\n")
                    path = "<img src=\"" + new_filename + "\" />"
                    self.textBrowser.insertHtml(path)
                else:
                    self.textBrowser.append(recvdata[0] + "\n")
                    #print(recvdata[0])
        self.re = threading.Thread(target=recv)  # 创建线程
        self.re.start()

    def quit(self, Dlog):
        def quit():
            stop_thread(self.re)
            print('关闭了single对话框')
            Dlog.close()
        self.pushButton_cancel.clicked.connect(quit)
