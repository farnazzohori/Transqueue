from flask import Flask, request, jsonify
from pymongo import MongoClient
import random
import time
import transaction_module
import multiprocessing

#Data Base Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["Sh4z0"]
Q_Col = db["Q"]
Bank_Col = db["Bank"]

app = Flask(__name__)



def get_transaction_code():
    random_value = str(random.randint(0,10000000000))
    timestamp = str(time.time()).replace(".","")
    return str(timestamp + random_value)

def func_transaction_module ():
    transaction_module.value_Parametr()
    

def insert_transaction_q(username,value,transaction_id):
    document = {'username': username, 'value': value, "transaction_id" :transaction_id}
    Q_Col.insert_one(document)

@app.route('/api/data/', methods=['POST'])
def receive_data():
    data = request.get_json()
    username = data.get('username')
    value = data.get('value')
    transaction_id = str(get_transaction_code())
    try:
        insert_transaction_q(username,value,transaction_id)
    except:
        pass
    
    if not username or not isinstance(value, (int, float)):
        return jsonify({
            'status': 'error',
            'message': 'Invalid input. You must provide a username and a numeric value.'
        }), 400
    else:
        return jsonify({
        'status': 'success',
        'message': f'Data received for user {username}',
        'data': {
            'username': username,
            'value': value,
            'transaction_id':transaction_id
        }}), 200
    '''
    def afzayesh_mojodi(username,value):
        document = {'username': username, 'value': value}
        Bank_Col.insert_one(document)
        return jsonify({
        'status': 'success',
        'message': f'Data received for user {username}',
        'data': {
            'username': username,
            'value': value,
            'transaction_id':
        }
    '''

    process1 = multiprocessing.Process(target=func_transaction_module )
    process2 = multiprocessing.Process(target=get_transaction_code)
    process3 = multiprocessing.Process(target=receive_data)
    
    
    process1.start()
    process2.start()
    process3.start()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)