def concat_first_last_digit(string):
    return string[0] + string[-1]
    
def remove_non_digits(string):
    result = ""
    for char in string:
        if char.isdigit():
            result += char

    return result

def replace_words_with_numbers(string):
    string = string.replace("one","one1one")
    string = string.replace("two","two2two")
    string = string.replace("three","three3three")
    string = string.replace("four","four4four")
    string = string.replace("five","five5five")
    string = string.replace("six","six6six")
    string = string.replace("seven","seven7seven")
    string = string.replace("eight","eight8eight")
    string = string.replace("nine","nine9nine")

    return string 
    
file = open("input.txt", "r")

sum = 0

for line in file:
    no_number_words = replace_words_with_numbers(line)
    only_digits = remove_non_digits(no_number_words)
    first_last_concat = concat_first_last_digit(only_digits)
    sum += int(first_last_concat)

print(sum)

file.close()



