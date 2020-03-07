# Name: Kevin Cui
# Date: 2020-02-05
# Description: Card Class

import random

class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.totalPoints = 0
        self.longestSuit = ('', 0)

    def __str__(self):
        ret = self.name+': '
        for h in self.hand:
            ret += str(h)+', '
        ret = ret[:-2]+'; points: '+str(self.findTotalPoints())+'; longest suit: '+str(self.findLongestSuit()[1])+' '+self.findLongestSuit()[0]
        return ret

    def __gt__(self, other):
        return self.totalPoints > other.totalPoints

    def addCard(self, card):
        self.hand.append(card)
        self.totalPoints += card.points
        cnt = 0
        for h in self.hand:
            if h.suit == card.suit:
                cnt += 1
        if cnt > self.longestSuit[1]:
            self.longestSuit = (card.suit, cnt)

    def findTotalPoints(self):
        return self.totalPoints

    def findLongestSuit(self):
        return self.longestSuit

    def findLongestSuitPair(self, partner):
        suits = ['D', 'C', 'H', 'S']
        cnt = [0]*4
        for h in self.hand:
            cnt[suits.index(h.suit)] += 1
        for h in partner.hand:
            cnt[suits.index(h.suit)] += 1
        return (suits[cnt.index(max(cnt))], max(cnt))

class Card(object):

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.points = 0
        syst = {'A':4, 'K':3, 'Q':2, 'J':1}
        if face in syst:
            self.points = syst[face]

    def __str__(self):
        return self.suit + self.face

names = ['North', 'West', 'South', 'East']
players = list(map(Player, names))

suits = ['D', 'C', 'H', 'S']
faces = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []
for s in suits:
    for f in faces:
        deck.append(Card(s, f))

random.shuffle(deck)

for d in range(len(deck)):
    players[d%4].addCard(deck[d])

pair1 = players[0].findLongestSuitPair(players[2])
pair2 = players[1].findLongestSuitPair(players[3])

players.sort()
players.reverse()

print('PLAYERS (in order of points)\n'+'\n'.join(map(str, players)))
print('Longest suit between pairs North and South', *pair1)
print('Longest suit between pairs West and East', *pair2)
    
