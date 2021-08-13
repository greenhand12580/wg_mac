from flask import Flask, render_template, request, url_for, send_from_directory, redirect
from werkzeug.utils import secure_filename
import csv
import os
import json
from pathlib import Path

user_information = ['1', '2', '3', '4']
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



# @app.route('/changepwd')
# def login():
#     return render_template('changepwd.html')


@app.route('/login1')
def login1():
    return render_template('login1.html')


@app.route('/static/login', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        myform = request.form
        x = myform.get("userid", None)
        y = myform.get('pwd', None)
        login = True
        for i in range(n):
            if x == users[i]["username"]:
                if y == users[i]["password"]:
                    login = False
                    with open('user.csv', 'w') as file:
                        writer = csv.writer(file)
                        writer.writerow([users[i]['username'], users[i]['password'], users[i]['email'], users[i]['phonenum']])
                    if not os.path.exists(users[i]['username']+'.csv'):
                        f = open(users[i]['username'] + '.csv', 'w')
                        f.close()
                    return render_template('/main1.html', username=users[i]['username'])
            if x == users[i]["phonenum"]:
                if y == users[i]["password"]:
                    login = False
                    with open('user.csv', 'w') as file:
                        writer = csv.writer(file)
                        writer.writerow([users[i]['username'], users[i]['password'], users[i]['email'], users[i]['phonenum']])
                    if not os.path.exists(users[i]['username']+'.csv'):
                        f = open(users[i]['username'] + '.csv', 'w')
                        f.close()
                    return render_template('/main1.html', username=users[i]['username'])
            if x == users[i]["email"]:
                if y == users[i]["password"]:
                    login = False
                    with open('user.csv', 'w') as file:
                        writer = csv.writer(file)
                        writer.writerow([users[i]['username'], users[i]['password'], users[i]['email'], users[i]['phonenum']])
                    if not os.path.exists(users[i]['username']+'.csv'):
                        f = open(users[i]['username'] + '.csv', 'w')
                        f.close()
                    return render_template('/main1.html', username=users[i]['username'])
        if login:
            return render_template('/login1.html', messages='密码不对或账号错误', login=login)


@app.route('/personalspace')
def personalspace():
    username = ['1', '2', '3', '4']
    with open('user.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            username = row
    title = []
    content = []
    length = int(0)
    with open(username[0] + '.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            title.append(row[1])
            content.append(row[2])
    length = len(title)
    return render_template('personalspace.html', username=username, title=title, content=content, length=length)


@app.route('/static/addarticle', methods=['GET', 'POST'])
def addarticle():
    if request.method == 'POST':
        myarticle = request.form
        x = myarticle.get("username", None)
        y = myarticle.get("title", None)
        z = myarticle.get("content", None)
        with open(x+'.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([x, y, z])
        return redirect(url_for('personalspace'))


@app.route('/static/showarticle/<number>')
def showarticle(number):
    username = ['1', '2', '3', '4']
    content = []
    title = []
    with open('user.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            username = row
    i = 0
    with open(username[0] + '.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if i == int(number):
                content.append(row[2])
                title.append(row[1])
            i += 1
    return render_template('content.html', content=content, username=username[0], title=title)
# @app.route('uploaded/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/changepwd')
def changepwd():
    userinformation = ['1', '2', '3', '4']
    with open('user.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            userinformation = row
    return render_template('changepwd.html', userinformation=userinformation[0])


@app.route('/static/changepwd', methods=['GET', 'POST'])
def chpwd():
    if request.method == 'POST':
        myform = request.form
        username = ['1', '2', '3', '4']
        with open('user.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                username = row
        x = myform.get("username", None)
        if x != username[0]:
            return render_template('changepwd1.html', messages="用户名非本人，请重新输入", userinformation=username[0])
        y = myform.get("oldpwd", None)
        z = myform.get("newpwd", None)
        data1 = Path('database.json').read_text()
        reader = json.loads(data1)
        newdata = []
        chang = len(reader)
        for i in range(chang):
            newdata.append(reader[i])
        for i in range(chang):
            if newdata[i]['username'] == x:
                if newdata[i]['password'] == y:
                    newdata[i]['password'] = z
                else:
                    return render_template('changepwd1.html', messages="旧密码不对，请重新输入", userinformation=username[0])
        data2 = json.dumps(newdata)
        Path('database.json').write_text(data2)
        return render_template('changepwd1.html', messages="修改成功，新密码登录时生效", userinformation=username[0])


if __name__ == '__main__':
    app.run(debug=True)
