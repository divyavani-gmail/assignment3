from flask import Flask, request, jsonify
from pymongo import MongoClient 
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")     
# Access database 
db = client['raven']  
# Access collection of the database 
mycol=db['alert'] 

app = Flask(__name__)

@app.route("/delete_duplicates", methods=['GET'])
def delete_duplicates():
    df=pd.DataFrame(mycol.find())
    init_count=mycol.count()
    df.drop(columns='_id',inplace=True)
    df.drop_duplicates(inplace=True)
    df.fillna('',inplace=True)
    if len(list(mycol.find())) > 0:
        mycol.delete_many({})
    documents=df.to_dict('records')
    mycol.insert_many(documents)
    return jsonify({'Initial Count':init_count,'Final Count':mycol.count()})


if __name__ == "__main__":
    app.run(port=5000, debug=True)