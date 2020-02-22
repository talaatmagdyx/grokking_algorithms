#!/usr/bin/env python
# -*- coding: utf-8 -*- 

states_needed = set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"])

# You also need the list of stations that you’re choosing from. I chose to
#use a hash for this:
# The keys are station names, and the values are the states they cover.
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# Finally, you need something to hold the final set of stations you’ll use:
final_stations = set()

# And you loop until states_needed is empty. Here’s the full code for
while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    final_stations.add(best_station)
    # update sates_need 
    states_needed -= states_covered

print (final_stations)