import sys
sys.setrecursionlimit(100000)

def read_file_to_2d_array(filename):
    with open(filename, 'r') as file:
        two_d_array = [list(line.strip()) for line in file]
    return two_d_array

def print_2d_char_array(two_d_array):
    rows_as_strings = [''.join(row) for row in two_d_array]
    all_rows = '\n'.join(rows_as_strings)
    
    print(all_rows)

def find_start_pipe(pipes):
    for i, line in enumerate(pipes):
        for j, char in enumerate(line):
            if char != "S":
                continue
            else: 
                print(f"Found Start at ({i},{j})")
                return i, j

def follow_pipes(i,j, direction, steps):
    current_pipe = pipes[i][j] 
    print(f"Current pipe {current_pipe}")
    if current_pipe == "S":
        pipe_length = (steps + 1)/2
        print(f"Back at the Start with {steps} steps!")
        print(f"should be {pipe_length} away")

    if current_pipe == "|" and direction == "N":
        my_pipes.append(f"({i},{j})")
        new_direction = "N"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i-1},{j}).''')
        follow_pipes(i-1,j, new_direction, steps + 1)
    
    if current_pipe == "|" and direction == "S":
        my_pipes.append(f"({i},{j})")
        new_direction = "S"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i+1},{j}).''')
        follow_pipes(i+1,j,new_direction, steps + 1)

    if current_pipe == "-" and direction == "W":
        my_pipes.append(f"({i},{j})")
        new_direction = "W"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j-1}).''')
        follow_pipes(i,j-1, new_direction, steps + 1)
    
    if current_pipe == "-" and direction == "E":
        my_pipes.append(f"({i},{j})")
        new_direction = "E"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j+1}).''')
        follow_pipes(i,j+1, new_direction, steps + 1)

    if current_pipe == "L" and direction == "S":
        my_pipes.append(f"({i},{j})")
        new_direction = "E"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j+1}).''')
        follow_pipes(i,j+1, new_direction, steps + 1)
    
    if current_pipe == "L" and direction == "W":
        my_pipes.append(f"({i},{j})")
        new_direction = "N"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i-1},{j}).''')
        follow_pipes(i-1,j, new_direction, steps + 1)

    if current_pipe == "J" and direction == "S":
        my_pipes.append(f"({i},{j})")
        new_direction = "W"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j-1}).''')
        follow_pipes(i,j-1, new_direction, steps + 1)
    
    if current_pipe == "J" and direction == "E":
        my_pipes.append(f"({i},{j})")
        new_direction = "N"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i-1},{j}).''')
        follow_pipes(i-1,j, new_direction, steps + 1)

    if current_pipe == "F" and direction == "N":
        my_pipes.append(f"({i},{j})")
        new_direction = "E"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j+1}).''')
        follow_pipes(i,j+1, new_direction, steps + 1)
    
    if current_pipe == "F" and direction == "W":
        my_pipes.append(f"({i},{j})")
        new_direction = "S"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i+1},{j}).''')
        follow_pipes(i+1,j, new_direction, steps + 1)

    if current_pipe == "7" and direction == "N":
        my_pipes.append(f"({i},{j})")
        new_direction = "W"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j-1}).''')
        follow_pipes(i,j-1, new_direction, steps + 1)
    
    if current_pipe == "7" and direction == "E":
        my_pipes.append(f"({i},{j})")
        new_direction = "S"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i+1},{j}).''')
        follow_pipes(i+1,j, new_direction, steps + 1)


def find_inner_pipe():
    count = 0
    inside = False 

    for i, line in enumerate(pipes):
        inside = False
        bend_before = None

        for j, char in enumerate(line):
            if f"({i},{j})" in my_pipes:
                pipe = True
            else: 
                pipe = False
            
            if inside:
                inside = not pipe or not cross_pipe(char, bend_before)
            else:
                inside = pipe and cross_pipe(char, bend_before)

            if pipe and char in ['L', 'J', '7', 'F']:
                bend_before = char

            if inside and not pipe:
                count += 1
                pipes[i][j] = "I"

            if not inside and not pipe: 
                pipes[i][j] = "O"

    return count


def cross_pipe(char, bend_before):
    if char == '|':
        return True

    if bend_before == 'L' and char == '7':
        return True

    if bend_before == 'F' and char == 'J':
        return True

    return False



filename = 'input.txt'
possible_pipes = ["|","-","L","J","F","7"]

my_pipes = []
pipes = read_file_to_2d_array(filename)
start_i, start_j = find_start_pipe(pipes)
my_pipes.append(f"({start_i},{start_j})")
follow_pipes(start_i+1, start_j, "S", 0)
# print_2d_char_array(pipes)
inner_count = find_inner_pipe()
print_2d_char_array(pipes)
print(f"Inner Pipe: {inner_count}")


