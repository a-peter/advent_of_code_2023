import numpy
import re

def scan(round, r):
    m = r.search(round)
    if m:
        return int(m.group(1))
    else:
        return 0

RED, GREEN, BLUE = 12, 13, 14
reGame = re.compile(r'Game\s(\d+):')
reRound = [ re.compile(r'(\d+) red'), re.compile(r'(\d+) green'), re.compile(r'(\d+) blue') ]
reRed = re.compile(r'(\d+) red')
reGreen = re.compile(r'(\d+) green')
reBlue = re.compile(r'(\d+) blue')

sumOfGames = 0
sumOfPowers = 0
for line in open('./Day_02/input-advent-02.1.txt'):
    # Get game number
    matchGame = reGame.search(line)
    gameNumber = int(matchGame.group(1))
    rounds = line[matchGame.end():].split(';')

    roundMax = [0, 0, 0]
    for round in rounds:
        for i in range(3):
            roundMax[i] = max(roundMax[i], scan(round, reRound[i]))
    if roundMax[0] <= RED and roundMax[1] <= GREEN and roundMax[2] <= BLUE:
        print('Round %d valid' % gameNumber)
        sumOfGames += gameNumber
    power = numpy.prod(roundMax)
    sumOfPowers += power

print('Sum of games: %d' % sumOfGames)
print('Sum of powers: %d' % sumOfPowers)