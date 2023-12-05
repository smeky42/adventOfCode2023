import os
import sys


def chunk_to_map(id):
    map = chunks[id].split(":")[1].split(os.linesep)
    return [[int(n) for n in s.split()] for s in map if s]

def map_to_map(seed,map):
    for mapping in map:
        # print(f"Check mapping {mapping}")
        destination_range_start = mapping[0]
        source_range_start = mapping[1]
        range_length = mapping[2]
        
        if seed >= source_range_start and seed <= (source_range_start + range_length):
            offset = seed - source_range_start
            # print(f"Offset {offset}")
            mapped = destination_range_start + offset
            # print(f"Seed number {seed} corresponds number {mapped} because of {offset}")

            return mapped 
    
    return seed

def merge_touples(tuples): 
    tuples.sort()

    merged = [tuples[0]]
    for current in tuples:
        previous = merged[-1]
        if current[0] <= previous[1]:
            upper_bound = max(previous[1], current[1])
            merged[-1] = (previous[0], upper_bound) 
        else:
            merged.append(current)

    return merged


with open("input.txt", "r") as file:
    data = file.read()
    chunks = data.split(os.linesep + os.linesep)

    seeds = chunks[0].split(": ")[1].split()
    seeds = [int(num) for num in seeds]
    seeds = list(zip(seeds[::2], seeds[1::2]))
    print(f"Tuples: {seeds}")
    seeds = merge_touples(seeds)
    print(f"Merged: {seeds}")
    

# print(seeds)

location = sys.maxsize - 1

visited_soil = []
visited_fertilizer = []
visited_water = []
visited_light = []
visited_temperature = []
visited_humidity = []

for start, seed_range in seeds:
    print(f"Working on {start}, with range {seed_range}")
    for seed in range(start, start + seed_range):
        mapped = map_to_map(seed, chunk_to_map(1))
        if mapped in visited_soil: 
            break
        
        visited_soil.append(mapped)
        mapped = map_to_map(mapped, chunk_to_map(2))
        if mapped in visited_fertilizer: 
            break
        
        visited_fertilizer.append(mapped)
        mapped = map_to_map(mapped, chunk_to_map(3))
        if mapped in visited_water: 
            break
        
        visited_water.append(mapped)
        mapped = map_to_map(mapped, chunk_to_map(4))
        if mapped in visited_light: 
            break
        
        visited_light.append(mapped)
        mapped = map_to_map(mapped, chunk_to_map(5))
        if mapped in visited_temperature: 
            break
        
        visited_temperature.append(mapped)
        mapped = map_to_map(mapped, chunk_to_map(6))

        if mapped in visited_humidity: 
            break
        
        visited_humidity.append(mapped)
        mapped = map_to_map(mapped, chunk_to_map(7))

        # print(f"Seed {seed} mapped to location {mapped}")
        if(location > mapped):
            location = mapped 

print(f"Lowest location: {location}")
    