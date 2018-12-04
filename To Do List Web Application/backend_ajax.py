from flask import Flask, request, render_template, redirect#, session;

import random, pymysql;

app=Flask(__name__);

app.secret_key=str(random.SystemRandom());

maxLen=150; # highest acceptable length for a list item

sqlconn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='mysql');

sqlcur = sqlconn.cursor();

try:
    sqlcur.execute("DROP TABLE todo");
except pymysql.err.InternalError:
    pass;

sqlcur.execute("CREATE TABLE todo(task VARCHAR(150) NOT NULL,num INT NOT NULL PRIMARY KEY AUTO_INCREMENT)");

#sqlcur.execute("show tables");

def clean(string):
    try:
        while(string[0]==' ' or string[-1]==' '):
                if(string[0]==' '):
                    string=string[1:];
                if(string[-1]==' '):
                    string=string[:-1];
    except IndexError:
        pass;
    cleanString='';
    for itrtnA in range(len(string)):
            if(string[itrtnA]==' '):
                if(string[itrtnA-1]!=' '):
                    cleanString+=string[itrtnA];
                else:
                    continue;
            elif(string[itrtnA]=='/' or string[itrtnA]=='\\'):
                continue;
            else:
                cleanString+=string[itrtnA];
    return cleanString;

@app.route('/',methods=['GET','POST'])
def home():
    if(request.method=='GET'):
        sqlcur.execute('SELECT * FROM todo');
        return render_template('frontend_ajax.html',toDoList=sqlcur.fetchall())#list(session.values()));
    elif(request.method=='POST'):
        inputt=clean(request.form['input']);
        if(0<len(inputt)<=maxLen):
            #session[inputt]=inputt;
            qry="INSERT INTO todo (task,num) VALUES ('"+inputt+"',NULL)";
            sqlcur.execute(qry);
        sqlcur.execute('SELECT * FROM todo');
        return render_template('frontend_ajax.html',toDoList=sqlcur.fetchall())#list(session.values()));

    
@app.route('/delete/<index>',methods=['DELETE'])
def delete(index):
    #del session[task];
    qry='DELETE FROM todo WHERE task='+index;
    sqlcur.execute(qry);
    sqlcur.execute('COMMIT');
    sqlcur.execute('SELECT * FROM todo');
    return render_template('frontend_ajax.html',toDoList=sqlcur.fetchall())#list(session.values()));

@app.route('/edit/<oldIndex>/<newValue>',methods=['PUT'])
def edit(oldIndex,newValue):
    newValue=clean(newValue);
    #newDict={};
    #global session;
    if(0<len(newValue)<=maxLen):
        sqlcur.execute("UPDATE todo SET task='"+newValue+"' WHERE num="+oldIndex);
        '''
        for key in session:
            if(key!=oldValue):
                newDict[key]=session[key];
            else:
                newDict[newValue]=newValue;
        session=newDict;'''
            
    return render_template('frontend_ajax.html',toDoList=sqlcur.fetchall())#list(session.values()));


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = "Origin, X-Requested-With, Content-Type, Accept"
    return response
    

app.run(debug=True,threaded=True);
