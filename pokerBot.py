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
        print counter
        remainingCards = generateDeck()
        hand1,remainingCards = dealHand(remainingCards)
        evaluateHand(hand1)
        if counter>37000:
            break
    
    
    
def evaluateHand(hand):
    faces = [card[0] for card in hand]
    suits = [card[1] for card in hand]
    readable = [str(x[0]) + ' of '+ x[1] for x in hand]
    print readable
    
    high = highCard(faces)
    
    if high==14 and isStraight and np.min(faces)==2:
        high = 5
    
    score_faces = {14:'ace',11:'jack',12:'queen',13:'king'}
    if high in score_faces:
        high = score_faces[high]    
    
    pairs = checkForPairs(faces)
    if pairs and (len(pairs)==2):
#        for i in pairs:
#            print str(faces[i]) +' of '+suits[i]
        print 'Pair'
    
    if pairs and (len(pairs)==3):
#        for i in pairs:
#            print str(faces[i]) +' of '+suits[i]
        print 'Three of a kind'    
                 
    if pairs and (len(pairs)==4):
 #  	for i in pairs:
 #           print str(faces[i]) +' of '+suits[i]
        if (faces.count(faces[0]) == 4 or 
		faces.count(faces[1]) == 4):
		print 'Four of a kind'
	else:
		print 'Two Pair'    
   

    if pairs and (len(pairs)==5):
        print 'Full House'
        for val in faces:
            if faces.count(val)==3:
                triple = val
            else:
                double = val
        print '%ss over %ss' % (triple,double)
    
    if isFlush(suits) and isStraight(faces):
        print 'Straight flush'
        print '%s high' % high
    else:
        if isFlush(suits):
            print 'Flush'
            print '%s high' % high
        
        if isStraight(faces):
            print 'Straight'
            print '%s high' % high
    
    
    
        
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
    
    
main()
