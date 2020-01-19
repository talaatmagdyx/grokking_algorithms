from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(name):
	return name[-1] == "m"

def search(name):
	search_queue = deque()
	search_queue += graph[name]
	# This array is how you keep track of
	searched = []
	# which people you’ve searched before.
	while search_queue:
		person = search_queue.popleft()
		#Only search this person if you
		if not person in searched:
		#haven’t already searched them.
			if person_is_seller(person):
				print ( person + " is a mango seller!" )
				return True
			else:
				search_queue += graph[person]
				# Marks this person as searched
				searched.append(person)
	return False

search("you")


