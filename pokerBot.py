# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 08:33:52 2016

@author: whitehead
"""

import numpy as np

class deckofCards:
    def __init__(self):
        self.isFull = True
        self.hasJokers = False
        self.cards = self.newDeck()
        
    def dealACard(self):
        dealt_card = self.cards.pop(np.random.randint(0,len(self.cards)))
        self.IsFull = False
        return dealt_card
    
    def newDeck(self):
        values = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']    
        suits = ['hearts','diamonds','clubs','spades']  
        deck = []
    
        for faceValue in values:
            for suit in suits:
                deck.append((faceValue,suit)) 
        return deck

class Hand:
    def __init__(self):
        self.cards = []
        self.cards_readable = []
        self.faces = []
        self.suits = []
        self.faceValues = []
        self.handName = ''
        self.ranking = 0
        
    def dealHand(self,deck):
        for i in range(0,5):
            self.cards.append(deck.dealACard())      
        self.faces = [card[0] for card in self.cards]
        self.suits = [card[1] for card in self.cards]
        self.convertToFaveValues()
        self.evaluateHand()  
        self.cards_readable = ['%s of %s' % (card[0], card[1]) for card in self.reordered()]
        return self
    
    def evaluateHand(self):
        self.handName = 'High Card'
        pairs = self.checkForPairs()
        if pairs and (len(pairs)==2):
            self.handName = 'One Pair'
        if pairs and (len(pairs)==3):
            self.handName = 'Three of a kind'    
        if pairs and (len(pairs)==4):
            if (self.faces.count(self.faces[0]) == 4 or 
                self.faces.count(self.faces[1]) == 4):
                    self.handName = 'Four of a kind'
            else:
                self.handName = 'Two Pair'   
        if pairs and (len(pairs)==5):
            self.handName = 'Full House'
                      
        if self.isFlush() and self.isStraight():
            self.handName = 'Straight Flush'
        else:
           if self.isFlush():
               self.handName = 'Flush'
        
           if self.isStraight():
               self.handName = 'Straight'     
    
        handRankings = {'Straight Flush':1,
                        'Four of a kind':2,
                        'Full House':3,
                        'Flush':4,
                        'Straight':5,
                        'Three of a kind':6,
                        'Two Pair':7,
                        'One Pair':8,
                        'High Card':9}    
        self.ranking = handRankings[self.handName]
    
    
    
    def convertToFaveValues(self):
        card_scores = {'ace':14,
                       'jack':11,
                       'queen':12,
                       'king':13}
        for face in self.faces:
            if face in card_scores:
                self.faceValues.append(card_scores[face])
            else:
                self.faceValues.append(face)
        
    def isFlush(self):
        if self.suits.count(self.suits[0])==5:
            return True
        else:
            return False

    def isStraight(self):
        if np.max(self.faceValues) - np.min(self.faceValues) ==4 and not self.checkForPairs():
            return True
        else:
            lowStraight = [2,3,4,5,14]
            if sorted(self.faceValues) == lowStraight:
                return True
            else:
                return False    
    
    def checkForPairs(self):    
        pairs = [i for i,x in enumerate(self.faceValues) if self.faceValues.count(x) > 1]
        if pairs:
            return pairs
        else:
            return False
    
    def reordered(self):
        cards = sorted([card for card in self.cards], key=lambda card:card[0])
        return cards
        
        
def findWinner(hand1,hand2):
    #lower is better - shutup
    if hand1.ranking < hand2.ranking:
        return 'Hand 1 is the winner'
    if hand1.ranking > hand2.ranking:
        return 'Hand 2 is the winner'
        
    if hand1.ranking == hand2.ranking:
        return evaluateDraw(hand1,hand2)
        
def evaluateDraw(hand1,hand2):
    
    if hand1.handName in ['Straight Flush','Flush','Straight','High Card']:
        hand1faces = sorted(hand1.faceValues,reverse=True)
        hand2faces = sorted(hand2.faceValues,reverse=True)
        winnerChosen = False        
        for card1,card2 in zip(hand1faces,hand2faces):
            if card1 == card2:
                pass
            else:
                if card1 > card2 and not winnerChosen:
                    winner = 'Player 1 wins with highest card %s' % card1
                    winnerChosen = True
                if card2 > card1 and not winnerChosen:
                    winner = 'Player 2 wins with highest card %s' % card2 
                    winnerChosen = True
        if not winnerChosen:
            winner = 'Draw, identical hands'
                                        
    if hand1.handName in  ['One Pair','Three of a kind']:
        for card in hand1.faces:
            if hand1.faces.count(card)>=2:
                hand1has = card
        for card in hand2.faces:
            if hand2.faces.count(card)>=2:
                hand2has = card
        if hand1has == hand2has:
            winner = "I've decided this is a draw, both players have %ss" % hand1has
        if hand1has > hand2has:
            winner = 'Player 1 is the winner pair of %ss beats pair of %ss' % (hand1has,hand2has)
        if hand2has > hand1has:
            winner = 'Player 2 is the winner pair of %ss beats pair of %ss' % (hand2has,hand1has)
            
    
    if hand1.handName in  ['Full House']:
        for card1,card2 in zip(hand1.faceValues,hand2.faceValues):
            if hand1.faceValues.count(card1) == 3:
                hand1three = card1
            if hand1.faceValues.count(card1) == 2:
                hand1two = card1
            if hand2.faceValues.count(card2) == 3:
                hand2three = card2
            if hand2.faceValues.count(card2) == 2:
                hand2two = card2
        print hand1.cards
        print hand2.cards
        print 'Hand 1 has %ss over %ss' % (hand1three,hand1two)
        print 'Hand 2 has %ss over %ss' % (hand2three,hand2two)
        if hand1three > hand2three:
            winner = 'Hand 1 wins'
        else:
            winner = 'Hand 2 wins'
    
    if hand1.handName in  ['Two Pair']: 
         hand1pairs = sorted([card for card in hand1.faceValues 
                             if hand1.faceValues.count(card)== 2],reverse=True)
         hand2pairs = sorted([card for card in hand1.faceValues 
                             if hand1.faceValues.count(card)== 2],reverse=True)        

         if hand1pairs[0] > hand2pairs[0]:
             print 'Player 1 wins'
         if hand1pairs[0] < hand2pairs[0]:
             print 'Player 2 wins'
         
         if hand1pairs[0] == hand2pairs[0] and hand1pairs[2]==hand2pairs[2]:
             winner = "I've decided this is a draw, both players have pairs of %ss and %ss" % (hand1pairs[0],hand1pairs[2])
             
         if hand1pairs[0] == hand2pairs[0] and hand1pairs[2] > hand2pairs[2]:
             winner = 'Player 1 wins'
         if hand1pairs[0] == hand2pairs[0] and hand1pairs[2] < hand2pairs[2]:
             winner = 'Player 2 wins'
             
    return winner


for i in range(0,1):
    deck = deckofCards()
    player1 = Hand().dealHand(deck)
    player2 = Hand().dealHand(deck)

    print player1.cards_readable
    print player2.cards_readable
    print 'Player1 has %s \nPlayer2 has %s' % (player1.handName,player2.handName)
    print findWinner(player1,player2)
   
 