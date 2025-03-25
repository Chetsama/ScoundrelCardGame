suits = "♤♧♡♢"
ranks = "23456789TJQKA"
cards = []
import random

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

def scoundrel(deck):
    # diamonds sword
    # hearts potion
    # clubs & spades monsters
    
    
    hand = []
    for i in range(4):
        hand.append(deck.pop())
    print("Welcome you scoundrel, moves are ABCD to select a card or S to skip")
    decision = input("What's your move then cowboy?")
    print(deck)
    print(hand)



if __name__ == "__main__":
    cards = generate_deck()
    print(len(cards))
    print(cards)
    random.shuffle(cards)
    scoundrel(cards)
    
    #main()