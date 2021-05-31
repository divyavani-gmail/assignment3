# Q2. Write an API to get citywise alert count from the alerts.csv provided to you
from flask import Flask, request, jsonify
from pymongo import MongoClient 
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")     
# Access database 
db = client['raven']  
# Access collection of the database 
mycol=db['alert'] 
# alert_category = input("Enter alert category:")
# city_name = input("Enter alert category:")

app = Flask(__name__)
@app.route("/alert_count", methods=['GET'])
def alert_count():
    data = dict(request.args)
    total_rows = len(list(mycol.find())) 
    city_count = mycol.find({"alert_1":str(data['alert_category']),"city":str(data['city_name'])})

    # result = mycol.find({"alert_1":str(data['category']) ,'date':str(data['date']) })

    return jsonify({'Total No.of rows':total_rows,'Alert count':len(list(city_count))})

    

if __name__ == "__main__":
    app.run(port=5000, debug=True)
