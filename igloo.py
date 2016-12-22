print "This is my first python program!"
#a = input("Please enter a number: ")
#b = input("Please enter another number: ")
#print 'the sum of your numbers is', a+b

hookups = {}
while True:
	mode = raw_input("Would you like to add hookups or search for your Eskimo brothers and sisters? ")
	if mode == "add":
		#hookups = {}
		while True:
			i = 0
			names = []
			yourname = raw_input("Please enter your name: ")
			if yourname == 'done':
				break
			if hookups.has_key(yourname):
				# just append the list of names to the names that are already there
				names = hookups.get(yourname) #returns all the names associated with that name
			#else:
			newHookups = {yourname: names}
			hookups.update(newHookups)
			while True:
				name = raw_input("Please enter someone you've hooked up with: ")
				if name == 'done':
					break
				names.append(name)
				print names
				print hookups
				i = i+1
	elif mode == "search":
		#do the searching algorithm here
		print "searching algorithm activated"
		searchName = raw_input("Please enter your name: ")
		if hookups.has_key(searchName) == False:
			print "You are not in our database. Join by typing add!"
		elif:

	elif mode == 'exit':
		break
	else:
		print "Please type 'add', 'search', or 'exit'"

