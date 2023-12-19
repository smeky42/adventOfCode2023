import sys
sys.setrecursionlimit(15000)

def print_2d_char_array(two_d_array):
    rows_as_strings = [''.join(row) for row in two_d_array]
    all_rows = '\n'.join(rows_as_strings)
    
    print(all_rows)

def get_height(filename):
    with open(filename, 'r') as file:
        height = 0
        max_height = 0
        min_height = 0
        for line in file: 
            direction, meter, color = line.rstrip("\n").split(' ')
            # print(f"D: {direction}, {meter}m")

            if direction == "D":
                height += int(meter)

            if direction == "U":
                height -= int(meter)

            if max_height < height:
                max_height = height

            if min_height > height:
                min_height = height 
        
    print(f"Height: {min_height} to {max_height} -> {abs(min_height) + abs(max_height) + 1}")
    return abs(min_height), abs(min_height) + abs(max_height) + 1

def get_widht(filename):
    with open(filename, 'r') as file:
        width = 0
        max_width = 0
        min_width = 0
        for line in file: 
            direction, meter, color = line.rstrip("\n").split(' ')
            # print(f"D: {direction}, {meter}m")


            if direction == "L":
                width -= int(meter)

            if direction == "R":
                width += int(meter)

            if max_width < width:
                max_width = width

            if min_width > width:
                min_width = width 
        
    print(f"Width: {min_width} to {max_width} -> {abs(min_width) + abs(max_width) + 1}")
    return abs(min_width), abs(min_width) + abs(max_width) + 1

def dig(start_x, start_y,filename):
    x = start_x
    y = start_y
    ground[y][x] = "S"
    with open(filename, 'r') as file:
        for line in file: 
            direction, meter, color = line.rstrip("\n").split(' ')
            x, y = dig_cube(x, y, direction, int(meter))


def dig_cube(x, y, d, m):
    # print_2d_char_array(ground)
    # print(f"Dig from {x},{y} {d} {m}m")
    if d == "U":
        for i in range(m):
            ground[y - i][x] = "#"
        return x, y - m
    if d == "D":
        for i in range(m):
            ground[y + i][x] = "#"
        return x, y + m
    if d == "L":
        for i in range(m):
            ground[y][x - i] = "#"
        return x - m, y
    if d == "R":
        for i in range(m):
            ground[y][x + i] = "#"
        return x + m, y
    

def fill(x,y):
    queue = [(x, y)]
    while queue:
        x, y = queue.pop()

        # print(f"{x},{y}")
        if ground[y][x] == ".":  
            ground[y][x] = "#" 

            if x > 0:
                queue.append((x-1,y))
            if x < len(ground[y]) - 1:
                queue.append((x+1,y))
            if y > 0:
                queue.append((x,y-1))
            if y < len(ground) - 1:
                queue.append((x,y+1))


    

def count_hash():
    count = 0

    for row in ground:
        for cell in row:
            if cell == "#":
                count += 1

    return count

filename = 'input.txt'
start_x, width = get_widht(filename)
start_y, height = get_height(filename)
ground = [["." for _ in range(height*2 + 2)] for _ in range(width*2 + 2)]

dig(start_x+1, start_y+1,filename)
ground[start_y+1][start_x+1] = "S"
# print_2d_char_array(ground)
print("\n\n")
fill(start_x+2,start_y+1)
print_2d_char_array(ground)
print(f"Count: {count_hash() + 1}")
