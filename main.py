# UNO
import random
class Card():
    def __init__(self,color:str,type:str,value:int):
        self.color = color
        self.type = type
        self.value = value

players = []
hand = []
deck = []

type = ["number", "+2","+4 wild","skip","reverse","wild"]
# 0, 1-9x2, 8 skip reverse +2, 4 wild +4wild
colors = ["Blue","Green","Red","Yellow"]

for t in type:
    if t == "number":
        for color in colors:
            deck.append(Card(color,"0",0))
        for j in range(2):
            for color in colors:
                for i in range(1,10):
                 deck.append(Card(color,int(i),i))
    if t == "+2" or t == "skip" or t == "reverse":
        for color in colors:
            for i in range(2):
                deck.append(Card(color,t,20))
    if t == "+4 wild" or t== "wild":
        for i in range(4):
            deck.append(Card("",t,50))


def print_deck(deck: Card):
    for item in deck:
        print(item.color, item.type, end =",")
    print()

print_deck(deck)
print(len(deck))

def create_Players():

    num = int(input("How many players are playing?"))

    random.shuffle(deck)
    print(deck)

    for x in range(num):
        hand =[]
