import functools

file_name = './Day_07/input-advent-07.txt'
# file_name = './Day_07/sample-07.txt'

kinds = list('AKQJT98765432')
kinds_2 = list('AKQT98765432J')

def get_type(cards: str, jokers = False):
    nums = []
    if jokers:
        number_of_jokers = cards.count('J')
        cards = cards.replace('J', '')
    while len(cards) > 0:
        nums.append(cards.count(cards[0]))
        cards = cards.replace(cards[0], '')
    nums.sort(reverse=True)
    if jokers:
        if len(nums) == 0:
            nums.append(number_of_jokers)
        else:
            nums[0] += number_of_jokers
    return nums[0] * (5 - len(nums))

def sorter_cmp(a, b):
    if b[2] != a[2]:
        return a[2] - b[2]
    else:
        for i in range(5):
            delta = kinds.index(b[0][i]) - kinds.index(a[0][i])
            if delta != 0:
                return delta
        return 0

def sorter_cmp_with_jokers(a, b):
    if b[2] != a[2]:
        return a[2] - b[2]
    else:
        for i in range(5):
            delta = kinds_2.index(b[0][i]) - kinds_2.index(a[0][i])
            if delta != 0:
                return delta
        return 0

hands = []
for line in open(file_name):
    hand = line.split()
    cards, bid, t = hand[0], int(hand[1]), get_type(hand[0])
    hands.append([cards, bid, t])
    print(hands[-1], get_type(cards))

# order by type

hands.sort(key=functools.cmp_to_key(sorter_cmp))
print()
[print(hand) for hand in hands]

sum = 0
for index, hand in enumerate(hands):
    sum += hand[1] * (index + 1)

print('Task 1: Winning %d' % sum)

#########################

hands = []
for line in open(file_name):
    hand = line.split()
    cards, bid, t = hand[0], int(hand[1]), get_type(hand[0], True)
    hands.append([cards, bid, t])
    print(hands[-1])
hands.sort(key=functools.cmp_to_key(sorter_cmp_with_jokers))

print()
[print(hand) for hand in hands]

sum = 0
for index, hand in enumerate(hands):
    sum += hand[1] * (index + 1)

print('Task 2: Winning %d' % sum)
