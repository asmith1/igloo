# graph version
# the connections will be represented by an undirected graph
# this will be implemented using adjacency lists
# this version is simplified in that it treats connections as bidirectional and does not account for verified/unverified connections

def search(searchName):
	results = []
	if connections.has_key(searchName) == False:
		print "You are not in our database. Join by typing add and entering your name!"
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
			print "You have no 2nd degree connections in our database!"
		else:
			print "Your 2nd degree connections are:", finalResults

def addConnection(yourname, connection):
	if connections.has_key(yourname):
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

def add():
	while True:
		names = []
		yourname = raw_input("Please enter your name: ")
		if yourname == 'done':
			break
		while True:
			connection = raw_input("Please enter a contact: ")
			if connection == 'done':
				break
			else: # add the connection to the list
				connections = addConnection(yourname, connection)
				connections = addConnection(connection, yourname)
				#print connections

connections = {}
while True:
	mode = raw_input("Would you like to add connections or search for your 2nd order connections? ")
	if mode == "add":
		add()
	elif mode == "search":
		searchName = raw_input("Please enter your name: ")
		search(searchName)
	elif mode == 'exit':
		break
	else:
		print "Please type 'add', 'search', or 'exit'"



