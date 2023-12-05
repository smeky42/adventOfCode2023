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

visited_soil = set()
visited_fertilizer = set()
visited_water = set()
visited_light = set()
visited_temperature = set()
visited_humidity = set()
visited_location = set()

for start, seed_range in seeds:
    print(f"Working on {start}, with range {seed_range}")
    for seed in range(start, start + seed_range):
        mapped = map_to_map(seed, chunk_to_map(1))
        visited_soil.add(mapped)
    
    print(f"Soil to visit: {len(visited_soil)}")
    for soil in visited_soil:
        mapped = map_to_map(soil, chunk_to_map(2))
        visited_fertilizer.add(mapped)

    print(f"Fertilizer to visit: {len(visited_fertilizer)}")
    for fertilizer in visited_fertilizer:
        mapped = map_to_map(fertilizer, chunk_to_map(3))
        visited_water.add(mapped)

    print(f"Water to visit: {len(visited_water)}")
    for water in visited_water:
        mapped = map_to_map(water, chunk_to_map(4))
        visited_light.add(mapped)

    print(f"Light to visit: {len(visited_light)}")
    for light in visited_light:
        mapped = map_to_map(light, chunk_to_map(5))
        visited_temperature.add(mapped)

    print(f"Temerature to visit: {len(visited_temperature)}")
    for temperature in visited_temperature:
        mapped = map_to_map(temperature, chunk_to_map(6))
        visited_humidity.add(mapped)

    print(f"Humidity to visit: {len(visited_humidity)}")
    for humidity in visited_humidity:
        mapped = map_to_map(humidity, chunk_to_map(7))
        visited_location.add(mapped)

    print(f"Minimal Visited in Set: {min(visited_location)}")



print(f"Lowest location: {location}")
    