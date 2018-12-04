from flask import Flask, request, jsonify
from json import *
app = Flask(__name__)

@app.route('/')
def doNothing():
	pass # (Under TA Ian's approval, we are allowed to do this).

@app.route('/todo/create', methods=['POST'])
def createItem():
	data = request.get_json()
	session['todo'] = data.get('newItem')
	return jsonify('success')

@app.route('/todo/read', methods=['GET'])
def returnItems():
	#return session
	return data

@app.route('/todo/update', methods=['PUT'])
def addItem():
	pass

@app.route('/todo/update',methods=['PUT'])
def addItem(old,new):
    if(len(new)>0
       and new not in data):
       # and not allSpaces(newValue)):
        data[data.index(old)]=new;
    return redirect('/');

       
@app.route('/todo/delete', methods=['DELETE'])
def removeItem():
	 data.remove(task);



@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept"
    return response

