from market import app, db
from flask import render_template, flash, redirect, url_for
from market.forms import RegisterForm, LoginForm
from market.models import User

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    

    if form.validate_on_submit():
        created_user = User(
            username=form.username.data,
            email_address=form.email_address.data,
            password=form.password1.data
        )
        db.session.add(created_user)
        db.session.commit()
        flash("Account created! Logged in as ", category="success")
        return redirect(url_for('home_page'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'Error: {err_msg}', category="danger")

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    return render_template('login.html', form=form)
