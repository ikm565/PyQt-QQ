#-*-coding:utf-8-*-
'''
login_data:
(1)[group_chat, group_title, id]
(2)[group, group_title, id, text]
(3)[single_person, end_name, recv_name, text]
(4)[login, id, password]
'''

from socket import *
import threading
import pymysql
import os
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


db = pymysql.connect("localhost", "root", "root", "liuchang")
cursor = db.cursor()
sql = 'select * from simple'

try:
    cursor.execute(sql)
    result = cursor.fetchall()
    
except:
    print('error: cant fetch data ')

address='127.0.0.1'
port = 6337
buffsize = 1024
s = socket(AF_INET, SOCK_STREAM)
s.bind((address, port))
s.listen(10)     #最大连接数

client_list = []

user_list = []
for i in result:
    user_list.append([i[1], i[2]])
print(user_list)
user_l = len(user_list)
user_client = []
thread_list = []
group_list = [['信息安全专业群'], ['信息安全学习群'], ['兼职群']]

def login(logindata, clientsock):

    for x in range(0, user_l):
        print("登录请求"+str(logindata[1]))
        if len(user_client)>=1:
            ul=len(user_client)

            if str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])!=str(logindata[2]):
                login_bkinfo = 'error_password'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])==str(logindata[2]):
                for user_cl in range(0, ul):
                    if str(user_client[user_cl][0]) == str(logindata[1]):
                        login_bkinfo = 'error_login'
                        clientsock.send(login_bkinfo.encode())
                        break
                    elif user_cl == ul - 1:
                        usercl=[]
                        usercl.append(logindata[1])
                        usercl.append(clientsock)
                        login_bkinfo = 'OK'
                        user_client.append(usercl)
                        #print(user_client)
                        clientsock.send(login_bkinfo.encode())
                break
            elif x==user_l-1:
                login_bkinfo = 'error_id'
                clientsock.send(login_bkinfo.encode())

        else:

            if str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])!=str(logindata[2]):
                login_bkinfo = 'error_password'
                clientsock.send(login_bkinfo.encode())
                break
            elif str(user_list[x][0])==str(logindata[1]) and str(user_list[x][1])==str(logindata[2]):
                usercl=[]
                usercl.append(logindata[1])
                usercl.append(clientsock)
                login_bkinfo = 'OK'
                user_client.append(usercl)
                #print(user_client)
                clientsock.send(login_bkinfo.encode())
                break
            elif x==user_l-1:
                login_bkinfo = 'error_id'
                clientsock.send(login_bkinfo.encode())






