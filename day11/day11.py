import numpy as np
import math

def read_file_to_2d_array(filename):
    with open(filename, 'r') as file:
        two_d_array = [list(line.strip()) for line in file]
    return two_d_array

def print_2d_char_array(two_d_array):
    rows_as_strings = [''.join(row) for row in two_d_array]
    all_rows = '\n'.join(rows_as_strings)
    
    print(all_rows)

def duplicate_rows(array):
    new_array = [[row] if not all(val == "." for val in row) else [row, row] for row in array]
    return [item for sublist in new_array for item in sublist]

def replace_dots(array):
    return [[(val if val != "." else "*") for val in row] if all((val == "." or val == "*") for val in row) else row for row in array]

def expand_old_universe(galaxies):
    galaxies = replace_dots(galaxies)
    transposed_galaxies = list(map(list, zip(*galaxies)))
    new_transposed_galaxies = replace_dots(transposed_galaxies)
    galaxies = list(map(list, zip(*new_transposed_galaxies)))
    return galaxies


def expand_universe(galaxies):
    galaxies = duplicate_rows(galaxies)
    transposed_galaxies = list(map(list, zip(*galaxies)))
    new_transposed_galaxies = duplicate_rows(transposed_galaxies)
    galaxies = list(map(list, zip(*new_transposed_galaxies)))
    return galaxies

def enumerate_galaxies(galaxies):
    galaxy_count = 0

    for i, line in enumerate(galaxies):
        for j, char in enumerate(line):
            if char == "#":
                galaxy_count += 1
                galaxies[i][j] = str(galaxy_count)

    return galaxy_count, galaxies


def count_stars(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    count = 0
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    for i in range(x1, x2):
        if galaxies[i][y1] == "*":
            count += 1
    
    for j in range(y1, y2):
        if galaxies[x1][j] == "*":
            count += 1
    
    return count * 10

def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
        
    return abs(x1-x2) + abs(y1-y2) + count_stars(coord1,coord2)

filename = 'input_test.txt'
galaxies = read_file_to_2d_array(filename)
galaxies = expand_old_universe(galaxies)
print_2d_char_array(galaxies)
galaxy_count, galaxies = enumerate_galaxies(galaxies)
print_2d_char_array(galaxies)


print(f"There are {galaxy_count} galaxies")

arr = np.array(galaxies)
dist_all = 0
for i in range(1, galaxy_count+1):
    start_galaxy = np.where(arr == str(i))
    for j in range(i+1, galaxy_count+1):
        end_galaxy = np.where(arr == str(j)) 
        dist = calculate_distance(start_galaxy,end_galaxy)
        dist_all += dist
        # print(f"From {i} to {j} : {dist}")


print(f"Distance between all Galaxies: {dist_all}")


count_stars(coord1, coord2)