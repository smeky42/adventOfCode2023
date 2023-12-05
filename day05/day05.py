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


with open("input.txt", "r") as file:
    data = file.read()
    chunks = data.split(os.linesep + os.linesep)

    seeds = chunks[0].split(": ")[1].split()
    seeds = [int(num) for num in seeds]
    

# print(seeds)

location = sys.maxsize

for seed in seeds:
   
    mapped = map_to_map(seed, chunk_to_map(1))
    mapped = map_to_map(mapped, chunk_to_map(2))
    mapped = map_to_map(mapped, chunk_to_map(3))
    mapped = map_to_map(mapped, chunk_to_map(4))
    mapped = map_to_map(mapped, chunk_to_map(5))
    mapped = map_to_map(mapped, chunk_to_map(6))
    mapped = map_to_map(mapped, chunk_to_map(7))

    print(f"Seed {seed} mapped to location {mapped}")
    if(location > mapped):
        location = mapped 

print(f"Lowest location: {location}")
    