from flask import render_template, url_for, request, redirect
from QuanLyPhongMach import app, utils
from QuanLyPhongMach.models import User
from flask_login import login_user, logout_user
from QuanLyPhongMach.admin import*
import hashlib
@app.route('/')

def index():
   return render_template('/index.html')


@app.route("/login", methods=['get', 'post'])

def login_usr():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user = User.query.filter(User.username == username.strip(),
                                 User.password == password).first()

        if user:
            login_user(user=user)


    return render_template('/login.html')






if __name__ == "__main__":
    app.run(debug=True)