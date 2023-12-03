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

def check_array(two_d_array):
    sum = 0
    for i, line in enumerate(two_d_array):
        for j, char in enumerate(line):
            if not char.isdigit() and char != '.':
                print(f"{char} at {i},{j}")

                if j > 0 and two_d_array[i][j-1].isdigit():
                    # print(f"Number W at position ({i}, {j-1}).")
                    sum += read_number(two_d_array, i, j-1)
                if j < len(two_d_array[i]) - 1 and two_d_array[i][j+1].isdigit():
                    # print(f"Number E at position ({i}, {j+1}).")
                    sum += read_number(two_d_array, i, j+1)

                if i > 0 and two_d_array[i-1][j].isdigit():
                    # print(f"Number N at position ({i-1}, {j}).")
                    sum += read_number(two_d_array, i-1, j)

                if i < len(two_d_array) - 1 and two_d_array[i+1][j].isdigit():
                    # print(f"Number S at position ({i+1}, {j}).")
                    sum += read_number(two_d_array, i+1, j)


                if i > 0 and j < len(two_d_array[i]) - 1 and two_d_array[i-1][j+1].isdigit():
                    # print(f"Number NE at position ({i-1}, {j+1}).")
                    sum += read_number(two_d_array, i-1, j+1)

                if i > 0 and j > 0 and two_d_array[i-1][j-1].isdigit():
                    # print(f"Number NW at position ({i-1}, {j-1}).")
                    sum += read_number(two_d_array, i-1, j-1)


                if i < len(two_d_array) - 1 and j < len(two_d_array[i]) - 1 and two_d_array[i+1][j+1].isdigit():
                    # print(f"Number SE at position ({i+1}, {j+1}).")
                    sum += read_number(two_d_array, i+1, j+1)

                if i < len(two_d_array) - 1 and j > 0 and two_d_array[i+1][j-1].isdigit():
                    # print(f"Number SW at position ({i+1}, {j-1}).")
                    sum += read_number(two_d_array, i+1, j-1)

    print_2d_char_array(two_d_array)
    return sum 

def read_number(two_d_array, i, j):
    while j > 0 and two_d_array[i][j-1].isdigit():
         j = j-1 
    
    digit = ""
    while j < len(two_d_array[i]) and two_d_array[i][j].isdigit():
        digit += two_d_array[i][j]
        two_d_array[i][j] = "."
        j = j+1 

    print(digit)
    return int(digit) 


def check_array_gears(two_d_array):
    sum = 0 
    for i, line in enumerate(two_d_array):
        for j, char in enumerate(line):
            if char == '*':
                print(f"{char} at {i},{j}")
                gear_ratio = 1
                gear_count = 0
                
                if j > 0 and two_d_array[i][j-1].isdigit():
                    # print(f"Number W at position ({i}, {j-1}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i, j-1)
                if j < len(two_d_array[i]) - 1 and two_d_array[i][j+1].isdigit():
                    # print(f"Number E at position ({i}, {j+1}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i, j+1)

                if i > 0 and two_d_array[i-1][j].isdigit():
                    # print(f"Number N at position ({i-1}, {j}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i-1, j)

                if i < len(two_d_array) - 1 and two_d_array[i+1][j].isdigit():
                    # print(f"Number S at position ({i+1}, {j}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i+1, j)

                if i > 0 and j < len(two_d_array[i]) - 1 and two_d_array[i-1][j+1].isdigit():
                    # print(f"Number NE at position ({i-1}, {j+1}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i-1, j+1)

                if i > 0 and j > 0 and two_d_array[i-1][j-1].isdigit():
                    # print(f"Number NW at position ({i-1}, {j-1}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i-1, j-1)


                if i < len(two_d_array) - 1 and j < len(two_d_array[i]) - 1 and two_d_array[i+1][j+1].isdigit():
                    # print(f"Number SE at position ({i+1}, {j+1}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i+1, j+1)

                if i < len(two_d_array) - 1 and j > 0 and two_d_array[i+1][j-1].isdigit():
                    # print(f"Number SW at position ({i+1}, {j-1}).")
                    gear_count +=1
                    gear_ratio *= read_number(two_d_array, i+1, j-1)

                if gear_count == 2:
                    print ("Found Gear")
                    sum += gear_ratio
    
    return sum




filename = 'input.txt'
part_numbers = read_file_to_2d_array(filename)
# sum = check_array(part_numbers)
# print(sum)

gear_ratio_sum = check_array_gears(part_numbers)
print(gear_ratio_sum)