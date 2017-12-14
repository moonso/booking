from flask import render_template
from booking import app

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
