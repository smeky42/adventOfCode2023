def file_to_arrays(filename):
    with open(filename, 'r') as file:
        text = file.read()

    parts = text.split('\n\n')
    arrays = [[list(line) for line in part.split('\n')] for part in parts]

    return arrays

def print_2d_char_array(two_d_array):
    rows_as_strings = [''.join(row) for row in two_d_array]
    all_rows = '\n'.join(rows_as_strings)
    
    print(all_rows)



def compare_columns(array, i, j):
    column1 = [row[i] for row in pattern]
    column2 = [row[j] for row in pattern]
    # print(f"Compare {i} to {j} is {column1 == column2}")
    return column1 == column2
        

filename = 'input.txt'
patterns = file_to_arrays(filename)

sum = 0
for pattern in patterns:
    # print("---")
    # print_2d_char_array(pattern)
    length_pattern = len(pattern)
    width_pattern = len(pattern[0])

    for i in range(length_pattern - 1):
        mirror_found = True
        l = i 
        r = i+1
        while l >= 0 and r < length_pattern and mirror_found:
            if not pattern[l] == pattern[r]:
                mirror_found = False

            l = l - 1 
            r = r + 1

        if mirror_found:
            print(f"found mirror between row {i} and {i+1} there are {i+1} rows above")
            sum += (i+1)*100


    for j in range(width_pattern - 1):
        mirror_found = True
        l = j 
        r = j+1
        while l >= 0 and r < width_pattern and mirror_found:
            if not compare_columns(pattern, l, r):
                mirror_found = False

            l = l - 1 
            r = r + 1

        if mirror_found:
            print(f"found mirror between column {j} and {j+1} there are {j+1} rows left")
            sum += j+1

print(f"Sum: {sum}")

