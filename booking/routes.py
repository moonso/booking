from flask import (render_template, flash, redirect, url_for, request)
from flask_login import (current_user, login_user, logout_user, login_required)
from booking import (app)
from booking.forms import (LoginForm, RegistrationForm)
from booking.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home', bills=bills)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        existing_user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        user = None
        if existing_user:
            user = User(existing_user['_id'], existing_user['email'], existing_user['password_hash'])
        if existing_user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('index')
        return redirect(url_for('index'))
        
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    user_collection = app.config['USERS_COLLECTION']
    
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user_obj = User(username=form.username.data, email=form.email.data)
        user_obj.set_password(form.password.data)
        user_collection.insert_one(
            {
                '_id': user_obj.username,
                'email': user_obj.email,
                'password_hash': user_obj.password_hash,
            }
        )
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for('login'))
    
    return render_template('register.html', title='Register', form=form)
        

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/add')
def add():
    """Add a user to the database"""
    u = User('Susan', email='susan@mail.com')
    u.set_password('cat')
    user_collection = app.config['USERS_COLLECTION']
    # print(dummy_user.__dict__)
    user_collection.insert_one(
        {
            '_id': u.username,
            'email': u.email,
            'password_hash': u.password_hash,
        }
    )
    return "Added user {0} with email {1}".format(u.username, u.email)

@app.route('/wipe')
def wipe():
    """Remove all users"""
    user_collection = app.config['USERS_COLLECTION']
    # print(dummy_user.__dict__)
    user_collection.remove({})
    return "Removed all users"
