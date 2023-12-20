import itertools

def print_2d_char_array(two_d_array):
    rows_as_strings = [''.join(row) for row in two_d_array]
    all_rows = '\n'.join(rows_as_strings)
    
    print(all_rows)

def generate_combinations(line):
    arrangement = line[0]
    pattern = line[1].split(",")

    num_question_marks = arrangement.count('?')
    combinations = list(itertools.product(['#', '.'], repeat=num_question_marks))
    final_strings = []

    for combination in combinations:
        temp_a = arrangement
        for replacement in combination:
            temp_a = temp_a.replace('?', replacement, 1)

        if check_pattern(temp_a, pattern):
            final_strings.append(temp_a)

    return final_strings
    
def check_pattern(arrangement, pattern):
    arrangement = arrangement.split(".")
    arrangement = [str(len(x)) for x in arrangement if x]
    # print(f"Check: {arrangement} {pattern}")
    return arrangement == pattern


filename = 'input.txt'
lines = []

with open(filename, 'r') as file:
    for line in file:
        lines.append(line.strip().split(' ', 1))

sum = 0
for line in lines:
    combinations = generate_combinations(line)
    sum += len(combinations)

print(f"Sum: {sum}")
