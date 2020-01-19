@graph = {}
@graph["you"] = ["alice", "bob", "claire"]
@graph["bob"] = ["anuj", "peggy"]
@graph["alice"] = ["peggy"]
@graph["claire"] = ["thom", "jonny"]
@graph["anuj"] = []
@graph["peggy"] = []
@graph["thom"] = []
@graph["jonny"] = []

def person_is_seller(name)
	name[-1] == 'm'
end

def search(name)
	search_queue = []
	search_queue += @graph[name]
	# This array is how you keep track of
	searched = []
	# which people you’ve searched before.
	while search_queue 
		person = search_queue.shift
		#Only search this person if you
		if not searched.include? person
		#haven’t already searched them.
			if person_is_seller(person)
				puts ( person + " is a mango seller!" )
				return true
			else
				search_queue += @graph[person]
				# Marks this person as searched
				searched << person
			end
		end
	end
	return false
end
search("you")


