from flask import Flask, render_template, request, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename
import os
import json
from pathlib import Path


data = Path('database.json').read_text()
users = json.loads(data)
n = len(users)

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = '/Users/admin/Pictures'


@app.route('/')
def index():
    return render_template('main.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/loginput', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        x = request.form['user']
        y = request.form['pwd']
        login = True
        for i in range(n):
            if x == users[i]["username"]:
                if y == users[i]["password"]:
                    login = False
                    render_template('main.html', username=users[i]['username'])
            if x == users[i]["phonenum"]:
                if y == users[i]["password"]:
                    login = False
                    render_template('main.html', username=users[i]['username'])
            if x == users[i]["email"]:
                if y == users[i]["password"]:
                    login = False
                    render_template('main.html', username=users[i]['username'])
        if login:
            render_template('/login.html', messages='密码不对或账号错误', login=login)



# @app.route('uploaded/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)
