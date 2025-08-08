from flask import Flask, request, jsonify
from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017/")
db = client["Sh4z0"]
Q_Col = db["Q"]
Bank_Col = db["Bank"]
document_bank=0

def value_Parametr():
    i=0
    Q_value=0
    document = list(Q_Col.find()) 
    for i in document:
        #print('Q_Col username:', i['username'])
        Q_value = i['value']
        #print('Q_Col value:', Q_value)
    
    document_bank=list(Bank_Col.find())
    if len(document_bank)==0:
        pass
    else:
        for x in document_bank:
            Bank_value=x['value']
            
            print(x['username'],Q_value)
            print(x['username'],Bank_value)
            
            sum_result=Bank_value+Q_value
            
            print("sum:",x['username'],sum_result)
            
            Bank_Col.update_one(
                {'username':i['username']},  
                {'$set': {'value': sum_result}})
            
            Q_Col.delete_one({'username':i['username']})

value_Parametr()