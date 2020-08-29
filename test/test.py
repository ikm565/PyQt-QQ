
import cv2
from tkinter import *
import tkinter.filedialog
from PyQt5 import QtCore, QtGui, QtWidgets, QString

root = tkinter.Tk()    # 创建一个Tkinter.Tk()实例
root.withdraw()       # 将Tkinter.Tk()实例隐藏
default_dir = r"文件路径"
file_path = tkinter.filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(default_dir)))
image = Image.open(file_path)
plt.imshow(image)
plt.show()

fhead = struct.pack(b'128sl', bytes(os.path.basename(filepath), encoding='utf-8'), os.stat(file_path).st_size)
s.send(fhead)
print('client filepath: {0}'.format(filepath))

fp = open(filepath, 'rb')
while 1:
  data = fp.read(1024)
  if not data:
    print('{0} file send over...'.format(filepath))
    break
  s.send(data)
s.close()
break


    void imgPathToHtml(QString &path)
    {
         path = QString("<img src=\"%1\"/>").arg(path);
    }
    2.在你的TextBrowser中添加html
    //这里的path既可以是qrc路径,也可以是本地路径
    QString imgPath = QString("D:/img/hello.png");
    imgPathToHtml(imgPath);
    m_TextBrowser.insertHtml(imgPath)



#receive

fname = tkinter.filedialog.asksaveasfilename(title=u'保存文件', filetypes=[("PNG", ".png")])
picture.save(str(fname) + '.png', 'PNG')

def deal_data(sock, addr):
  print("Accept connection from {0}".format(addr))

  while True:
    fileinfo_size = struct.calcsize('128sl')
    buf = sock.recv(fileinfo_size)
    if buf:
      filename, filesize = struct.unpack('128sl', buf)
      fn = filename.decode().strip('\x00')
      new_filename = os.path.join('./', 'new_' + fn)

      recvd_size = 0
      fp = open(new_filename, 'wb')

      while not recvd_size == filesize:
        if filesize - recvd_size > 1024:
          data = sock.recv(1024)
          recvd_size += len(data)
        else:
          data = sock.recv(1024)
          recvd_size = filesize
        fp.write(data)
      fp.close()
    sock.close()
    break