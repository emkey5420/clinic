from flask import Flask, render_template, request, redirect
from flask_login import login_user, logout_user
from clinicapp import login , app
import dao , models
from models import UserRole




@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login/", methods=['get', 'post'])
def login_process():
    if request.method.__eq__("POST"):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user)
            return redirect('/')

    return render_template('login.html')

@app.route('/login-admin', methods=['post'])
def login_admin_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password, role=UserRole.ADMIN)
    if user:
        login_user(user)

    return redirect('/admin')



@app.route('/register/', methods=['get', 'post'])
def register_process():
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password.__eq__(confirm):
            data = request.form.copy()
            del data['confirm']

            dao.add_user(avatar=request.files.get('avatar'), **data)

            return redirect('/login/')
        else:
            err_msg = 'Mật khẩu không khớp!'

    return render_template('register.html', err_msg=err_msg)

@app.route("/logout/")
def logout_process():
    logout_user()
    return redirect('/login/')


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
