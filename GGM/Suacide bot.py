from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
   return '%s님 환영합니다.' % name

@app.route('/login', methods = ['GET']) # methods = ['GET', 'POST']) 로 여러 개 가능
def login():
    return render_template('login.html')

@app.route('/submit', methods = ['POST'])
def submit():
   if request.method == 'POST':
      user = request.form['myName']
      return redirect(url_for('welcome', name=user))

if __name__ == '__main__':
    app.run(host="127.0.0.1", port="8080")