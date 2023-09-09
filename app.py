import os
import json
import pymongo
from flask import Flask
from flask import request
app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://cbazjara11:cbastian11@examensjbd.kt9c7lm.mongodb.net/?retryWrites=true&w=majority")
db = client['db_examenf']
collection = db['Camisetas Real Madridcamisetas']

@app.route('/')
def get():
    nombre = collection.find()
    response = []
    for document in nombre:
        document['_id'] = str(document['_id'])
        response.append(document)
    return json.dumps(response)
if __name__ == '__main__':
    app.run()