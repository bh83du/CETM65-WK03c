from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    users = ['Stuart','Joe','Frank']
    return render_template('index.html', title = 'Home', users=users)

@app.route('/Stuart')
def my_func_2():
    return 'Hi from the Test Route!'



app.run(debug=True)
