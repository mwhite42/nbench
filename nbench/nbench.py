from eve import Eve
from pymongo import MongoClient
from flask import render_template
from flask import send_from_directory, redirect, jsonify
from flask_cors import CORS


client = MongoClient('localhost', 27017)
db = client['nbench']
collection = db['benchmark']
app = Eve(__name__, static_folder='static')
CORS(app, resources={r'/*': {'orgins': '*'}})


@app.route('/ping', methods=['GET'])
def alive():
    return jsonify('nbench is running')


@app.route('/mongotest')
def test_me():
    for doc in collection.find({}):
        print(doc)
    return {'test': 'me'}


if __name__ == '__main__':
    app.run(debug=True)
