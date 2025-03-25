from enum import Enum
class face_card(Enum):
    def __str__(self):
        return str(self.value)
    T=10
    J=11
    Q=12
    K=13
    A=14

class suit(Enum):
    def __str__(self):
        return str(self.value)
    0 = '♤'
    1 = '♧'
    2 = '♡'
    3 = '♢'

class action(Enum):
    def __str__(self):
        return str(self.value)
    attack = 'attack'
    defend = 'defend'
    heal = 'heal'

class card():
    def __init__(self, suit, rank, action):
        self.suit = suit
        self.rank = rank
        self.name = suit + rank
        self.action = action
    
    if suit in '♡':
        color = 'red'
        property = 'heal'
    elif suit in '♢':
        color = 'red'
        property = 'attack'
    else:
        color = 'black'
        property = 'monster'



def main():
    equiped = ['♢A']
    print(equiped[0][1])
    if equiped[0][1] in 'TJQKA':
        val= str(equiped[0][1])
        print(face_card[equiped[0][1]])

    

if __name__ == "__main__":
    main()
    for i in range(4):
        for j in range(13):

            card(suit[i], rank[j], action[0])
            card[D4].color()
            card[D4].property()
            
