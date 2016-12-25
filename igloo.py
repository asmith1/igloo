# graph version
# the hookups will be represented by an undirected graph
# this will be implemented using adjacency lists
# this version is simplified in that it treats hookups as bidirectional and does not account for verified/unverified hookups

def search(searchName):
	results = []
	if hookups.has_key(searchName) == False:
		print "You are not in our database. Join by typing add and entering your name!"
	else:
		names = hookups.get(searchName)
		for i in range(len(names)): # for each hookup
			#if hookups.has_key(names[i]): #that name has entered hookups => it 100% will, because it will at least have searchName in it
				# add all of the values associated with that name key
			eskSiblings = hookups.get(names[i])
			results = results + eskSiblings
			finalResults = set(results)
			finalResults.remove(searchName)
			print "Eskimo siblings up to", names[i], "are:", finalResults
			#for ind in range(len(hookups.keys())):
				#for index in range(len(hookups.get(hookups.keys()[ind]))): #for each of the names in the list of name associated with key[ind]
					#if hookups.get(hookups.keys()[ind])[index] == searchName:
					#	results.append(hookups.keys()[ind])
						#print "Results from iteration", index, "are :", results
		print "Your eskimo siblings are:", finalResults

def addHookup(yourname, hookup):
	if hookups.has_key(yourname):
		names = hookups.get(yourname)
		# next check if the hookup is already a value
	else:
		names = []
	newHookups = {yourname: names}
	hookups.update(newHookups)
	for i in range(len(names)):
		if names[i] == hookup:
			return hookups
	# otherwise, if it exits the for loop, the name isnt there so we have to add it
	names.append(hookup)
	return hookups

def add():
	while True:
		names = []
		yourname = raw_input("Please enter your name: ")
		if yourname == 'done':
			break
		#if hookups.has_key(yourname):
			# just append the list of names to the names that are already there
		#	names = hookups.get(yourname) #returns all the names associated with that name
		#newHookups = {yourname: names}
		#hookups.update(newHookups)
		while True:
			hookup = raw_input("Please enter someone you've hooked up with: ")
			if hookup == 'done':
				break
			else: # add the hookup to the list
				hookups = addHookup(yourname, hookup)
				hookups = addHookup(hookup, yourname)
				print hookups

hookups = {}
while True:
	mode = raw_input("Would you like to add hookups or search for your Eskimo brothers and sisters? ")
	if mode == "add":
		add()
	elif mode == "search":
		searchName = raw_input("Please enter your name: ")
		search(searchName)
	elif mode == 'exit':
		break
	else:
		print "Please type 'add', 'search', or 'exit'"



