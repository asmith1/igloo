# igloo.py
# the connections will be represented by an undirected graph
# this will be implemented using adjacency lists
# this version is simplified in that it treats connections as bidirectional and does not account for verified/unverified connections

def search(searchName):
	results = []
	if searchName not in connections:
		return "You are not in our database. Join by typing add and entering your name!"
	else:
		names = connections.get(searchName)
		for i in range(len(names)): # for each connection
			#if connections.has_key(names[i]): #that name has entered connections => it 100% will, because it will at least have searchName in it
				# add all of the values associated with that name key
			secondOrdConns = connections.get(names[i])
			results = results + secondOrdConns
			finalResults = set(results)
			finalResults.remove(searchName)
		if len(finalResults) == 0:
			return "You have no 2nd degree connections in our database!"
		else:
			cleanresults = ', '.join(list(finalResults))
			return "Your 2nd degree connections are: " + cleanresults

# private function, only used internally
def addConnection(yourname, connection):
	if yourname in connections:
		names = connections.get(yourname)
		# next check if the connection is already a value
	else:
		names = []
	newConnections = {yourname: names}
	connections.update(newConnections)
	for i in range(len(names)):
		if names[i] == connection:
			return connections
	# otherwise, if it exits the for loop, the name isnt there so we have to add it
	names.append(connection)
	return connections

# adds a connection to the connections dict and returns the entire updated dict
def add(yourname, connection):
	connections = addConnection(yourname, connection)
	connections = addConnection(connection, yourname)
	return connections

def addbyCL():
	while True:
		names = []
		yourname = input("Please enter your name: (or done to exit)")
		if yourname == 'done':
			break
		while True:
			connection = input("Please enter a contact: (or done to exit)")
			if connection == 'done':
				break
			else: # add the connection to the list
				add(yourname, connection)
				#print connections

connections = {}
if __name__ == '__main__':
	# run program via command line
	while True:
		mode = input("Would you like to add connections or search for your 2nd order connections? ")
		if mode == "add":
			addbyCL()
		elif mode == "search":
			searchName = input("Please enter your name: ")
			print (search(searchName))
		elif mode == 'exit':
			break
		else:
			print("Please type 'add', 'search', or 'exit'")
