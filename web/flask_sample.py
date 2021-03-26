from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/hello')
def hello():
    return render_template('hello.html')


@app.route('/json')
def ret_json():
    return jsonify(js)

js = [
        {
          "subject": "AWS",
          "score": 30,
          "target": 60,
        },
        {
          "subject": "Python",
          "score": 70,
          "target": 120,
        },
        {
          "subject": "Javascript",
          "score": 3,
          "target": 60,
        },
      ]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)
