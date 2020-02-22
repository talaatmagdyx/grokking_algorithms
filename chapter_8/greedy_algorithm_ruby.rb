
require 'set'

states_needed = Set["mt", "wa", "or", "id", "nv", "ut","ca", "az"] 

# You also need the list of stations that you’re choosing from. I chose to
#use a hash for this:
# The keys are station names, and the values are the states they cover.
stations = {}
stations["kone"] = ["id", "nv", "ut"].to_set
stations["ktwo"] = ["wa", "id", "mt"].to_set
stations["kthree"] = ["or", "nv", "ca"].to_set
stations["kfour"] = ["nv", "ut"].to_set
stations["kfive"] = ["ca", "az"].to_set

# Finally, you need something to hold the final set of stations you’ll use:
final_stations = Set.new

# And you loop until states_needed is empty. Here’s the full code for
while states_needed.length > 0
    best_station = nil
    states_covered = Set.new

    stations.each do |station, states_for_station|
        covered = states_needed & states_for_station
        if covered.length > states_covered.length
            best_station = station
            states_covered = covered
        end
    end
    final_stations.add(best_station)
    # update sates_need 
    states_needed -= states_covered
end
p final_stations.inspect