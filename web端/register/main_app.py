'''
writen by LiuChang
2020/5/3
author@LiuChang
'''
# coding=utf-8
import sys
sys.path.append('..')
from flask import Flask, request, render_template, flash
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
#from secret_func import *
import config
#from flask_mail import Mail, Message
import random
import jsonify


app = Flask(__name__)
cache = Cache(
    config={
        "CACHE_TYPE": "simple"
    }
)
app.config.from_object(config)
cache.init_app(app)
db = SQLAlchemy(app)


# 对flask进行一个初始化
# 创建一个simple表
class Simple(db.Model):
    __tablename__ = 'simple'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(100), nullable=False, unique=True)
    pwd = db.Column(db.String(100), nullable=False, unique=False)

db.create_all()


@app.route('/')
# -----------------------------------------------------------
def index():
    return render_template("regist.html")

'''
@app.route('/lsuccess/', methods=['post', 'GET'])
def login():
    if request.method == "POST":
        user = request.form.get('username')  # broswer端处理过程
        pwd = request.form.get('password')
        print("id:" + user)
        print("pwd:" + pwd)
        if user == Simple.user and pwd == Simple.pwd:
            return "参数请求不正常"
        else:
            result = Simple.query.filter(Simple.user == user).first()
            if result is None:
                flash("用户不存在！")
                return render_template('loginin.html')
            else:
                if login_in_varify(result.pwd, pwd):
                    return "登录成功"
                else:
                    flash("用户名或密码错误")
                    return render_template('loginin.html')
'''

@app.route('/rsuccess/', methods=['POST'])
def regist_function():
    if request.method == "POST":
        user = request.form.get('rename')
        password = request.form.get('repwd')
        #email = request.form.get('email')
        #pubk = request.form.get('pubk')
        print("id:" + user)
        print("pass:" + password)
        #print("email:" + email)
        #print("public_key: "+pubk)
        '''
        regist_trans = password  # 处理后的数据
        user, pwd, pubk = sign_up_process(regist_trans)
        validation_number = cache.get(user)
        print("code:" + str(validation_number))
        validation_from_user = request.form.get('verification')
        email = sm4_c(email)
        result = Simple.query.filter(Simple.email == email).first()
        if result is not None:
            flash("该邮箱已注册！")
            return render_template('regist.html')
        if str(validation_number) != validation_from_user:
            flash("验证码有误!")
            return render_template('regist.html')
            # return render_template("./templates/regist.html")
        '''
        result = Simple.query.filter(Simple.user == user).first()
        if result is None:
            simple1 = Simple(user=user, pwd=password)
            db.session.add(simple1)
            db.session.commit()
            return "注册成功"
        else:
            flash("账号已经存在")
            return render_template('regist.html')
'''
@app.route('/sendcode/')
def send_code():
    id = request.args.get("id")
    email = request.args.get('email')

    mail = Mail(app)
    validation_number = random.randint(1000, 10000)
    message = "您的验证码为： " + str(validation_number)
    msg = Message(message,
                  recipients=[email])
    mail.send(msg)
    cache.set(id, validation_number)
    print("邮件已发送    ")
    data = {"msg": "ok"}
    return jsonify(data)
'''

@app.route('/changing/', methods=['post', 'GET'])
def change_function():
    if request.method == "POST":
        user = request.form.get('username')  # broswer端处理过程
        pwd = request.form.get('pwd')
        #email = request.form.get('email')
        new_password = request.form.get('repwd')
        #code = request.form.get('verification')
        result = Simple.query.filter(Simple.user == user).first()
        print("id:" + user)
        print("pass:" + pwd)
        #print("email:" + email)
        print("new_pass:" + new_password)
        #print("code:" + str(code))
        if result is None:
            flash("用户不存在！")
            return render_template("change.html")
        else:
            if result.pwd == pwd:
                result.pwd = new_password
                db.session.commit()
                return "修改成功！"
            else:
                flash("输入有误！")
                return render_template('change.html')

'''
@app.route('/changing2/', methods=['POST'])
def change2_function():
    if request.method == "POST":
        inputtext = request.form.get("verification")
        user = request.form.get("username")
        new_password = request.form.get('repwd')
        result = Simple.query.filter(Simple.user == user).first()
        print("id:" + user)
        print("new_pass:" + new_password)
        print("sign:" + inputtext)
        if result is None:
            flash("用户不存在！")
            return render_template("change_sign.html")
        else:
            public_key = result.pubk
            if verify_sm2_sign(public_key, inputtext):
                first_para, new_pass, not_important = sign_up_process(new_password)
                result.pwd = new_pass
                db.session.commit()
                return "修改成功"
            else:
                flash("私钥有误！")
                return render_template('change_sign.html')
'''

@app.route('/regist/')
def regist_html():
    return render_template('regist.html')

'''
@app.route('/login/')
def loginin_html():
    return render_template('loginin.html')
'''

@app.route('/change/')
def change_html():
    return render_template('change.html')

'''
@app.route('/change2/')
def change2_html():
    return render_template('change_sign.html')
'''

if __name__ == '__main__':
    app.run(debug=True)
