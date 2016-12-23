# graph version

def search(searchName):
	results = []
	if hookups.has_key(searchName) == False:
		print "You are not in our database. Join by typing add!"
	else:
		names = hookups.get(searchName)
		for i in range(len(names)):
			if hookups.has_key(names[i]): #that name has entered hookups
				# add all of the values associated with that name key
				results = results + hookups.get(names[i])
				print "Results from first if statement are:", results
			for ind in range(len(hookups.keys())):
				for index in range(len(hookups.get(hookups.keys()[ind]))): #for each of the names in the list of name associated with key[ind]
					if hookups.get(hookups.keys()[ind])[index] == searchName:
						results.append(hookups.keys()[ind])
						print "Results from iteration", index, "are :", results
		print "Your eskimo siblings are: ", results

hookups = {}
while True:
	mode = raw_input("Would you like to add hookups or search for your Eskimo brothers and sisters? ")
	if mode == "add":
		while True:
			names = []
			yourname = raw_input("Please enter your name: ")
			if yourname == 'done':
				break
			if hookups.has_key(yourname):
				# just append the list of names to the names that are already there
				names = hookups.get(yourname) #returns all the names associated with that name
			newHookups = {yourname: names}
			hookups.update(newHookups)
			while True:
				name = raw_input("Please enter someone you've hooked up with: ")
				if name == 'done':
					break
				names.append(name)
				#print names
				print hookups
	elif mode == "search":
		searchName = raw_input("Please enter your name: ")
		search(searchName)
	elif mode == 'exit':
		break
	else:
		print "Please type 'add', 'search', or 'exit'"



