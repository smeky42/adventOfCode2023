def check_card(card):
    splitted_card = card.split('|')
    # print(card)

    list_one = splitted_card[0].split(':')[1].split()
    list_two = splitted_card[1].split()

    list_one = [int(num) for num in list_one]
    list_two = [int(num) for num in list_two]

    points = 0
    for num in list_two:
        if num in list_one:
            if points == 0:
                points = 1
            else: 
                points = points * 2

    # print(points)
    return points


file = open("input.txt", "r")

sum = 0

for card in file:
    sum += check_card(card)
    
print(f"Points: {sum}")