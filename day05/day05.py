import os
import sys
import threading



def chunk_to_map(id):
    map = chunks[id].split(":")[1].split(os.linesep)
    return [[int(n) for n in s.split()] for s in map if s]

def map_to_map_reverse(seed,map):
    for mapping in map:
        # print(f"Check mapping {mapping}")
        destination_range_start = mapping[1]
        source_range_start = mapping[0]
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

def reverse(start, end):
    location = sys.maxsize - 1
    print(f"started from {start} to {end}")
    for seed in range(start, end):
        mapped = map_to_map_reverse(seed, chunk_to_map(7))
        mapped = map_to_map_reverse(mapped, chunk_to_map(6))
        mapped = map_to_map_reverse(mapped, chunk_to_map(5))
        mapped = map_to_map_reverse(mapped, chunk_to_map(4))
        mapped = map_to_map_reverse(mapped, chunk_to_map(3))
        mapped = map_to_map_reverse(mapped, chunk_to_map(2))
        mapped = map_to_map_reverse(mapped, chunk_to_map(1))

        for start, seed_range in seeds:
            if(start <= mapped <= (start + seed_range)):
                # print(f"{seed} -> {mapped}")
                if seed < location:
                    location = seed
    
    print(f"Lowests location of batch: {location}")

    
for i in range(50, 60):
    start = i * 100000
    end = start + 100000 -1
    t = threading.Thread(target=reverse, args=(start, end))
    t.start()



print(f"Lowest location: {location}")
    