def tcplink(clientsock, clientaddress):
    group_l = len(group_list)
    while True:
        recvdata = clientsock.recv(buffsize).decode('utf-8')
        logindata = recvdata.split('*')
        print(logindata)
        if str(logindata[0]) == 'login':
            login(logindata, clientsock)

        elif str(logindata[0]) == 'group_chat':
            #reqci=1
            for y in range(0, group_l):
                if str(group_list[y][0]) == str(logindata[1]):
                    requser=str(logindata[2])+' '+'加入'
                    group_list[y].append(clientsock)
                    groupl=len(group_list[y])
                    if groupl>2:
                        for h in range(1,groupl):
                            group_list[y][h].send(requser.encode())
                    else:
                        clientsock.send(requser.encode())
                    break

        elif str(logindata[0]) == 'group':
            #接受文件
            '''
                先接受图片到本地缓存server_down_loads，再识别接受用户，
                判断其是否在线，若在线进行转发，否则不转发，提示不在线
                使用一个数据包file来预定一个文件的发送时间，在接收到file的
                提示数据包的时候，就准备接受一个file，与用户转发也是同理
            '''
            if logindata[3] == "file":
                fileinfo_size = struct.calcsize('128sl')
                buf = clientsock.recv(fileinfo_size)
                if buf:
                    filename, filesize = struct.unpack('128sl', buf)
                    fn = filename.decode().strip('\x00')
                    new_filename = os.path.join('./server_downloads', fn)

                    recvd_size = 0
                    fp = open(new_filename, 'wb')

                    while not recvd_size == filesize:
                        if filesize - recvd_size > 1024:
                            data = clientsock.recv(1024)
                            recvd_size += len(data)
                        else:
                            data = clientsock.recv(1024)
                            recvd_size = filesize
                        fp.write(data)
                    fp.close()
                    
                #转发文件给群内成员
                for wl in range(0, group_l):
                    if str(group_list[wl][0]) == str(logindata[1]):
                        senddata = ["file"]
                        senddata.append(str(logindata[2])+":")
                        senddata = '*'.join(senddata)
                        l = len(group_list[wl])
                        try:
                            if l >=2:
                                for x in range(1, l):
                                    group_list[wl][x].send(senddata.encode())
                                    
                                    file_path = new_filename
                                    fhead = struct.pack(b'128sl', bytes(os.path.basename(file_path), encoding='utf-8'), os.stat(file_path).st_size)
                                    print('client filepath: {0}'.format(file_path))
                                   
                                    group_list[wl][x].send(fhead)
                                    fp = open(file_path, 'rb')
                                    while 1:
                                        data = fp.read(1024)
                                        if not data:
                                            print('{0} file send over...'.format(file_path))
                                            break
                                        group_list[wl][x].send(data)
                            else:
                                #clientsock.send(senddata.encode())
                                break
                            print("群聊信息" + str(senddata)+str(clientaddress))
                        except ValueError:
                            break
                            
            #正常普通交流信息
            else:
                for wl in range(0, group_l):
                    if str(group_list[wl][0]) == str(logindata[1]):
                        senddata=str(logindata[2])+":"+str(logindata[3])
                        l = len(group_list[wl])
                        try:
                            if l >=2:
                                for x in range(1, l):
                                    group_list[wl][x].send(senddata.encode())
                            else:
                                clientsock.send(senddata.encode())
                                break
                            #print("群聊信息" + str(senddata)+str(clientaddress))
                        except ValueError:
                            break

        elif str(logindata[0]) == 'single_person':
            if logindata[3] == "file":
                '''
                先接受图片到本地缓存server_down_loads，再识别接受用户，
                判断其是否在线，若在线进行转发，否则不转发，提示不在线
                使用一个数据包file来预定一个文件的发送时间，在接收到file的
                提示数据包的时候，就准备接受一个file，与用户转发也是同理
                '''
                fileinfo_size = struct.calcsize('128sl')
                buf = clientsock.recv(fileinfo_size)
                if buf:
                    filename, filesize = struct.unpack('128sl', buf)
                    fn = filename.decode().strip('\x00')
                    new_filename = os.path.join('./server_downloads', fn)

                    recvd_size = 0
                    fp = open(new_filename, 'wb')

                    while not recvd_size == filesize:
                        if filesize - recvd_size > 1024:
                            data = clientsock.recv(1024)
                            recvd_size += len(data)
                        else:
                            data = clientsock.recv(1024)
                            recvd_size = filesize
                        fp.write(data)
                    fp.close()
                    
                #转发给用户
                user_cl = len(user_client)
                #print(user_client)
                
                senddata = ["file"]
                senddata.append(str(logindata[1])+":")
                send_info = '*'.join(senddata)
                z = 1
                for pl in range(0,user_cl):
                    if user_client[pl][0] == logindata[2]:
                        #print(logindata[2])
                        user_client[pl][1].send(send_info.encode())
                        file_path = new_filename
                        fhead = struct.pack(b'128sl', bytes(os.path.basename(file_path), encoding='utf-8'), os.stat(file_path).st_size)
                        print('client filepath: {0}'.format(file_path))
                       
                        user_client[pl][1].send(fhead)
                        fp = open(file_path, 'rb')
                        while 1:
                            data = fp.read(1024)
                            if not data:
                                print('{0} file send over...'.format(file_path))
                                break
                            user_client[pl][1].send(data)
                        #clientsock.send(send_info.encode())
                        break
                    elif z == user_cl:
                        back = str(logindata[2])+'不在线'
                        clientsock.send(back.encode())
                    z+=1
                '''
                for wl in range(0, group_l):
                    if str(group_list[wl][0]) == str(logindata[1]):
                        senddata = ["file"]
                        senddata.append(str(logindata[2])+":")
                        senddata = '*'.join(senddata)
                        l = len(group_list[wl])
                        try:
                            if l >=2:
                                for x in range(1, l):
                                    group_list[wl][x].send(senddata.encode())
                                    
                                    file_path = new_filename
                                    fhead = struct.pack(b'128sl', bytes(os.path.basename(file_path), encoding='utf-8'), os.stat(file_path).st_size)
                                    print('client filepath: {0}'.format(file_path))
                                   
                                    group_list[wl][x].send(fhead)
                                    fp = open(file_path, 'rb')
                                    while 1:
                                        data = fp.read(1024)
                                        if not data:
                                            print('{0} file send over...'.format(file_path))
                                            break
                                        group_list[wl][x].send(data)
                            else:
                                #clientsock.send(senddata.encode())
                                break
                            print("群聊信息" + str(senddata)+str(clientaddress))
                        except ValueError:
                            break
                '''
            else:
                #print(logindata)
                user_cl = len(user_client)
                #print(user_client)
                send_info = str(logindata[1])+":"+str(logindata[3])
                z = 1
                for pl in range(0,user_cl):
                    if user_client[pl][0] == logindata[2]:
                        user_client[pl][1].send(send_info.encode())
                        #clientsock.send(send_info.encode())
                        break
                    elif z==user_cl:
                        back=str(logindata[2])+'不在线'
                        clientsock.send(back.encode())
                    z+=1
                
        elif str(logindata[0]) == 'quit':
            user_cl = len(user_client)
            for pl in range(0,user_cl):
                if user_client[pl][0]==logindata[1]:
                    del user_client[pl]
                    #clientsock.send(send_info.encode())
                    break
            break
            
        elif str(logindata[0]) == '':
            print('无法识别：')
            print(logindata[0])
            break

    clientsock.close()
    #del client_list[-1]




while True:
    clientsock, clientaddress = s.accept()
    client_list.append(clientsock)
    print('connect from:',clientaddress)
    '''joinfo=str(clientaddress)
    try:
        ld=len(client_list)
        for x in range(0, ld):
            client_list[x].send(joinfo.encode())
    except ValueError:
        continue
    '''
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))  #新创建的线程
    t.start()
s.close()



