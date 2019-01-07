from flask import Flask, request, render_template, redirect
from igloo import add, search

app=Flask(__name__)

username = None
connectionList=[]

@app.route('/')
def add_form():
    return render_template('add_form.html')

@app.route('/', methods=['POST'])
def add_name():
    global username
    if not username:
        print ('getting the username!')
        username = request.form['username']
        return render_template('add_form.html', username=username)
    else:
        # return add_connections(username)
        connection = request.form['connection']
        connectionList.append(connection)
        return render_template('add_form.html', username=username, connectionList=connectionList)

# @app.route('/<username>/connections', methods=['POST'])
# def add_connections(username):
#     connection = request.form['connection']
#     addToConnectionList(connection)
#     return render_template('add_form.html', username=username, connectionList=connectionList)


# @app.route('/')
# def home():
#     add("Ashley", "Joel")
#     add("Elia", "Ashley")
#     add("Ashley", "Daniel")
#     return search("Elia")
#     if __name__ == '__main__':
#         app.run(debug=True)

# @app.route('/search')
# def searchPage():
#
