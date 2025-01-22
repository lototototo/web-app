from flask import render_template, request, redirect, url_for
from app import app
from datetime import datetime

@app.route('/')
def home():
    current_time = datetime.now()
    return render_template('index.html', current_time=current_time)

@app.route('/home')
def red_home():
    return redirect(url_for('home'))

@app.route('/about')
def about():
    users = ['Alice','Bob','Charlie']
    return render_template('about.html', users_list=users)

@app.route('/contact')
def contact():
    contact_dict = {'manager':'John Black', 'address':{'street':'Lenina', 'city':'Moscow', 'index':'142110'}} 
    return render_template('contact.html', contact_dict=contact_dict)

@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('contact_successfully.html')
    else:
        return redirect(url_for('contact'))