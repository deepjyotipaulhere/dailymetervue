from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import pymongo
import datetime
import os
from bson.objectid import ObjectId
from gridfs import GridFS

app=Flask(__name__)
CORS(app)

def connect():
    client=MongoClient('mongodb://149.56.14.83:27017/')
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

@app.route('/createpost',methods=['POST'])
def post():
    x=request.get_json()
    con=connect()
    db=con.dailymeter
    coll_post=db.post
    x["date"]=datetime.datetime.utcnow()
    try:
        postid=coll_post.insert_one(x).inserted_id
    except pymongo.errors.DuplicateKeyError:
        return "Duplicate Key"
    print(postid)
    con.close()
    return str(postid)

@app.route('/login',methods=['POST'])
def login():
    x=request.get_json()
    con=connect()
    db=con.dailymeter
    coll_user=db.user
    u={}
    try:
        xx=coll_user.find_one({"email":x["email"],"pwd":x["pwd"]})
        u["name"]=xx["name"]
        u["uid"]=str(xx["_id"])
        con.close()
        return jsonify(u)
    except Exception as e:
        print(e)
        con.close()
        return "invalid"

@app.route('/getposts/<uid>',methods=['GET'])
def posts(uid):
    x=request.get_json()
    con=connect()
    db=con.dailymeter
    coll_post=db.post
    u=[]
    try:
        p={}
        x=coll_post.find({"user":uid})
        for post in x:
            p={}
            p["title"]=post["title"]
            p["post"]=post["post"][:50]
            p["date"]=post["date"]
            p["postid"]=str(post["_id"])
            u.append(p)
        con.close()
        return jsonify(u)
    except Exception as e:
        print(e)
        con.close()
        return "error"

@app.route('/post/<id>',methods=['GET'])
def getpost(id):
    x=request.get_json()
    con=connect()
    db=con.dailymeter
    coll_post=db.post
    u={}
    try:
        # print(id.encode("utf-8"))
        x=coll_post.find_one({"_id": ObjectId(id)})
        u["title"]=x["title"]
        u["post"]=x["post"].replace('\n','<br />')
        u["date"]=x["date"]
        con.close()
        return jsonify(u)
    except Exception as e:
        print(e)
        return "notfound"

@app.route('/insertdoc',methods=['POST'])
def insertdoc():
    file = request.files['mediafile']
    if file.filename == '':
        return "None"
    else:
        con=connect()
        db=con.dailymeter
        fs = GridFS(db)
        ob = fs.put(file,content_type=file.content_type)
        return str(ob)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')