def check_card(card):
    splitted_card = card.split('|')

    list_one = splitted_card[0].split(':')[1].split()
    list_two = splitted_card[1].split()

    list_one = [int(num) for num in list_one]
    list_two = [int(num) for num in list_two]

    hits = 0
    for num in list_two:
        if num in list_one:
            hits += 1

    return hits

def get_card_number(card):
    split_strings = card.split(':')
    card_string = split_strings[0].strip()
    card_parts = card_string.split(' ')
    card_number = int(card_parts[-1])

    return int(card_number)


with open("input.txt", "r") as file:
    lines = file.readlines()

for index, card in enumerate(lines):
    hits = check_card(card)
    number = get_card_number(card)
    # print(f"Line {index}: {card.strip()} has {hits} hits.")
    for hit in range(hits): 
        # print(f"Card {number + hit} is duplicated")
        lines.append(lines[number + hit])

    
print(f"Cards: {len(lines)}")