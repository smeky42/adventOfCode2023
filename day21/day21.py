def print_2d_char_array(two_d_array):
    rows_as_strings = [''.join(row) for row in two_d_array]
    all_rows = '\n'.join(rows_as_strings)
    
    print(all_rows)

def read_file_to_2d_array(filename):
    with open(filename, 'r') as file:
        two_d_array = [list(line.strip()) for line in file]
    return two_d_array

def find_start(ground):
    for i, line in enumerate(ground):
        for j, char in enumerate(line):
            if char != "S":
                continue
            else: 
                print(f"Found Start at ({i},{j})")
                return i, j

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def walk(x,y, steps):
    queue = [(x, y, steps)]
    while queue:
        x, y, steps = queue.pop()
        rest_steps = max_steps - steps

        if steps == max_steps:
            endpoints.add((x,y))
        elif steps < max_steps and (x,y,rest_steps) not in already_tried:
            already_tried.add((x,y,rest_steps))
            print(f'\r{len(endpoints)} - {x},{y} {steps}', end='', flush=True)
        
            if x > 0 and ground[y][x-1] != "#":
                queue.append((x-1,y,steps+1))
            if x < len(ground[y]) - 1 and ground[y][x+1] != "#":
                queue.append((x+1,y,steps+1))
            if y > 0 and ground[y-1][x] != "#":
                queue.append((x,y-1,steps+1))
            if y < len(ground) - 1 and ground[y+1][x] != "#":
                queue.append((x,y+1,steps+1))
    
    return queue

def duplicate_array_horizontal(array, times):
    duplicated_array = [row * times + row * times for row in array]
    return duplicated_array

def duplicate_array_vertically(array, times):
    duplicated_array = array * times + array * times
    return duplicated_array


def blow_up(array, times):
    array = duplicate_array_horizontal(array, times)
    return duplicate_array_vertically(array, times)

max_steps = 1000
# divisors = find_divisors(max_steps)
endpoints = set()
already_tried = set()
ground = read_file_to_2d_array("input_test2.txt")
x, y = find_start(ground)

blow_factor = 100
start_x = blow_factor * len(ground[y]) + x
start_y = blow_factor * len(ground) + y  
ground = blow_up(ground, blow_factor)

walk(start_x,start_y, 0)

# for divisor in divisors:
#     walk(x, y, divisor)

print(f"Endpoints: {len(endpoints)}")