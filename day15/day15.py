with open('input.txt', 'r') as file:
    line = file.readline().strip()
    array = line.split(',')

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.
def apply_rules(s):
    value = 0
    for char in s:
        ascii_code = ord(char)
        value += ascii_code
        value *= 17
        value %= 256
    return value

# Apply the rules to each string in the array
new_array = [apply_rules(s) for s in array]

# print(new_array)
print(sum(new_array))