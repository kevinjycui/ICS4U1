# Name: Kevin Cui
# Date: 2020-02-03
# Description: Python Review

# 1
for i in range(2, 21):
    print(list(j for j in range(1, i+1) if i%j == 0))

# 2
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def dayYear(day, month):
    return sum(months[:month-1])+day
day = int(input('Input day\n--> '))
month = int(input('Input month\n--> '))
print(dayYear(day, month))

# 3
n = int(input('Input value of n\n--> '))
e = 1
for i in range(1, n+1):
    fact = 1
    for j in range(2, i+1):
        fact *= j
    e += 1/fact
print(e)

# 4
s = input('Input string\n--> ')
for i in range(len(s)):
    print(s[i:])
print()
for i in range(len(s)):
    print(' '*i+s[i:])
print()
print('-'.join(list(s)))
for i in range(1, len(s)):
    print(' '*i+'-'.join(list(s[:-i])))
print()
print(s[::-1]+s)
for i in range(1, len(s)):
    print(' '*i+s[:-i][::-1]+s[:-i])
print()

# 5
def getCombos(input_list):
    comb = []
    dupl = []
    for i in input_list:
        for j in input_list:
            if i == j:
                dupl.append(str(i)+str(j))
            else:
                comb.append(str(i)+str(j))
    return comb, dupl
sol = getCombos([1, 2, 3, 4])
print('Combinations are:', sol[0])
print('Doubles are:', sol[1])

# 6
marks = []
for i in range(20):
    marks.append(int(input('Input the next mark\n--> ')))
avg = sum(marks)/len(marks)
sqdif = 0
for m in marks:
    sqdif += (m - avg)**2
sqavg = sqdif/len(marks)
from math import sqrt
stdev = sqrt(sqavg)
print('Standard deviation is', stdev)

# 7
import random
def generate(size):
    elements = []
    for i in range(size-1):
        if random.randint(0, 9) == 0:
            elements.append(random.choice((random.randint(-100, -1), random.randint(1, 100))))
        else:
            elements.append(0)
    if len(elements) == elements.count(0):
        elements.append(random.choice((random.randint(-100, -1), random.randint(1, 100))))
    elif random.randint(0, 9) == 0:
        elements.append(random.choice((random.randint(-100, -1), random.randint(1, 100))))
    else:
        elements.append(0)
    while elements.count(0)/size < 0.8:
        elements[elements.index(next(filter(lambda e: e != 0, elements)))] = 0
    return elements

def construct(lst):
    k = len(lst) - lst.count(0)
    val = []
    pos = []
    for l in range(len(lst)):
        if lst[l] != 0:
            val.append(lst[l])
            pos.append(l)
    return val, pos, k

def reconstruct(m, val, pos):
    elements = []
    j = 0
    for i in range(m):
        if j < len(pos) and i == pos[j]:
            elements.append(val[j])
            j += 1
        else:
            elements.append(0)
    return elements

elem = generate(100)
print(elem)
val, pos, k = construct(elem)
print(k)
print(val)
print(pos)
print(reconstruct(100, val, pos))

# 8
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K', 'A']
suits = ['S', 'D', 'H', 'C']

deck = []
for c in cards:
    for s in suits:
        deck.append(c+s)

random.shuffle(deck)

hands = [
    [], [], [], []
    ]

points = [0, 0, 0, 0]
name = ['North', 'West', 'South', 'East']

longs = [
[0, 0, 0, 0], [0, 0, 0, 0]
    ]

table = {'A':4, 'K':3, 'Q':2, 'J':1}

for d in range(len(deck)):
    hands[d%4].append(deck[d])
    card = deck[d][:-1]
    suit = deck[d][len(deck[d])-1]
    if card in table:
        points[d%4] += table[card]
    longs[(d%4)%2][suits.index(suit)] += 1

for p in range(len(points)):
    if points[p] == max(points):
        print(name[p], 'has the most points with a hand of', hands[p])
        print('Longest suit is', suits[longs[p%2].index(max(longs[p%2]))], 'with', max(longs[p%2]), 'cards.')
