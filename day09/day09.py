
def file_to_array(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        array_of_arrays = []
        for line in lines:
            array = list(map(int, line.split()))
            # array.append(None)
            array_of_arrays.append(array)
    return array_of_arrays

def calculate_last_number(numbers):
    # print(f"Calculate: {numbers}")
    diff_numbers = [j-i for i, j in zip(numbers[:-1], numbers[1:])]
    
    if all(num == 0 for num in diff_numbers):
        # print("All numbers in the array are 0.")
        return 0
    else:
        return calculate_last_number(diff_numbers) + diff_numbers[-1]
    
def calculate_first_number(numbers):
    # print(f"Calculate: {numbers}")
    diff_numbers = [j-i for i, j in zip(numbers[:-1], numbers[1:])]
    
    if all(num == 0 for num in diff_numbers):
        # print("All numbers in the array are 0.")
        return 0
    else:
        return diff_numbers[0] - calculate_first_number(diff_numbers)



filename = "input.txt"
reports = file_to_array(filename)
# print(f"Data: {reports}")

sum = 0
for report in reports: 
    sum += report[-1] + calculate_last_number(report)

print(f"Sum Last: {sum}")

sum = 0
for report in reports: 
    sum += report[0] - calculate_first_number(report)

print(f"Sum First: {sum}")