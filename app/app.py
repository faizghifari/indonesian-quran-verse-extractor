import flask
import pickle
import numpy as np

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

# @app.route('results')
# def results():
#     model = pickle.load('wordsim.pkl')


if __name__ == '__main__':
    app.run(port=5000, debug=True)

