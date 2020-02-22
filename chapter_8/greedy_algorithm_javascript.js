

let states_needed = new Set(["mt", "wa", "or", "id", "nv", "ut","ca", "az"]);

// You also need the list of stations that you’re choosing from. I chose to
// use a hash for this:
// The keys are station names, and the values are the states they cover.
let stations = {};
stations["kone"] = new Set(["id", "nv", "ut"]);
stations["ktwo"] = new Set(["wa", "id", "mt"]);
stations["kthree"] = new Set(["or", "nv", "ca"]);
stations["kfour"] = new Set(["nv", "ut"]);
stations["kfive"] = new Set(["ca", "az"]);

// Finally, you need something to hold the final set of stations you’ll use:
final_stations = new Set();

// And you loop until states_needed is empty. Here’s the full code for
while (states_needed.size) {
    let best_station = null;
    let states_covered = new Set();
    for (let station in stations) {
      let states = stations[station];
      let covered = new Set([...states_needed].filter((x) => states.has(x)));
      if (covered.size > states_covered.size) {
        best_station = station;
        states_covered = covered;
      }
    }
    states_needed = new Set([...states_needed].filter((x) => !states_covered.has(x)));
    final_stations.add(best_station);
  }
  
  console.log(final_stations); 