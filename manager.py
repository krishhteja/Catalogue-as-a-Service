import pymongo
from pymongo import MongoClient
from flask import Flask, jsonify, request
from datetime import datetime
from datetime import timedelta
import uuid
import dateutil.parser as parser
import os, time

MONGO_HOST = 'MONGO_ADDERSS'
client = pymongo.MongoClient(MONGO_HOST)
db = client.DATABASE_NAME

class DatabaseManager:
    def fun(self):
        return jsonify({"result":"success"})
        
    def getArea(self, area):
        data = db.api
        query = {}
        query['Area'] = area
        search = data.find(query, {"_id":False})
        response = []
        for element in search:
            response.append(element)
        return jsonify({"result":"success", "output":response})
        
    def getAllAreas(self):
        data = db.api
        response = []
        search = data.find({}, {"_id":False}).distinct("Area")
        for element in search:
            response.append(element)
        return jsonify({"result":"success", "output":response})
        
    def getDataSourceInfo(self, datasource):
        data = db.api
        query = {}
        query['Data Source'] = datasource
        response = data.find_one(query, {"_id":False})
        print(response)
        return jsonify({"result":"success", "output":response})
        
    def getFiles(self, area, dataSource, location, fileType):
        data = db.files
        query = {}
        query['Area'] = area
        query['Data Source'] = dataSource
        query['Geo-Location'] = location
        query['Type of Source'] = fileType
        search = data.find(query, {"_id":False})
        output = []
        for file in search:
            output.append(file)
        return jsonify({"result":"success", "output":output})