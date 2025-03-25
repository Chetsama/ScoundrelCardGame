suits = "♤♧♡♢"
ranks = "23456789TJQKA"
import random
player_health=20
from enum import Enum
equiped = []
heal_last_turn = False

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
    cards = []

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

def new_hand(deck, hand, skip_last):
    if skip_last == True:
        
        random.shuffle(hand)
        hand.extend(deck)
        deck = hand
        hand = []

        for i in range(4):
            hand.append(deck.pop())
        scoundrel(hand, deck, skip_last)

    if len(deck)>3:
        for i in range(3):
            hand.append(deck.pop())
        scoundrel(hand, deck, skip_last)
    elif len(deck)==0:
        print("You've done it you scoundrel")
        exit()
    else:
        for i in range(len(deck)):
            hand.append(deck.pop())
        scoundrel(hand, deck, skip_last)

def calculate_damage(sword, monster):
    if sword>=monster:
        damage = 0
    else:
        damage = monster-sword
    return damage

def turn(move):
    global player_health
    global equiped
    global heal_last_turn
    biggest_monster = 15
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
            if len(equiped)>1:
                if equiped[len(equiped)-1][1] in 'TJQKA':
                    biggest_monster = int(str(face_card[equiped[len(equiped)-1][1]]))
                else:
                    biggest_monster = int(equiped[len(equiped)-1][1])
            if equiped == []:
                player_health=player_health-number
                return True
            else:
                answer = some_user_input("Do you want to use your equiped card? y/n\n")
                if answer == 'y':
                    if equiped[0][1] in 'TJQKA':
                        weapon_strength = int(str(face_card[equiped[0][1]]))
                    else:
                        weapon_strength = int(equiped[0][1])
                    if number>biggest_monster:
                        print(f"{bcolors.WARNING}This is an invalid move{bcolors.ENDC}")
                        return False
                    else:
                        player_health=player_health-calculate_damage(weapon_strength, number)
                        equiped.append(move)
                        return True
                else:
                    player_health=player_health-number
                    return True
        case '♡':
            if heal_last_turn == True:
                print(f"{bcolors.FAIL}You can't heal two turns in a row{bcolors.ENDC}")
                return False
            else:
                player_health=player_health+number
                heal_last_turn = True
                return True
        case '♢':
            answer = some_user_input("Do you want to equip this card? y/n ")
            if answer == 'y':
                print(f'{bcolors.OKGREEN}equiped{bcolors.ENDC}\n')
                equiped = [move]
            return True

def scoundrel(hand, deck, skip_last):
    global player_health
    global heal_last_turn
    if player_health<=0:
        print(f"{bcolors.FAIL}DEAD{bcolors.ENDC}\n\n")
        again = some_user_input("Would you like to play again?\n\n")
        if again == 'y':
            player_health=20
            new_game()
        else:
            exit()
    if player_health>20:
        player_health=20
        
    #USERINPUT
    print("Hand  - " + str(hand))
    print("Equip - " + str(equiped))
    print("Your health is: " + str(player_health))
    print("{} cards remaining".format(str(len(deck))))
    decision = input("What's your move then cowboy?")

    if decision in 'abcds' and len(decision)==1:
        print("")
    else:
        print(f"{bcolors.FAIL}That's not gonna work{bcolors.ENDC}")
        scoundrel(hand, deck, skip_last)

            
    #USERINPUT
    match decision:
        case 'a':
            valid_move = turn(hand[0])
            if(valid_move):
                skip_last = False
                hand[0] = '//'
        case 'b':
            valid_move = turn(hand[1])
            if(valid_move):
                skip_last = False
                hand[1] = '//'
        case 'c':
            valid_move = turn(hand[2])
            if(valid_move):
                skip_last = False
                hand[2] = '//'
        case 'd':
            valid_move = turn(hand[3])
            if(valid_move):
                skip_last = False
                hand[3] = '//'
        case 's':
            count = [x for x in hand if x == '//']
            if skip_last == True:
                print(f"{bcolors.FAIL}You can't skip two turns in a row{bcolors.ENDC}")
            elif len(count)==0:
                skip_last = True
                new_hand(deck, hand, skip_last)
                
            else:
                print(f"{bcolors.FAIL}You can only skip with a full hand, soz :({bcolors.ENDC}")

            #shuffle hand
            #ensure moves_taken=0
            #put the cards back in at the bottom of the deck
    
    #TODO check if all cards are used
    
    remaining_card = [x for x in hand if x != '//']
    if len(remaining_card)==0 and len(deck)==0:
        print("You've done it you scoundrel")
        exit()
    elif len(remaining_card)==1 and len(deck)>0:
        print(f'{bcolors.OKCYAN}remaining_card: {bcolors.ENDC}' + str(remaining_card))
        heal_last_turn = False
        new_hand(deck, remaining_card, skip_last)
    
    decision = ""

    scoundrel(hand,deck, skip_last)


def new_game():
    deck = generate_deck()
    random.shuffle(deck)
    hand = []
    skip_last = False
    for i in range(4):
        hand.append(deck.pop())
    
    print("Welcome you scoundrel, moves are ABCD to select a card or S to skip")
    print("Your current Health is " + str(player_health))
    print("There are " + str(len(deck)) + " cards remaining")
    print("")

    scoundrel(hand, deck, skip_last)


if __name__ == "__main__":
    # diamonds sword
    # hearts potion
    # clubs & spades monsters
    new_game()