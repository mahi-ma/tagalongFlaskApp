from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for('index'))
        else:
            return 'Login failed'

    # return render_template('login.html')

@app.route('/index')
@login_required
def index():
    return 'Logged in as: ' + current_user.id
