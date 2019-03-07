from flask import Flask, render_template ,session, escape, request, Response
from flask import url_for, redirect, send_from_directory
from flask import send_file, make_response, abort, jsonify
from flask import Flask, jsonify, request
import json
import os, sys

from manager import DatabaseManager

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

app = Flask(__name__)
app.secret_key="secret"

app.url_map.strict_slashes = False
db = DatabaseManager()

@app.route('/')
def basic_pages(**kwargs):
    return make_response(open('index.html').read())

@app.route('/moreInfo')
def navigate():
    return make_response(open('moreinfo.html').read())

@app.route('/getAreaInfo', methods=['POST'])
def getAreaInfo():
	area = request.json['area']
	return db.getArea(area), 200, {'Content-Type':'application/json'}

@app.route('/getDataSourceInfo', methods=['POST'])
def getDataSourceInfo():
	datasource = request.json['datasource']
	return db.getDataSourceInfo(datasource), 200, {'Content-Type':'application/json'}

@app.route('/getAllAreas', methods=['POST'])
def getAllAreas():
	return db.getAllAreas(), 200, {'Content-Type':'application/json'}

@app.route('/getFiles', methods=['POST'])
def getFiles():
	area = request.json['area']
	location = request.json['location']
	dataSource = request.json['dataSource']
	fileType = request.json['fileType']
	return db.getFiles(area, dataSource, location, fileType), 200, {'Content-Type':'application/json'}
	
if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 5000)))