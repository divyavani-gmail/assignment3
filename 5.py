# Q5. Write an API to delete alerts with a given date,
#  alert category and time span. 
#  The API should be able to delete alerts given a start time and end time for that particular date

from flask import Flask, request, jsonify
from pymongo import MongoClient 
from bson.json_util import dumps
import pandas as pd

# given_date = input("Enter alert data:")
# alert_category = input("Enter alert category:")
# start_time = input("Enter start time:")
# end_time = input("Enter end time:")

client = MongoClient("mongodb://localhost:27017/")  
db = client['raven']  
mycol=db['alert'] 

app = Flask(__name__)
@app.route('/alert/', methods=['DELETE'])
def post():
    data = dict(request.args)
    print(type(data['date']))
    # data = mycol.find({"alert_1":category,'date':date})

    # print(data)
    # df=pd.DataFrame(mycol.find())s
    # df.drop(columns='_id',inplace=True)
    # df.drop_duplicates(inplace=True)
    # documents=df.to_dict('records')
    # mycol.insert_many(documents)
    # data = request.json

    # category = data['category'] 
    # date = data['date']
    result = mycol.find({"alert_1":str(data['category']) ,'date':str(data['date']) })
    print(list(result))
    print(len(list(result)))
    if not len(list(result)):
        return jsonify({"message":"records not found"})
    else:
        result1 = mycol.delete_many({"alert_1":str(data['category']) ,'date':str(data['date'])})
    # print(result1)
    
    # start_time = data['start_time']
    # end_time = data['end_time']
    # print(alert_category)

    # if 'alert_category' in data and 'date' in data:
    #     if start_time >= data and end_time <= data:


    return jsonify({"message":"record deleted"})

if __name__ == '__main__':
    app.run(debug=True)

    # result = dumps(data)
    # print(result)
    # df=pd.DataFrame(mycol.find())
    # return jsonify({1:'value'})

