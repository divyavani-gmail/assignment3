from pymongo import MongoClient 
import pandas as pd
   
num=int(input("Enter the no. of times you want to insert document:"))
# Connect with the portnumber and host 
client = MongoClient("mongodb://localhost:27017/")     
# Access database 
mydatabase = client['raven']  
# Access collection of the database 
mycollection=mydatabase['alert'] 
#deleting data if already exists
if len(list(mycollection.find())) > 0:
    mycollection.delete_many({})
df=pd.read_csv('alerts.csv')
df.drop(columns='_id',inplace=True)
df_list=[]
for i in range(num):
    df_list.append(df)
df1=pd.concat(df_list)
documents=df1.to_dict('records')
mycollection.insert_many(documents)
print('No. of documents and their columns inserted in Collection',len(list(mycollection.find())))
