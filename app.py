from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hint_adminpanel')
def hint_adminpanel():
    return render_template('hint_adminpanel.html')
@app.route('/answ')
def answ():
    return render_template('answ.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run()
