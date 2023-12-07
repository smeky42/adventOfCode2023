
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # print(f"Compare \n {arr[j]} {arr[j+1]}")

            if poker_hand_ranking(arr[j]) > poker_hand_ranking(arr[j+1]): #arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            elif poker_hand_ranking(arr[j]) == poker_hand_ranking(arr[j+1]):
                # print(f"Equal Hand Ranking \n {arr[j]} {arr[j+1]}")
                if poker_card_ranking(arr[j],arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


def poker_card_ranking(hand1, hand2):
    hand1 = hand1.split()[0]
    hand2 = hand2.split()[0]
    ranks = 'J23456789TQKA'
    
    for rank1, rank2 in zip(hand1, hand2): 
        if ranks.index(rank1) > ranks.index(rank2):
            # print(f"{hand1} hand1 wins")
            return True
        elif ranks.index(rank1) < ranks.index(rank2): 
            # print(f"{hand2} hand2 wins")
            return False
    
    print(f"{hand1} and {hand2} are equal")
    return True
    

def find_leading_card(hand, count):
    if count == 1:
        return highest_card(hand)

    for card in hand: 
        if hand.count(card) == count and card != 'J':  
            return card
    
    return find_leading_card(hand, count-1)

    return '2'


def highest_card(hand):
    ranks = 'J23456789TQKA'
    highest_card = 'J'

    for card in hand: 
        if ranks.index(highest_card) < ranks.index(card):
            highest_card = card

    return highest_card


def poker_hand_ranking(hand):
    hand = hand.split()[0]
    ranks = '23456789TJQKA'

    # print(f"Rank hand {hand}")

    rank_counts = {rank: hand.count(rank) for rank in ranks}
    if len(set(hand)) == 1:
        if 5 in rank_counts.values():
            return 900 # + ranks.index(find_leading_card(hand, 5)) # Five of a kind
    elif len(set(hand)) == 2:
        if 4 in rank_counts.values():
            if 'J' in hand: 
                return poker_hand_ranking(hand.replace('J', find_leading_card(hand,4)))
            return 800 # + ranks.index(find_leading_card(hand, 4)) # Four of a kind
        else:
            if 'J' in hand: 
                return poker_hand_ranking(hand.replace('J', find_leading_card(hand,4)))
            return 700# + ranks.index(find_leading_card(hand, 3)) # Full house
    elif len(set(hand)) == 3:
        if 3 in rank_counts.values():
            if 'J' in hand: 
                return poker_hand_ranking(hand.replace('J', find_leading_card(hand,3)))
            return 400 #+ ranks.index(find_leading_card(hand, 3))  # Three of a kind
        else:
            if 'J' in hand: 
                return poker_hand_ranking(hand.replace('J', find_leading_card(hand,3)))
            return 300 #+ ranks.index(find_leading_card(hand, 2)) # Two pairs
    elif len(set(hand)) == 4:
        if 'J' in hand: 
            return poker_hand_ranking(hand.replace('J', find_leading_card(hand,2)))
        return 200 #+ ranks.index(find_leading_card(hand, 2))  # One pair
    elif len(set(hand)) == 5:
        if 'J' in hand: 
            return poker_hand_ranking(hand.replace('J', find_leading_card(hand,1)))
        return 100 #+ ranks.index(highest_card(hand)) # High card


def multiply_numbers_with_rank(hands):
    result = []
    for i, hand in enumerate(hands):
        number = int(hand.split()[1].replace("\n",""))
        result.append(number * (i+1))
    return result


with open("input.txt", "r") as file:
    hands = file.readlines()

# # print(hands)

hands = bubble_sort(hands)
# print(hands)
with open("output.txt", 'w') as f:
    for item in hands:
        f.write("%s \n" % item.split()[0])

hands = multiply_numbers_with_rank(hands)
# print(f"Multiply {hands}")
print(f"Sum {sum(hands)}")

