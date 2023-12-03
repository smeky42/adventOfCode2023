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

def read_number(two_d_array, i, j):
    while j > 0 and two_d_array[i][j-1].isdigit():
         j = j-1 
    
    digit = ""
    while j < len(two_d_array[i]) and two_d_array[i][j].isdigit():
        digit += two_d_array[i][j]
        two_d_array[i][j] = "."
        j = j+1 

    # print(digit)
    return int(digit)

def check_array(two_d_array):
    sum = 0
    gear_sum = 0
    for i, line in enumerate(two_d_array):
        for j, char in enumerate(line):
            if not char.isdigit() and char != '.':
                # print(f"{char} at {i},{j}")

                gear_count = 0
                gear_ratio = 1

                if j > 0 and two_d_array[i][j-1].isdigit():
                    # print(f"Number W at position ({i}, {j-1}).")
                    number = read_number(two_d_array, i, j-1)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number


                if j < len(two_d_array[i]) - 1 and two_d_array[i][j+1].isdigit():
                    # print(f"Number E at position ({i}, {j+1}).")
                    number = read_number(two_d_array, i, j+1)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number

                if i > 0 and two_d_array[i-1][j].isdigit():
                    # print(f"Number N at position ({i-1}, {j}).")
                    number = read_number(two_d_array, i-1, j)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number

                if i < len(two_d_array) - 1 and two_d_array[i+1][j].isdigit():
                    # print(f"Number S at position ({i+1}, {j}).")
                    number = read_number(two_d_array, i+1, j)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number


                if i > 0 and j < len(two_d_array[i]) - 1 and two_d_array[i-1][j+1].isdigit():
                    # print(f"Number NE at position ({i-1}, {j+1}).")
                    number = read_number(two_d_array, i-1, j+1)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number

                if i > 0 and j > 0 and two_d_array[i-1][j-1].isdigit():
                    # print(f"Number NW at position ({i-1}, {j-1}).")
                    number = read_number(two_d_array, i-1, j-1)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number


                if i < len(two_d_array) - 1 and j < len(two_d_array[i]) - 1 and two_d_array[i+1][j+1].isdigit():
                    # print(f"Number SE at position ({i+1}, {j+1}).")
                    number = read_number(two_d_array, i+1, j+1)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number

                if i < len(two_d_array) - 1 and j > 0 and two_d_array[i+1][j-1].isdigit():
                    # print(f"Number SW at position ({i+1}, {j-1}).")
                    number = read_number(two_d_array, i+1, j-1)
                    sum += number
                    if char == '*':
                        gear_count +=1
                        gear_ratio *= number
                
                if gear_count == 2:
                    # print ("Found Gear")
                    gear_sum += gear_ratio

    # print_2d_char_array(two_d_array)
    return sum, gear_sum


filename = 'input.txt'
part_numbers = read_file_to_2d_array(filename)
print(check_array(part_numbers))
