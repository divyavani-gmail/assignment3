# Q3. Insert duplicates in Mongodb and write an API to delete duplicates from mongodb

from flask import Flask, request, jsonify
from pymongo import MongoClient 
import pandas as pd

num=int(input("Enter the no. of times you want to insert document:"))
client = MongoClient("mongodb://localhost:27017/")   
mydatabase = client['raven']  
mycollection=mydatabase['alert'] 


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'Not Found'+request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ == "__main__":
    app.run(debug=True)