from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_login import login_user, logout_user, login_required
from sqlalchemy.orm import Query

from clinicapp import login, app, db
import dao, models
from models import UserRole, BenhNhan,  DatLichKham, BacSi
from datetime import datetime


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login/", methods=['GET', 'POST'])
def login_process():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user)
            return redirect('/')
        else:
            return ' Dang nhap thanh cong'
    return render_template('login.html')

@app.route("/logout/")
def logout_process():
    logout_user()
    return redirect('/login/')



@app.route("/register/", methods=['GET', 'POST'])
def register_process():
    err_msg = ''
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        if password == confirm:
            data = request.form.copy()
            del data['confirm']

            dao.add_user(avatar=request.files.get('avatar'), **data)

            return redirect('/login/')
        else:
            err_msg = 'Mật khẩu không khớp!'

    return render_template('register.html', err_msg=err_msg)



@app.route('/datlichkham', methods=['GET', 'POST'])
# @login_required
def datlichkham():
    bac_si_list = BacSi.query.all()
    if request.method == 'POST':
        ho_ten = request.form['ho_ten']
        so_dien_thoai = request.form['so_dien_thoai']
        email = request.form['email']
        ngay_kham = request.form['ngay_kham']
        gio_kham = request.form['gio_kham']
        bac_si = request.form['bac_si']
        ghi_chu = request.form['ghi_chu']

        new_lich_kham = DatLichKham(ho_ten=ho_ten, ngay_kham=ngay_kham, gio_kham=gio_kham, bac_si=bac_si, ghi_chu=ghi_chu)
        db.session.add(new_lich_kham)
        new_benh_nhan = BenhNhan(ho_ten=ho_ten,so_dien_thoai=so_dien_thoai,email=email)
        db.session.add(new_benh_nhan)
        db.session.commit()

        return redirect(url_for('datlichkham'))

    return render_template('datlichkham.html',bac_si_list=bac_si_list)

@app.route("/gioithieu/")
def gioithieu():
    return render_template("gioithieu.html")

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
