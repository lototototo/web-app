from flask import render_template, request, redirect, url_for
from app import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/home')
def red_home():
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('contact_successfully.html')
    else:
        return redirect(url_for('contact'))