suits = "♤♧♡♢"
ranks = "23456789TJQKA"
cards = []
import random
player_health=20
from enum import Enum

class choice(Enum):
    A=1
    B=2
    C=3
    D=4
    S=5

def generate_deck():
    print("♤♧♡♢")
    print("A23456789TJQK")

    for i in range(4):
        if i<2:
            for j in range(13):
                cards.append(suits[i]+ranks[j])
        else:
            for j in range(9):
                cards.append(suits[i]+ranks[j])

    return cards

def turn(move):
    global player_health
    print("move: " + move)
    number=0
    if move == "//":
        return
    
    if(move[1] in 'TJQKA'):
        match move[1]:
            case 'T':
                number = 10
                print(move)
            case 'J':
                number = 11
            case 'Q':
                number = 12
            case 'K':
                number = 13
            case 'A':
                number = 14
    else:
        number = int(move[1])
            

    match move[0]:
        case '♤':
            player_health=player_health-number
            print(player_health)
        case '♧':
            player_health=player_health-number
            print(player_health)
        case '♡':
            player_health=player_health+number
            print(player_health)
        case '♢':
            print('equip')


def scoundrel(deck):
    # diamonds sword
    # hearts potion
    # clubs & spades monsters
    
    hand = []
    for i in range(4):
        hand.append(deck.pop())
    print("Welcome you scoundrel, moves are ABCD to select a card or S to skip")
    print(player_health)
    print(hand)
    
    #USERINPUT
    wait=True
    while(wait==True):
        decision = input("What's your move then cowboy?")
        try:
            if decision in 'ABCDS' and len(decision)==1:
                print(player_health)
            else:
                print("That's not gonna work")
                decision = input("What's your move then cowboy?")
        except:
            print("That's not gonna work")
            decision = input("What's your move then cowboy?")
    #USERINPUT
        
        #print(choice[decision].value)
        #print(choice)
        match decision:
            case 'A':
                turn(hand[0])
                hand[0] = '//'
            case 'B':
                turn(hand[1])
                hand[1] = '//'
            case 'C':
                turn(hand[2])
                hand[2] = '//'
            case 'D':
                turn(hand[3])
                hand[3] = '//'
            case 'S':
                #TODO
                print('wip')
        
        print(hand)
        decision = ""




if __name__ == "__main__":
    cards = generate_deck()
    print(len(cards))
    
    #print(cards)
    random.shuffle(cards)
    scoundrel(cards)
    
    
    #main()