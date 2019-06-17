import flask
import pickle
import numpy as np

from flask import Flask, render_template, request
from app.lib.dict import load_dict

app = Flask(__name__)

temp_dict = load_dict()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        form = request.form
        input_text = request.form['input-text']

        print(input_text)
        return render_template('results.html', input_text=input_text, form=form, temp_dict=temp_dict)
    else:
        return render_template('error.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

