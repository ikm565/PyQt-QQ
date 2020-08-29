DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
PORT = '3306'
DATABASE = 'liuchang'
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SECRET_KEY = '123456'
SQLALCHEMY_TRACK_MODIFICATIONS = False

'''
MAIL_DEFAULT_SENDER = "2062683161@qq.com"
MAIL_PASSWORD = "nizaitoushishi48"
MAIL_SERVER= 'smtp.qq.com'  # this is email server
MAIL_PORT = 465  # this is the port of email server
MAIL_USE_SSL = True
MAIL_USERNAME = '2062683161@qq.com'
MAIL_PASSWORD = 'fcxccmxmcvzhehih'  # this is email password(这是什么?下面会讲)
FLASKY_MAIL_SENDER = '2062683161@qq.com'  # this is sender
FLASKY_ADMIN = '2062683161@qq.com'  # this is the email of admin
FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'  # this is subject of email we will send
'''