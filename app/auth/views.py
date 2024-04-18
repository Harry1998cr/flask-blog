from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, logout_user


from . import auth
from ..models import User, db
from .forms import LoginForm, RegistrationForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(formdata=request.form)
    print(form.password)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main_page'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/forgot-password')
def forget_password():
    return render_template('auth/forgot-password.html')


@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm(formdata=request.form)
    print(form.email.data)
    if form.validate_on_submit():
        print("Registration form validated successfully")
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        print("Redirecting to login page...")
        return redirect(url_for('auth.login'))  # 注册成功后重定向到登录页面
    return render_template('auth/register.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main_page'))
