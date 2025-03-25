from enum import Enum
class face_card(Enum):
    def __str__(self):
        return str(self.value)
    T=10
    J=11
    Q=12
    K=13
    A=14

def main():
    equiped = ['♢T']
    print(equiped[0][1])
    if equiped[0][1] in 'TJQKA':
        val= str(equiped[0][1])
        print(face_card[equiped[0][1]])

    

if __name__ == "__main__":
    main()