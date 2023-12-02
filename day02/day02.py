import re 

def get_id_of_valid_record(record):
    valid_red = check_if_color_is_valid(record, "red")
    valid_blue = check_if_color_is_valid(record, "blue")
    valid_green = check_if_color_is_valid(record, "green")

    if valid_red & valid_blue & valid_green:
        return int(get_id_of_record(record))
    else: 
        return 0

def get_id_of_record(record):
    match = re.search(r'\d+', record)
    if match:
        return match.group()
    
def check_if_color_is_valid(record, color):
    return {
        'red': lambda: check_highest_numbers_of_color(record, color) <= 12,
        'green': lambda: check_highest_numbers_of_color(record, color) <= 13,
        'blue': lambda: check_highest_numbers_of_color(record, color) <= 14,
    }.get(color, lambda: False)()

def check_highest_numbers_of_color(record, color):
    highest = 0
    matches = re.findall(r'(\d+)\s+' + color, record)
    for match in matches: 
        if int(match) > highest: 
            highest = int(match)

    return highest

def get_power_of_colors(record):
    smallest_red = check_highest_numbers_of_color(record, "red")
    smallest_blue = check_highest_numbers_of_color(record, "blue")
    smallest_green = check_highest_numbers_of_color(record, "green")
    return smallest_red * smallest_blue * smallest_green



file = open("input.txt", "r")

sum = 0
power_sum = 0

for record in file:
    sum += get_id_of_valid_record(record)
    power_sum += get_power_of_colors(record)

print("Sum of valid records: " + str(sum))
print("Sum of the power of minimal colors: " + str(power_sum))

file.close()



