import random,display, turtle
class Game():
    def __init__(self, id):
        self.p1went = False
        self.p2went = False
        self.p3went = False
        self.p4went = False
        self.advanced = True
        self.deck = self.createDeck()
        random.shuffle(self.deck)
        self.p1cards = []
        self.p2cards = []
        self.p3cards = []
        self.p4cards = []
        self.curDeck = []
        for i in range(7):
            self.p1cards.append(self.deck[0])
            self.deck.pop(0)
        for i in range(7):
            self.p2cards.append(self.deck[0])
            self.deck.pop(0)
        for i in range(7):
            self.p3cards.append(self.deck[0])
            self.deck.pop(0)
        for i in range(7):
            self.p4cards.append(self.deck[0])
            self.deck.pop(0)
        self.curDeck.append(self.deck[0])
        if self.curDeck[0][1] == "f" or self.curDeck[0][1] == "w":
            self.curDeck[0][0] = random.randint(0,3)
        self.deck.pop(0)
        self.reverse = False
        self.pickup2 = False
        self.pickupTally = 0
        self.ready = False
        self.display1 = False
        self.display2 = False
        self.display3 = False
        self.display4 = False
        self.id = id

    def Display(self):
        self.display1 = True
        self.display2 = True
        self.display3 = True
        self.display4 = True
        
    def play(self, player, card):
        if card == "d":
            if player == 0:
                self.p1cards.append(self.deck[0])
                self.deck.pop(0)
            elif player == 1:
                self.p2cards.append(self.deck[0])
                self.deck.pop(0)
            elif player == 2:
                self.p3cards.append(self.deck[0])
                self.deck.pop(0)
            else:
                self.p4cards.append(self.deck[0])
                self.deck.pop(0)
            if self.reverse:
                if player == 0:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                elif player == 1:
                    self.p1went = False
                elif player == 2:
                    self.p2went = False
                else:
                    self.p3went = False
            else:
                if player == 0:
                    self.p1went = True
                elif player == 1:
                    self.p2went = True
                elif player == 2:
                    self.p3went = True
                else:
                    self.p4went = True
                    self.resetWent()

        elif card[1] == "d":
            nextP = []
            self.curDeck.append(card)
            if self.reverse:
                if player == 0:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                    nextP = self.p4cards
                elif player == 1:
                    self.p1went = False
                    nextP = self.p1cards
                elif player == 2:
                    self.p2went = False
                    nextP = self.p2cards
                else:
                    self.p3went = False
                    nextP = self.p3cards
                for i in range(len(nextP) - 1):
                    if nextP[i][1] == "d":
                        self.pickup2 = True
                        self.pickupTally += 2
                if not self.pickup2:
                    player -= 1
                    for i in range(2):
                        if player == 0:
                            self.p1cards.append(self.deck[0])
                            self.deck.pop(0)
                        elif player == 1:
                            self.p2cards.append(self.deck[0])
                            self.deck.pop(0)
                        elif player == 2:
                            self.p3cards.append(self.deck[0])
                            self.deck.pop(0)
                        else:
                            self.p4cards.append(self.deck[0])
                            self.deck.pop(0)
                    player +=1
                else:
                    over = True
                    for i in range(len(nextP)):
                        if nextP[i][1] == "d":
                            over = False
                    if over:
                        player -= 1
                        for i in range(2 + self.pickupTally):
                            if player == 0:
                                self.p1cards.append(self.deck[0])
                                self.deck.pop(0)
                            elif player == 1:
                                self.p2cards.append(self.deck[0])
                                self.deck.pop(0)
                            elif player == 2:
                                self.p3cards.append(self.deck[0])
                                self.deck.pop(0)
                            else:
                                self.p4cards.append(self.deck[0])
                                self.deck.pop(0)
                        player +=1
                        self.pickupTally = 0
                        self.pickup2 = False
            else:
                if player == 0:
                    self.p1went = True
                    nextP = self.p2cards
                elif player == 1:
                    self.p2went = True
                    nextP = self.p3cards
                elif player == 2:
                    self.p3went = True
                    nextP = self.p4cards
                else:
                    self.p4went = True
                    self.resetWent()
                    nextP = self.p1cards   
                for i in range(len(nextP) - 1):
                    if nextP[i][1] == "d":
                        self.pickup2 = True
                        self.pickupTally += 2
                if not self.pickup2:
                    player += 1
                    for i in range(2):
                        if player == 0:
                            self.p1cards.append(self.deck[0])
                            self.deck.pop(0)
                        elif player == 1:
                            self.p2cards.append(self.deck[0])
                            self.deck.pop(0)
                        elif player == 2:
                            self.p3cards.append(self.deck[0])
                            self.deck.pop(0)
                        elif player == 3:
                            self.p4cards.append(self.deck[0])
                            self.deck.pop(0)
                        else:
                            self.p1cards.append(self.deck[0])
                            self.deck.pop(0)
                    player -=1
                else:
                    over = True
                    for i in range(len(nextP)):
                        if nextP[i][1] == "d":
                            over = False
                    if over:
                        player += 1
                        for i in range(2 + self.pickupTally):
                            if player == 0:
                                self.p1cards.append(self.deck[0])
                                self.deck.pop(0)
                            elif player == 1:
                                self.p2cards.append(self.deck[0])
                                self.deck.pop(0)
                            elif player == 2:
                                self.p3cards.append(self.deck[0])
                                self.deck.pop(0)
                            elif player == 3:
                                self.p4cards.append(self.deck[0])
                                self.deck.pop(0)
                            else:
                                self.p1cards.append(self.deck[0])
                                self.deck.pop(0)
                        player -=1
                        self.pickupTally = 0
                        self.pickup2 = False
            cards = self.getCards(player)
            for i in range(len(cards)):
                if card == cards[i]:
                    r = i
            cards.pop(r)
             
        elif card[1] == "s":
            self.curDeck.append(card)
            if self.reverse:
                player -= 1
                if player == -1:
                    player = 3
                if player == 0:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                elif player == 1:
                    self.p1went = False
                    self.p2went = False
                    self.p3went = False
                elif player == 2:
                    self.p1went = True
                    self.p2went = False
                    self.p3went = False
                else:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = False
                player += 1
                if player == 4:
                    player = 0
            else:
                player += 1
                if player == 0:
                    self.p1went = True
                    self.p2went = False
                    self.p3went = False
                elif player == 1:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = False
                elif player == 2:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                else:
                    self.p1went = False
                    self.p2went = False
                    self.p3went = False
                    self.resetWent()
                player -= 1
            cards = self.getCards(player)
            for i in range(len(cards)):
                if card == cards[i]:
                    r = i
            cards.pop(r)
            
        elif card[1] == "r":
            self.reverse = not self.reverse
            self.curDeck.append(card)
            if self.reverse:
                if player == 0:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                elif player == 1:
                    self.p1went = False
                elif player == 2:
                    self.p2went = False
                else:
                    self.p3went = False
            else:
                if player == 0:
                    self.p1went = True
                elif player == 1:
                    self.p2went = True
                elif player == 2:
                    self.p3went = True
                else:
                    self.p4went = True
                    self.resetWent()
            cards = self.getCards(player)
            for i in range(len(cards)):
                if card == cards[i]:
                    r = i
            cards.pop(r)
            
        

        elif card[1] == "w":
            self.curDeck.append(card)
            if self.reverse:
                if player == 0:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                elif player == 1:
                    self.p1went = False
                elif player == 2:
                    self.p2went = False
                else:
                    self.p3went = False
            else:
                if player == 0:
                    self.p1went = True
                elif player == 1:
                    self.p2went = True
                elif player == 2:
                    self.p3went = True
                else:
                    self.p4went = True
                    self.resetWent()
            cards = self.getCards(player)
            for i in range(len(cards)):
                card2 = cards[i]
                if card2[1] == "w":
                    r = i
            cards.pop(r)
            
        elif card[1] == "f":
            self.curDeck.append(card)
            if self.reverse:
                if player == 0:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                elif player == 1:
                    self.p1went = False
                elif player == 2:
                    self.p2went = False
                else:
                    self.p3went = False
                player -= 1
                for i in range(4):
                    if player == 0:
                        self.p1cards.append(self.deck[0])
                        self.deck.pop(0)
                    elif player == 1:
                        self.p2cards.append(self.deck[0])
                        self.deck.pop(0)
                    elif player == 2:
                        self.p3cards.append(self.deck[0])
                        self.deck.pop(0)
                    else:
                        self.p4cards.append(self.deck[0])
                        self.deck.pop(0)
                player +=1
            else:
                if player == 0:
                    self.p1went = True
                elif player == 1:
                    self.p2went = True
                elif player == 2:
                    self.p3went = True
                else:
                    self.p4went = True
                    self.resetWent()
                player += 1
                for i in range(4):
                    if player == 0:
                        self.p1cards.append(self.deck[0])
                        self.deck.pop(0)
                    elif player == 1:
                        self.p2cards.append(self.deck[0])
                        self.deck.pop(0)
                    elif player == 2:
                        self.p3cards.append(self.deck[0])
                        self.deck.pop(0)
                    elif player == 3:
                        self.p4cards.append(self.deck[0])
                        self.deck.pop(0)
                    else:
                        self.p1cards.append(self.deck[0])
                        self.deck.pop(0)
                player -=1
            cards = self.getCards(player)
            for i in range(len(cards)):
                card2 = cards[i]
                if card2[1] == "f":
                    r = i
            cards.pop(r)
            
        else:
            self.curDeck.append(card)
            if self.reverse:
                if player == 0:
                    self.p1went = True
                    self.p2went = True
                    self.p3went = True
                elif player == 1:
                    self.p1went = False
                elif player == 2:
                    self.p2went = False
                else:
                    self.p3went = False
            else:
                if player == 0:
                    self.p1went = True
                elif player == 1:
                    self.p2went = True
                elif player == 2:
                    self.p3went = True
                else:
                    self.p4went = True
                    self.resetWent()
            cards = self.getCards(player)
            print(cards)
            print(card)
            for i in range(len(cards)):
                card2 = cards[i]
                try:
                    if card[0] == card2[0] and int(card[1]) == int(card2[1]):
                        print("!")
                        r = i
                except:
                    print("not a number card")
            cards.pop(r)

        if len(self.deck) < 4:
            for i in range(len(self.curDeck) - 1):
                self.deck.append(self.curDeck[0])
                self.curDeck.pop(0)
            random.shuffle(self.deck)
        self.advanced = True
                
    def connected(self):
        return self.ready

    def winner(self, game):
        w = -1
        if len(game.p1cards) == 0:
            w = 0
        elif len(game.p2cards) == 0:
            w = 1
        elif len(game.p3cards) == 0:
            w = 2
        elif len(game.p4cards) == 0:
            w = 3
        return w

    def getCards(self, player):
        if player == 0:
            return self.p1cards
        elif player == 1:
            return self.p2cards
        elif player == 2:
            return self.p3cards
        else:
            return self.p4cards

    def getDisplays(self):
        return self.display1,self.display2,self.display3,self.display4

    def unDisplay(self):
        self.display1 = False
        self.display2 = False
        self.display3 = False
        self.display4 = False

    def getTurn(self, player):
        if self.p1went == False and self.p2went == False and self.p3went == False and self.p4went == False:
            if self.advanced:
                self.Display()
                self.advanced = True
            else:
                self.unDisplay()
            if player == 0:
                return True
        elif self.p1went == True and self.p2went == False and self.p3went == False and self.p4went == False:
            if self.advanced:
                self.Display()
                self.advanced = True
            else:
                self.unDisplay()
            if player == 1:
                return True
        elif self.p1went == True and self.p2went == True and self.p3went == False and self.p4went == False:
            if self.advanced:
                self.Display()
                self.advanced = True
            else:
                self.unDisplay()
            if player == 2:
                return True
        elif self.p1went == True and self.p2went == True and self.p3went == True and self.p4went == False:
            if self.advanced:
                self.Display()
                self.advanced = True
            else:
                self.unDisplay()
            if player == 3:
                return True
        return False
            
    def resetWent(self):
        self.p1went = False
        self.p2went = False
        self.p3went = False
        self.p4went = False

    def reset(self):
        self.p1went = False
        self.p2went = False
        self.p3went = False
        self.p4went = False
        self.deck = self.createDeck()
        random.shuffle(self.deck)
        self.p1cards = []
        self.p2cards = []
        self.p3cards = []
        self.p4cards = []
        self.curDeck = []
        for i in range(7):
            self.p1cards.append(self.deck[0])
            self.deck.pop(0)
        for i in range(7):
            self.p2cards.append(self.deck[0])
            self.deck.pop(0)
        for i in range(7):
            self.p3cards.append(self.deck[0])
            self.deck.pop(0)
        for i in range(7):
            self.p4cards.append(self.deck[0])
            self.deck.pop(0)
        self.curDeck.append(self.deck[0])
        self.deck.pop(0)
        self.reverse = False
        self.pickup2 = False
        self.pickupTally = 0
        self.id = id
        self.ready = False

    def validChoice(self, card):
        topCard = self.curDeck[len(self.curDeck) - 1]
        print(topCard)
        print(card)
        if card[0] == 4:
            return True
        if card[1] == topCard[1]:
            return True
        if card[0] == topCard[0]:
            return True
        return False

    def createDeck(self):
        deck = []
        for x in range(4):
            deck.append([x,"0"])
            for y in range(2):
                for z in range(1,10):
                    deck.append([x,str(z)])
        for x in range(2):
            for y in range(4):
                deck.append([y,"s"])
        for x in range(2):
            for y in range(4):
                deck.append([y,"r"])
        for x in range(2):
            for y in range(4):
                deck.append([y,"d"])
        for i in range(4):
            deck.append([4,"w"])
            deck.append([4,"f"])
        return deck
