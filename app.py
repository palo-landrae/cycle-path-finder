from flask import Flask, render_template, request, json, jsonify, url_for, redirect
from flask_cors import CORS, cross_origin
import pandas as pd
import gpd

app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

cors = CORS(app)

@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/_get_post_json/', methods=['POST'])
def get_post_json():
    data = request.get_json()
    gpd.update_json(data)
    return jsonify(state='success', data=data)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
