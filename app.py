from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))  # 确保模板目录正确设置

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # 在此处添加登录逻辑
        return redirect(url_for('login'))  # 示例：登录后重定向到登录页面
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        # 在此处添加注册逻辑
        return redirect(url_for('login'))  # 示例：注册后重定向到登录页面
    return render_template('signup.html')

@app.route('/discover', methods=['GET', 'POST'])
def discover():
    return render_template('discover.html')


if __name__ == '__main__':
    app.run(debug=True)
