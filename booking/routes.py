from flask import (render_template, flash, redirect)
from booking import app
from booking.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Mans'}
    bills = [
        {
            'payer': {'username': 'John'},
            'company': 'Telia',
            'amount': 249,
            'category': 'it',
        },
        {
            'payer': {'username': 'Susan'},
            'company': 'Trygg Hansa',
            'amount': 350,
            'category': 'car',
        }
    ]
    return render_template('index.html', title='Home', user=user, bills=bills)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {0}, remember_me={1}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    else:
        flash("Please fill both username and password")
    return render_template('login.html', title='Sign In', form=form)