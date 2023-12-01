import re

def concat_first_last_digit(string):
    return string[0] + string[-1]
    
    
def remove_non_digits(string):
    result = ""
    for char in string:
        if char.isdigit():
            result += char

    return result

file = open("input.txt", "r")

sum = 0

for line in file:
    only_digits = remove_non_digits(line)
    first_last_concat = concat_first_last_digit(only_digits)
    sum += int(first_last_concat)

print(sum)

file.close()



