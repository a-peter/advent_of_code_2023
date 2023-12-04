sum_of_values = 0
card_infos = [] # list of [number of cards, number of wins, value of wins for task 1]
NUM_CARDS = 0
NUM_MATCH = 1
NUM_WIN = 2

def check_card_present(card_number):
    while len(card_infos) < card_number:
        card_infos.append([0, 0, 0])
    return card_infos[card_number - 1]

def add_match(card_number, number_of_cards):
    card_infos[card_number - 1][0] += number_of_cards
    
card_number = 0
for line in open('./Day_04/input-advent-04.1.txt'):
    card_number += 1
    card_info = check_card_present(card_number)
    card_info[NUM_CARDS] += 1

    # prepare line
    numbers = line.split(':')[1].split('|')
    winning_numbers = [int(n) for n in numbers[0].split()]
    own_numbers = [int(n) for n in numbers[1].split()]
    
    value = 0
    for number in own_numbers:
        if number in winning_numbers:
            card_info[NUM_MATCH] += 1
            check_card_present(card_number + card_info[NUM_MATCH])
            add_match(card_number + card_info[NUM_MATCH], card_info[NUM_CARDS])
            # print(number)
            if card_info[2] == 0:
                card_info[2] = 1
            else:
                card_info[2] *= 2
    sum_of_values += card_info[2]

print('Sum of values: %d' % sum_of_values)

number_of_cards = 0
for i in range(len(card_infos)):
    number_of_cards += card_infos[i][NUM_CARDS]

print('Number of scratchcards: %d' % number_of_cards)