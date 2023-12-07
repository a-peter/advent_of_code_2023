import functools
import math

kinds = list('AKQJT98765432')
kinds_2 = list('AKQT98765432J')
# FIVE, FOUR, FULL, THREE, TWO, ONE, HIGH = 6, 5, 4, 3, 2, 1, 0
def get_type(cards: str):
    nums = []
    while len(cards) > 0:
        nums.append(cards.count(cards[0]))
        cards = cards.replace(cards[0], '')
    nums.sort(reverse=True)
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


hands = []
# for line in open('./Day_07/input-advent-07.txt'):
for line in open('./Day_07/sample-07.txt'):
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