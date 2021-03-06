from flask import Flask, request, render_template, redirect
from igloo import add, search, getConnections

app=Flask(__name__)

username = None
# connectionList=[]

@app.route('/')
def add_form():
    global username
    return render_template('homepage.html', username=username)

@app.route('/', methods=['POST'])
def add_name():
    global username
    print ("-----USERNAME: ", username)
    username = request.form['username']
    return render_template('homepage.html', username=username)

@app.route('/logout')
def logout():
    print("logout")
    global username
    username = None
    return redirect("/")

@app.route('/add')
def add_connections_page():
    global username
    connectionList = getConnections(username)
    return render_template('add_connections.html', username=username, connectionList=connectionList)

@app.route('/add', methods=['POST'])
def add_connections():
    global username
    connection = request.form['connection']
    newDict = add(username, connection)
    connectionList = newDict[username]
    print (newDict, connectionList)
    return render_template('add_connections.html', username=username, connectionList=connectionList)

# @app.route('/<username>/connections', methods=['POST'])
# def add_connections(username):
#     connection = request.form['connection']
#     addToConnectionList(connection)
#     return render_template('add_form.html', username=username, connectionList=connectionList)

@app.route('/search')
def searchPage():
    global username
    secondDegCons = search(username)
    return render_template('search.html', username=username, secondDegCons=secondDegCons)
