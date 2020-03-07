# Name: Kevin Cui
# Date: 2020-02-28
# Description: War Game

from Structures import Queue # Import queue data structure for decks and hands
import random

class Player(object): # Define player class

    def __init__(self, name): # Initialize
        self.name = name
        self.hand = Queue()
        self.totalPoints = 0

    def __str__(self): # Output name and hand when printing
        ret = ''
        temp = Queue()
        while not self.hand.isEmpty(): # Get all items in hand ans push back into hand
            card = self.hand.dequeue()
            temp.enqueue(card)
            ret = str(card)+', ' + ret
        ret = self.name+': ' + ret[:-2]
        while not temp.isEmpty():
            self.hand.enqueue(temp.dequeue())
        return ret

    def findTotalPoints(self): # Find total points
        return self.totalPoints

    def __gt__(self, other): # Comparator
        return self.findTotalPoints() > other.findTotalPoints()

    def addCard(self, card): # Add card to hand
        self.hand.enqueue(card)
        self.totalPoints += card.points

    def revealCard(self, out=False): # Remove a card and return it
        if self.hand.isEmpty():
            return -1
        card = self.hand.dequeue()
        self.totalPoints -= card.points
        if out:
            print(self.name+': '+str(card), end=' ')
        return card

    def isLost(self): # Check if there are no cards left in hand
        return self.hand.isEmpty()

class Card(object):

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face
        self.points = 0
        syst = {'A':4, 'K':3, 'Q':2, 'J':1}
        if face in syst:
            self.points = syst[face] + 10
        else:
            self.points = int(face)

    def __str__(self):
        return self.face + self.suit

    def __gt__(self, other):
        return self.points > other.points

    def __eq__(self, other):
        return self.points == other.points

suits = ['♦', '♣', '♥', '♠'] # Suit and face combinations
faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# faces = ['9', '10', 'J', 'Q', 'K', 'A'] # Shrinked deck for testing purposes

deck = []
for f in faces:
    for s in suits:
        deck.append(Card(s, f)) # Create 54 card deck with all suit and face combinations

random.shuffle(deck) # Shuffle the deck

players = [Player('North'), Player('South')]
for d in range(len(deck)):
    players[d%2].addCard(deck.pop()) # Create players and distribute cards to players

predicted = max(players).name # Find predicted winner
print(predicted, 'is the predicted winner of the game\n')

while not players[0].isLost() and not players[1].isLost(): # Play the game until someone loses
    for p in players:
        print(p) # Print current hands
    print()

    card1 = players[0].revealCard(True) # Reveal a card from each hand
    card2 = players[1].revealCard(True)

    print('\n')

    if card1 > card2: # Check who wins the round
        players[0].addCard(card1)
        players[0].addCard(card2)
    elif card2 > card1:
        players[1].addCard(card1)
        players[1].addCard(card2)
    else:
        print('WAR!!!') # If it is a tie, start a war
        warcards = [card1, card2]
        war = True
        while war and not players[0].isLost() and not players[1].isLost() and warcards[len(warcards)-1] == warcards[len(warcards)-2]: # War phase
            for i in range(4):
                if players[0].isLost() or players[1].isLost(): # Check if any player ran out of cards during the war
                    war = False
                    continue
                warcards.append(players[0].revealCard()) # Take four cards from each hand
                warcards.append(players[1].revealCard())
            if war:
                for w in range(0, len(warcards), 2): # Output current war pile
                    if w%8 == 0:
                        print(warcards[w], end=' ')
                    else:
                        print('◼', end=' ')
                print()
                for w in range(1, len(warcards), 2):
                    if (w-1)%8 == 0:
                        print(warcards[w], end=' ')
                    else:
                        print('◼', end=' ')
                print('\n')

        for w in range(0, len(warcards), 2): # Output information of war pile at end
            print(warcards[w], end=' ')
        print()
        for w in range(1, len(warcards), 2):
            print(warcards[w], end=' ')
        print('\n')

        if warcards[len(warcards)-1] > warcards[len(warcards)-2]: # Give cards to winner of war
            for w in warcards:
                players[1].addCard(w)

        elif warcards[len(warcards)-2] > warcards[len(warcards)-1]:
            for w in warcards:
                players[0].addCard(w)

        if players[0].isLost(): # Check if any player ran out of cards during the war
            print(players[0].name, 'does not have enough cards for a war!')

        if players[1].isLost():
            print(players[1].name, 'does not have enough cards for a war!')

print('The predicted winner was', predicted, 'and the winner was', max(players).name) # Output predicted winner and winner
