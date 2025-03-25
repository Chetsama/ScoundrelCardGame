suits = "♤♧♡♢"
ranks = "23456789TJQKA"
cards = []
import random
player_health=20
from enum import Enum
equiped = []

class choice(Enum):
    a=1
    b=2
    c=3
    d=4
    s=5

class face_card(Enum):
    def __str__(self):
        return str(self.value)
    T=10
    J=11
    Q=12
    K=13
    A=14

def generate_deck():
    print("♤♧♡♢\n")
    #print("23456789TJQKA")

    for i in range(4):
        if i<2:
            for j in range(13):
                cards.append(suits[i]+ranks[j])
        else:
            for j in range(9):
                cards.append(suits[i]+ranks[j])

    #print(cards)
    return cards

def some_user_input(text):
    break_while = False
    while (break_while == False):
        ask = input(text)
        try:
            if ask in 'yn' and len(ask)==1:
                print("")
                break_while = True
                return ask
            else:
                print("That's not gonna work")
                ask = input(text)
        except:
            print("That's not gonna work")
            exit()


def turn(move):
    global player_health
    global equiped
    #print("move: " + move)
    number=0
    if move == "//":
        return
    
    #sets a number for face cards
    if(move[1] in 'TJQKA'):
        number = int(str(face_card[move[1]]))
    else:
        number = int(move[1])
    
    #print('{} = {}'.format(equiped[0][1], number))

    
    match move[0]:
        case monster if monster in '♤♧':
            if equiped == []:
                player_health=player_health-number
            else:
                answer = some_user_input("Do you want to use your equiped card? y/n\n")
                if answer == 'y':
                    if equiped[0][1] in 'TJQKA':
                        weapon_strength = int(str(face_card[equiped[0][1]]))
                    else:
                        weapon_strength = int(equiped[0][1])

                    player_health=player_health-number+int(weapon_strength)
                    equiped.append(move)
                else:
                    player_health=player_health-number
        case '♡':
            player_health=player_health+number
        case '♢':
            answer = some_user_input("Do you want to equip this card? y/n ")
            if answer == 'y':
                print('equiped')
                equiped = [move]
                

def new_hand(deck, hand):
    
    if len(deck)>3:
        for i in range(3):
            hand.append(deck.pop())
        print(str(len(deck)) + " cards remaining")
        scoundrel(hand, deck)
    elif len(deck)==0:
        print("You've done it you scoundrel")
        exit()
    else:
        for i in range(len(deck)):
            hand.append(deck.pop())
        print(str(len(deck)) + " cards remaining")
        scoundrel(hand, deck)

def scoundrel(hand, deck):    
    #USERINPUT
    print("Hand - " + str(hand))
    print("Equip- " + str(equiped))
    print("Your health is: " + str(player_health))

    moves_taken=0
    while(moves_taken<3):
        decision = input("What's your move then cowboy?\n\n")
        try:
            if decision in 'abcds' and len(decision)==1:
                print("")
            else:
                print("That's not gonna work")
                decision = input("What's your move then cowboy?\n")
        except:
            print("That's not gonna work")
            decision = input("What's your move then cowboy?\n")

    #USERINPUT
        match decision:
            case 'a':
                turn(hand[0])
                hand[0] = '//'
                moves_taken+=1
            case 'b':
                turn(hand[1])
                hand[1] = '//'
                moves_taken+=1
            case 'c':
                turn(hand[2])
                hand[2] = '//'
                moves_taken+=1
            case 'd':
                turn(hand[3])
                hand[3] = '//'
                moves_taken+=1
            case 's':
                #TODO
                print('wip')
                #shuffle hand
                #ensure moves_taken=0
                #put the cards back in at the bottom of the deck
        
        #TODO check if all cards are used
        if moves_taken==3:
            remaining_card = [x for x in hand if x != '//']
            print('remaining_card: ' + str(remaining_card))
            new_hand(deck, remaining_card)
        else:
            print("Hand - " + str(hand))
            print("Equip- " + str(equiped))
            print("Your health is: " + str(player_health))
        
        decision = ""




if __name__ == "__main__":
    deck = generate_deck()
    
    
    #print(cards)
    random.shuffle(deck)

    # diamonds sword
    # hearts potion
    # clubs & spades monsters

    hand = []
    for i in range(4):
        hand.append(deck.pop())
    
    print("Welcome you scoundrel, moves are ABCD to select a card or S to skip")
    print("Your current Health is " + str(player_health))
    print("There are " + str(len(deck)) + " cards remaining")
    print("")

    scoundrel(hand, deck)
    
    
    #main()