import sys
sys.setrecursionlimit(100000)

def read_file_to_2d_array(filename):
    with open(filename, 'r') as file:
        two_d_array = [list(line.strip()) for line in file]
    return two_d_array

def print_2d_char_array(two_d_array):
    # Join each row into a single string
    rows_as_strings = [''.join(row) for row in two_d_array]
    
    # Join all the rows
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
        print(f"Back at the Start with {steps} steps!")
        print(f"should be {(steps + 1)/2} away")

    if current_pipe == "|" and direction == "N":
        pipes[i][j] = str(steps)[-1]
        new_direction = "N"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i-1},{j}).''')
        follow_pipes(i-1,j, new_direction, steps + 1)
    
    if current_pipe == "|" and direction == "S":
        pipes[i][j] = str(steps)[-1]
        new_direction = "S"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i+1},{j}).''')
        follow_pipes(i+1,j,new_direction, steps + 1)

    if current_pipe == "-" and direction == "W":
        pipes[i][j] = str(steps)[-1]
        new_direction = "W"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j-1}).''')
        follow_pipes(i,j-1, new_direction, steps + 1)
    
    if current_pipe == "-" and direction == "E":
        pipes[i][j] = str(steps)[-1]
        new_direction = "E"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j+1}).''')
        follow_pipes(i,j+1, new_direction, steps + 1)

    if current_pipe == "L" and direction == "S":
        pipes[i][j] = str(steps)[-1]
        new_direction = "E"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j+1}).''')
        follow_pipes(i,j+1, new_direction, steps + 1)
    
    if current_pipe == "L" and direction == "W":
        pipes[i][j] = str(steps)[-1]
        new_direction = "N"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i-1},{j}).''')
        follow_pipes(i-1,j, new_direction, steps + 1)

    if current_pipe == "J" and direction == "S":
        pipes[i][j] = str(steps)[-1]
        new_direction = "W"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j-1}).''')
        follow_pipes(i,j-1, new_direction, steps + 1)
    
    if current_pipe == "J" and direction == "E":
        pipes[i][j] = str(steps)[-1]
        new_direction = "N"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i-1},{j}).''')
        follow_pipes(i-1,j, new_direction, steps + 1)

    if current_pipe == "F" and direction == "N":
        pipes[i][j] = str(steps)[-1]
        new_direction = "E"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j+1}).''')
        follow_pipes(i,j+1, new_direction, steps + 1)
    
    if current_pipe == "F" and direction == "W":
        pipes[i][j] = str(steps)[-1]
        new_direction = "S"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i+1},{j}).''')
        follow_pipes(i+1,j, new_direction, steps + 1)

    if current_pipe == "7" and direction == "N":
        pipes[i][j] = str(steps)[-1]
        new_direction = "W"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i},{j-1}).''')
        follow_pipes(i,j-1, new_direction, steps + 1)
    
    if current_pipe == "7" and direction == "E":
        pipes[i][j] = str(steps)[-1]
        new_direction = "S"
        print(f'''{steps}: Heading {direction} follow pipe {current_pipe} at position ({i}, {j}) 
              in direction {new_direction} to ({i+1},{j}).''')
        follow_pipes(i+1,j, new_direction, steps + 1)

    
    



         


filename = 'input.txt'
possible_pipes = ["|","-","L","J","F","7"]
pipes = read_file_to_2d_array(filename)
start_i, start_j = find_start_pipe(pipes)
follow_pipes(start_i+1, start_j, "S", 0)
print_2d_char_array(pipes)
