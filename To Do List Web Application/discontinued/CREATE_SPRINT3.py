@app.route("/todo/create",methods=["POST"])
def create_todo():
	#print(request.get_json())
	data=request.get_json()
	text=data['content']
	#session['todo_list'].append(text)
	#session.modified=True
	sql="INSERT INTO toDolist (todo) VALUES (%s)"
	connection.cursor().execute(sql,(data['content'],))
	connection.commit()
	return jsonify(result="success")

