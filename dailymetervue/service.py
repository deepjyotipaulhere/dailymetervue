from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
import pymongo
import datetime

app=Flask(__name__)
CORS(app)

def connect():
    client=MongoClient('mongodb://localhost:27017/')
    return client

@app.route('/register',methods=['POST'])
def register():
    x=request.get_json()
    con=connect()
    db=con.dailymeter
    coll_user=db.user
    x["date"]=datetime.datetime.utcnow()
    try:
        uid=coll_user.insert_one(x).inserted_id
    except pymongo.errors.DuplicateKeyError:
        return "Duplicate Key"
    print(uid)
    con.close()
    return str(uid)



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')