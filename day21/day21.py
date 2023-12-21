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
            print(f"{x},{y} {steps}")
            
            if x > 0 and ground[y][x-1] != "#":
                queue.append((x-1,y,steps+1))
            if x < len(ground[y]) - 1 and ground[y][x+1] != "#":
                queue.append((x+1,y,steps+1))
            if y > 0 and ground[y-1][x] != "#":
                queue.append((x,y-1,steps+1))
            if y < len(ground) - 1 and ground[y+1][x] != "#":
                queue.append((x,y+1,steps+1))
    
    return queue


max_steps = 64
# divisors = find_divisors(max_steps)
endpoints = set()
already_tried = set()
ground = read_file_to_2d_array("input.txt")
x, y = find_start(ground)
walk(x,y, 0)

# for divisor in divisors:
#     walk(x, y, divisor)

print(f"Endpoints: {len(endpoints)}")