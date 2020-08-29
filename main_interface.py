# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_interface.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from socket import *
import group
import single_person
from Dialog_add import Ui_Dialog

widget_group = QtWidgets.QMainWindow()
ui_group = group.Ui_MainWindow()
ui_group.setupUi(widget_group)
child = QtWidgets.QDialog()
child_ui = single_person.Ui_Dialog()
child_ui.setupUi(child)

Diaaddw = QtWidgets.QWidget()
Diaadd = Ui_Dialog()
Diaadd.setupUi(Diaaddw)

class Ui_MainWindowt(object):
    def __init__(self, my_socket):
        self.my_socket = my_socket
        self.buffsize = 1024

    def setupUit(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(300, 400)
        self.MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        self.MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/myicon_1.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 300, 100))
        self.frame.setStyleSheet("background-color: rgb(255, 0, 127);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 70, 100, 30))
        self.label.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(250, 0, 50, 30))
        self.pushButton_close.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_hide = QtWidgets.QPushButton(self.frame)
        self.pushButton_hide.setGeometry(QtCore.QRect(200, 0, 50, 30))
        self.pushButton_hide.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 85, 255);")
        self.pushButton_hide.setObjectName("pushButton_hide")
        #self.frame_2 = QtWidgets.QFrame(self.frame)
        #self.frame_2.setGeometry(QtCore.QRect(120, 8, 60, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        #self.frame_2.setSizePolicy(sizePolicy)
        #self.frame_2.setStyleSheet("background-image:url(image/Icon_head.png)")
        #self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        #self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        #self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 100, 300, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_friend = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_friend.setGeometry(QtCore.QRect(0, 0, 150, 40))
        self.pushButton_friend.setStyleSheet("background-color: rgb(255, 239, 239);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main_source/image/contact_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_friend.setIcon(icon1)
        self.pushButton_friend.setIconSize(QtCore.QSize(60, 40))
        self.pushButton_friend.setObjectName("pushButton_friend")
        self.pushButton_group = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_group.setGeometry(QtCore.QRect(150, 0, 150, 40))
        self.pushButton_group.setStyleSheet("background-color: rgb(255, 248, 248);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/main_source/image/wechat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_group.setIcon(icon2)
        self.pushButton_group.setIconSize(QtCore.QSize(60, 40))
        self.pushButton_group.setObjectName("pushButton_group")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 140, 300, 260))
        self.listWidget.setIconSize(QtCore.QSize(45, 45))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/main_source/image/Icon_user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        item.setIcon(icon3)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon3)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        #icon4.addPixmap(QtGui.QPixmap("image/partjob.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        item.setIcon(icon4)
        self.listWidget.addItem(item)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(0, 140, 300, 260))
        self.treeWidget.setAutoScrollMargin(10)
        self.treeWidget.setIconSize(QtCore.QSize(40, 40))
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setIndentation(6)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.treeWidget.headerItem().setFont(0, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setToolTip(0, "")
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("image/Icon_logger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon5)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1.setIcon(0, icon5)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        item_0.setFont(0, font)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        font = QtGui.QFont()
        font.setPointSize(10)
        item_1.setFont(0, font)
        item_1.setIcon(0, icon5)
        '''
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        '''
        # self.setCentralWidget(self.treeWidget)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.menuEvent)
        # MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close)
        self.pushButton_friend.clicked.connect(self.listWidget.hide)
        self.pushButton_group.clicked.connect(self.listWidget.show)
        self.pushButton_friend.clicked.connect(self.treeWidget.show)
        self.pushButton_group.clicked.connect(self.treeWidget.hide)
        self.pushButton_hide.clicked.connect(MainWindow.showMinimized)

        self.listWidget.itemClicked.connect(self.group_req)
        self.treeWidget.itemClicked.connect(self.single_person_req)
        self.pushButton_close.clicked.connect(self.quit_line)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "局域网通讯工具"))
        self.label.setText(_translate("MainWindow", "2062683161"))
        self.pushButton_close.setText(_translate("MainWindow", "关闭"))
        self.pushButton_hide.setText(_translate("MainWindow", "隐藏"))
        self.pushButton_friend.setText(_translate("MainWindow", "好友"))
        self.pushButton_group.setText(_translate("MainWindow", "群聊"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "信息安全专业群"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "信息安全学习群"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "兼职群"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "联系人"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "老师"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "2062683162"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "2062683163"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "同学"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "2062683161"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        
# import frist_rc

    def menuEvent(self):
        #右键点击分组，触发添加分组和添加好友的界面
        treeText = self.treeWidget.currentItem().text(0)
        if treeText == '老师' or treeText == '同学':
            my_menu = QtWidgets.QMenu(self.MainWindow)
            '''
            group_add_action = QtWidgets.QAction('添加分组', my_menu)
            my_menu.addAction(group_add_action)
            group_add_action.triggered.connect(self.group_add)
            '''
            friend_add_action = QtWidgets.QAction('添加好友', my_menu)
            my_menu.addAction(friend_add_action)
            friend_add_action.triggered.connect(self.friend_add)
            my_menu.exec_(QtGui.QCursor.pos())
        else:
            my_menu2 = QtWidgets.QMenu(self.MainWindow)
            friend_remove_action = QtWidgets.QAction('删除', my_menu2)
            my_menu2.addAction(friend_remove_action)
            friend_remove_action.triggered.connect(self.friend_remove)
            my_menu2.exec_(QtGui.QCursor.pos())
        return

    def group_req(self, item):
        #群聊
        group_title = item.text()
        id = self.label.text()
        group_chat = ['group_chat']
        group_chat.append(group_title)
        group_chat.append(id)
        group_chat = '*'.join(group_chat)
        self.my_socket.send(group_chat.encode('utf-8'))
        self.group_recv(item)
        return

    def single_person_req(self, item):
        #显示对话框
        id = self.label.text()
        friend_title = item.text(0)
        if friend_title != '老师' and friend_title != '同学':
            child.show()
            child_ui.label.setText(friend_title)
            child_ui.recv_thread(self.my_socket)
            child_ui.infor_send(self.my_socket, id, friend_title)
            child_ui.quit(child)
            child_ui.textBrowser.clear()
        return

    def group_recv(self, item):
        #显示对话框
        group_title = item.text()
        id = self.label.text()
        item = QtWidgets.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("image/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        item.setText(str(id))
        #ui_group.listWidget.addItem(item)
        widget_group.show()
        ui_group.textBrowser.clear()
        ui_group.label_2.setText(group_title)
        #ui_group.textBrowser.append("欢迎" + id + "\n")
        ui_group.recv_thread(self.my_socket)
        ui_group.infor_send(self.my_socket, group_title, id)
        ui_group.infor_quit(widget_group)
        return

    def group_add(self):
        #添加分组
        Diaaddw.show()
        Diaaddw.setWindowTitle("添加分组")
        Diaadd.label.setText("新组名：")

        def gettext():
            groupname = Diaadd.lineEdit.text()
            if groupname != '':
                root5 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                root5.setText(0, groupname)
                self.treeWidget.addTopLevelItem(root5)
                Diaaddw.close()
            else:
                QtWidgets.QMessageBox.information(self.MainWindow, '提示', '组名不能为空!',
                                                  QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                  QtWidgets.QMessageBox.Close)

        Diaadd.pushButton.clicked.connect(gettext)
        return

    def friend_add(self):
        #添加好友
        selectroot = self.treeWidget.currentItem()
        Diaaddw.show()
        Diaaddw.setWindowTitle("添加好友")
        Diaadd.label.setText("好友名：")

        def gettext():
            friend_name = Diaadd.lineEdit.text()
            if friend_name != '':
                root5 = QtWidgets.QTreeWidgetItem(selectroot)
                root5.setText(0, friend_name)
                font = QtGui.QFont()
                font.setPointSize(10)
                root5.setFont(0, font)
                icon6 = QtGui.QIcon()
                icon6.addPixmap(QtGui.QPixmap("image/Icon_logger.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                root5.setIcon(0, icon6)
                Diaaddw.close()
            else:
                QtWidgets.QMessageBox.information(self.MainWindow, '提示', '好友名不能为空!',
                                                  QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Close,
                                                  QtWidgets.QMessageBox.Close)

        Diaadd.pushButton.clicked.connect(gettext)
        return

    def friend_remove(self):
        #删除好友
        try:
            # 尝试删除子节点（通过其父节点，调用removeChild函数进行删除）
            currNode = self.treeWidget.currentItem()
            parent1 = currNode.parent()
            parent1.removeChild(currNode)
        except Exception:
            # 遇到异常时删除根节点
            try:
                rootIndex = self.treeWidget.indexOfTopLevelItem(currNode)
                self.treeWidget.takeTopLevelItem(rootIndex)
            except Exception:
                print(Exception)
        '''
        self.treeWidget.currentItem().setText(0, ' ')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(""), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.treeWidget.currentItem().setIcon(0, icon)
        '''
        return
        
    def quit_line(self):
        quit_mess = ['quit']
        id = self.label.text()
        quit_mess.append(id)
        quit_mess = ' '.join(quit_mess)
        self.my_socket.send(quit_mess.encode('utf-8'))
        return
