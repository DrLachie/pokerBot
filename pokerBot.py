# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 19:14:24 2016

@author: whitehead
"""

import numpy as np

def main():
    counter = 0
    while(True):
        counter+=1
        #print counter
        remainingCards = generateDeck()
        hand1,remainingCards = dealHand(remainingCards)
        hand2,remainingCards = dealHand(remainingCards)
        compareHands(hand1,hand2)
        if counter>100:
            break
    

def compareHands(hand1,hand2):
    handRankings = {'Straight Flush':1,
                    'Four of a kind':2,
                    'Full House':3,
                    'Flush':4,
                    'Straight':5,
                    'Three of a kind':6,
                    'Two Pair':7,
                    'One Pair':8,
                    'High Card':9}
    
    hand1has = evaluateHand(hand1)
    hand2has = evaluateHand(hand2)    
    
    if handRankings[hand1has] == handRankings[hand2has]:
        splitDraw(hand1has,hand1,hand2)
        
    else:
        if handRankings[hand1has] < handRankings[hand2has]:
            print 'Hand 1 wins with %s over hand 2\'s %s' % (hand1has,hand2has)
        else:
            print 'Hand 2 wins with %s over hand 1\'s %s' % (hand2has,hand1has)
    print '\n'
    
    
def splitDraw(inHand,hand1,hand2):
    hand1faces = [card[0] for card in hand1]
    hand2faces = [card[0] for card in hand2]
    if inHand in ['Straight Flush','Flush','Straight','High Card']:
        high1 = highCard(hand1faces)
        high2 = highCard(hand2faces)
        if high1 == high2:
            print 'Draw'
        else:
            if high1 > high2:
                print 'Hand 1 wins with %s %s high over Hand 2\'s %s' % (inHand,scoreToFace(high1),
                                                                           scoreToFace(high2))            
            else:
                print 'Hand 2 wins with %s %s high over Hand 1\'s %s' % (inHand,scoreToFace(high2),
                                                                           scoreToFace(high1))
    else:
        print 'Still a draw, working on it'
    
    
    
    
def evaluateHand(hand):
    faces = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    readable = [str(x[0]) + ' of '+ x[1] for x in hand]
    print readable
    
    inHand = 'High Card'
 
    pairs = checkForPairs(faces)
    if pairs and (len(pairs)==2):
        inHand = 'One Pair'
    
    if pairs and (len(pairs)==3):
        inHand = 'Three of a kind'    
                 
    if pairs and (len(pairs)==4):
        if (faces.count(faces[0]) == 4 or 
		faces.count(faces[1]) == 4):
		inHand = 'Four of a kind'
	else:
		inHand = 'Two Pair'    
   

    if pairs and (len(pairs)==5):
        inHand = 'Full House'

    if isFlush(suits) and isStraight(faces):
        inHand = 'Straight flush'
    else:
        if isFlush(suits):
            inHand = 'Flush'
        
        if isStraight(faces):
            inHand = 'Straight'
    
    
    return inHand
    
        
def highCard(faces):
    faceValues = faces
    card_scores = {'ace':14,
                   'jack':11,
                   'queen':12,
                   'king':13}
    for i,val in enumerate(faceValues):
        if val in card_scores:
            faceValues[i]=card_scores[val]
    
    highCard = faceValues.index(np.max(faceValues))
    return faces[highCard]
           
def isStraight(faceValues):
    
    card_scores = {'ace':14,
                   'jack':11,
                   'queen':12,
                   'king':13}
                   
    for i,val in enumerate(faceValues):
        if val in card_scores:
            faceValues[i]=card_scores[val]
                 
    if np.max(faceValues) - np.min(faceValues) ==4 and not checkForPairs(faceValues):
        return True
    else:
        lowStraight = [2,3,4,5,14]
        if sorted(faceValues) == lowStraight:
            return True
        else:
            return False
        
    
def isFlush(suits):
    if suits.count(suits[0])==5:
        return True
    else:
        return False

def checkForPairs(faceValues):    
    pairs = [i for i,x in enumerate(faceValues) if faceValues.count(x) > 1]
    if pairs:
        return pairs
    else:
        return False
    
def dealHand(cardsInDeck):
    hand = []
    for i in range(0,5):
        cardDealt,cardsInDeck = dealCard(cardsInDeck)
        hand.append(cardDealt)
    
    return hand,cardsInDeck



def dealCard(cardsInDeck):
    dealt_card = cardsInDeck.pop(np.random.randint(0,len(cardsInDeck)))
    return dealt_card,cardsInDeck


def generateDeck():
    values = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']    
    suits = ['hearts','diamonds','clubs','spades']
    deck = []
    
    for faceValue in values:
        for suit in suits:
            deck.append((faceValue,suit))
    
    return deck

def scoreToFace(cardScore):
    card_scores = {14:'ace',
                   11:'jack',
                   12:'queen',
                   13:'king'}
    
    if cardScore in card_scores:
        return card_scores[cardScore]
    else:
        return cardScore
    
    
    
main()
