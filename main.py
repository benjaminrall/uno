from network import Network
import random, socket, display, time
'''
KEY ==
Types:
    0 = red
    1 = yellow
    2 = blue
    3 = green
    4 = wild

Class:
    0-9 = numbers
    s = skip
    r = reverse
    d = draw 2
    w = wild
    f = draw 4
     
    CARD = [COLOUR, NUMBER/TYPE]
'''

def Display(player, turn):
    if turn < 0:
        display.reset()
        display.draw(-200,250,2,game.curDeck[len(game.curDeck) - 1])
        display.draw(200,250,2,[0,"uno"])
        pCards = []
        for i in range(4):
            cards = game.getCards(i)
            print("Player " + str(i + 1) + ": " + str(len(cards)) + " cards")
            if len(cards) == 1:
                pCards.append([str(i+1),"UNO"])
            else:
                pCards.append([str(i+1),str(len(cards))])
            
        display.write(-390,370,15,"You are player "+str(player+1))
        if turn > -1:
            display.write(0,250,17,"It is Player "+str(turn)+"'s turn...")
        else:
            display.write(0,250,17,"It is your turn.")
        display.write(0,-380,20,"Player "+pCards[0][0]+": "+pCards[0][1]+"           Player "+pCards[1][0]+": "+pCards[1][1]+"            Player "+pCards[2][0]+": "+pCards[2][1]+"            Player "+pCards[3][0]+": "+pCards[3][1])

        cards = []
        temp = game.getCards(player)
        for i in range(len(temp)):
            cards.append(temp[i])
        lines = 0
        for i in range(4):
            if (i*12) <= len(cards):
                lines = i
        if lines >= 0:
            for i in range(1,13):
                if len(cards) > 0:
                    card = cards[0]
                    display.draw(-450 + (70*i),0,1.5,card)
                    cards.pop(0)
                else:
                    break
        if lines >= 1:
            for i in range(1,13):
                if len(cards) > 0:
                    card = cards[0]
                    display.draw(-450 + (70*i),-120,1.5,card)
                    cards.pop(0)
                else:
                    break
        if lines >= 2:
            for i in range(1,13):
                if len(cards) > 0:
                    card = cards[0]
                    display.draw(-450 + (70*i),-240,1.5,card)
                    cards.pop(0)
                else:
                    break
        if lines >= 3:
            print("Too many cards")
    else:                    
        display.reset()
        display.draw(-200,250,2,game.curDeck[len(game.curDeck) - 1])
        display.draw(200,250,2,[0,"uno"])
        pCards = []
        for i in range(4):
            cards = game.getCards(i)
            print("Player " + str(i + 1) + ": " + str(len(cards)) + " cards")
            if len(cards) == 1:
                pCards.append([str(i+1),"UNO"])
            else:
                pCards.append([str(i+1),str(len(cards))])
            
        display.write(-390,370,15,"You are player "+str(player+1))
        if turn > -1:
            display.write(0,250,17,"It is Player "+str(turn)+"'s turn...")
        else:
            display.write(0,250,17,"It is your turn.")
        display.write(0,-380,20,"Player "+pCards[0][0]+": "+pCards[0][1]+"           Player "+pCards[1][0]+": "+pCards[1][1]+"            Player "+pCards[2][0]+": "+pCards[2][1]+"            Player "+pCards[3][0]+": "+pCards[3][1])
        cards = []
        temp = game.getCards(player)
        for i in range(len(temp)):
            cards.append(temp[i])
        lines = 0
        for i in range(4):
            if (i*12) <= len(cards):
                lines = i
        if lines >= 0:
            for i in range(1,13):
                if len(cards) > 0:
                    card = cards[0]
                    display.draw(-450 + (70*i),0,1.5,card)
                    cards.pop(0)
                else:
                    break
        if lines >= 1:
            for i in range(1,13):
                if len(cards) > 0:
                    card = cards[0]
                    display.draw(-450 + (70*i),-120,1.5,card)
                    cards.pop(0)
                else:
                    break
        if lines >= 2:
            for i in range(1,13):
                if len(cards) > 0:
                    card = cards[0]
                    display.draw(-450 + (70*i),-240,1.5,card)
                    cards.pop(0)
                else:
                    break
        if lines >= 3:
            print("Too many cards")

def printGame(game, player):
    global first
    if not (game.connected()):
        print("Waiting for players...")
        display.write(0,0,40,"Waiting for players...")
    else:
        if first:
            Display(p,1)
            first = False
        try:
            print(game.curDeck[len(game.curDeck) - 1])
        except:
            print("(Error2)")
        for i in range(4):
            if game.getTurn(i):
                if i == player:
                    print("It is your turn.")
                    turn = -500
                else:
                    print("It is player " + str(i + 1) + "'s turn.")
                    turn = i + 1
        for i in range(4):
            cards = game.getCards(i)
            global over, winner
            print("Player " + str(i + 1) + ": " + str(len(cards)) + " cards")
            if len(cards) == 0 and over == False:
                print("Player " + str(i + 1) + " wins!")
                winner = i + 1
                over = True
                display.reset()
                display.write(0,0,40,"Player " + str(winner) + " wins!")
                time.sleep(1000)
            elif over:
                print("Player",winner,"wins!")
        cards = game.getCards(player)
        print(cards)
        display1, display2, display3, display4 = game.getDisplays()
        if player == 0:
            if display1:
                Display(player,turn)
        elif player == 1:
            if display2:
                Display(player,turn)
        elif player == 2:
            if display3:
                Display(player,turn)
        elif player == 3:
            if display4:
                Display(player,turn)
        game.unDisplay()
        
run, over, winner = True, False, -1
n = Network()
p = int(n.getP())
first = True
print("You are player",p+1)
while run:
    try:
        game = n.send("get")
        game.display1 = False
        game.display2 = False
        game.display3 = False
        game.display4 = False
        if game == None:
            print("(Error4)")
    except socket.error as e:
        print(str(e))
        run = False
        print("(Error1)")
        break

    try:
        if game.getTurn(p) and game.connected() and over == False:
            cards = game.getCards(p)
            printGame(game, p)
            choice = ""
            if over == False:
                choice = input("Enter the number of the card you would like to play: ")
            if choice == "d" or choice == "D":
                game = n.send(choice.lower())
            else:
                try:
                    choice = int(choice)
                    card = cards[choice - 1]
                    if choice > 0 and choice <= len(cards) and game.validChoice(card) and over == False:
                        if game.pickup2:
                            if card[1] == "d":
                                game = n.send(card)
                            else:
                                print("Not a valid choice")
                        elif card[1] == "f" or card[1] == "w":
                            choice2 = input("Enter the colour you would like to change to (r/y/b/g): ")
                            if choice2.lower() == "r":
                                card[0] = 0
                                game = n.send(card)
                                print("Sent")
                            elif choice2.lower() == "y":
                                card[0] = 1
                                game = n.send(card)
                                print("Sent")
                            elif choice2.lower() == "b":
                                card[0] = 2
                                game = n.send(card)
                                print("Sent")
                            elif choice2.lower() == "g":
                                card[0] = 3
                                game = n.send(card)
                                print("Sent")
                            else:
                                print("Not a valid choice")
                        else:
                            game = n.send(card)
                    elif over == False:
                        print("Not a valid choice")
                except:
                    print("(Error3)")
                    print("Not a valid choice")
                game.advanced = True
        else:
            printGame(game, p)
            time.sleep(5)
    except socket.error as e:
        print(e)

