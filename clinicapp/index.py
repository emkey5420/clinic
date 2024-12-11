from flask import Flask, render_template, request, redirect
from flask_login import login_user, logout_user
from clinicapp import login
import dao , models
from models import UserRole
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login/", methods=['get', 'post'])
def login_process():
    if request.method.__eq__('POST'):
        account = request.form.get('account')
        password = request.form.get('password')

        u = dao.auth_user(account=account, password=password)
        if u:
            login_user(u)
            return redirect('/')

    return render_template('login.html')

@app.route("/register/", methods=['get', 'post'])
def register_process():
    err_msg = ''
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        repassword = request.form.get('repassword')

        if password.__eq__(repassword):
            data = request.form.copy()
            del data['repassword']
            return redirect('/login')
        else:
            err_msg = 'Mật khẩu không khớp!'

    return render_template('register.html')

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
