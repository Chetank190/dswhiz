from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    first_name = "Chetan"
    return render_template('index.html',
                           f_name = first_name)