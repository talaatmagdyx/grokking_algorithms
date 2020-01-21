#!/usr/bin/env python
# -*- coding: utf-8 -*- 

graph = {}
# add start to hash
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}


infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

def find_lowest_cost_node(costs):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in costs:
		cost = costs[node]
		if cost < lowest_cost and node not in processed:
			lowest_cost = cost
			lowest_cost_node = node
	return lowest_cost_node



# need an array to keep track of all the nodes you’ve already
# processed, because you don’t need to process a node more than once:
processed = []

node = find_lowest_cost_node(costs)

# If you’ve processed all the nodes, this while loop is done.
while node is not None:
	cost = costs[node]
	neighbors = graph[node]
	#Go through all the neighbors of this node.
	for n in neighbors.keys():
		# If it’s cheaper to get to this neighbor
		new_cost = cost + neighbors[n]
		if costs[n] > new_cost:
			costs[n] = new_cost
			# update the cost for this node.
			parents[n] = node
	#This node becomes the new parent for this neighbor.
	processed.append(node)
	#Mark the node as processed.
	node = find_lowest_cost_node(costs)
	#Find the next node to process, and loop.


print(processed)