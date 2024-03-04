# UNO
import random


class Card():
    def __init__(self, color: str, type: str, value: int):
        self.color = color
        self.type = type
        self.value = value


players = []
deck = []
discard = []

type = ["number", "+2", "+4 Wild", "Skip", "Reverse", "Wild"]
# 0, 1-9x2, 8 skip reverse +2, 4 wild +4wild
colors = ["Blue", "Green", "Red", "Yellow"]

for t in type:
    if t == "number":
        for color in colors:
            deck.append(Card(color, "0", 0))
        for j in range(2):
            for color in colors:
                for i in range(1, 10):
                    deck.append(Card(color, i, i))
    if t == "+2" or t == "Skip" or t == "Reverse":
        for color in colors:
            for i in range(2):
                deck.append(Card(color, t, 20))
    if t == "+4 Wild" or "Wild" == t:
        for i in range(4):
            deck.append(Card("All", t, 50))


def print_deck(dek: list):
    for item in dek:
        print(item.color, item.type, end=",")
    print()


def allow(d: Card,d2: Card):
    if d.color == d2.color or d.type == d2.type or d2.type == "Wild" or d2.type == "+4 Wild":
        return True
    return False


def possible(d: Card, hand: list):
    for card in hand:
        if d.color == card.color or d.type == card.type or card.type == "Wild" or card.type =="+4 Wild":
            return True
    return False




num_of_players = int(input("How many players are playing?"))

random.shuffle(deck)

for x in range(num_of_players):
    handy = []
    for y in range(4):
        handy.append(deck.pop())
    players.append(handy)


turn_number = 0

discard.append(deck.pop())

#do you check if the player can play a card for them, if not, then draw a card and check if that can be played, and
# if it can then just play it and move on

while True:
    player_turn = turn_number % num_of_players
    print(discard[-1].color,discard[-1].type)
    print("It's "+str(player_turn)+" turn, hand: ", end =" ")
    print_deck(players[player_turn])

    if not possible(discard[-1],players[player_turn] ):
        x = deck.pop()
        if discard[-1].color == x.color or discard[-1].type == x.type:
            discard.append(x)

        else:
            players[player_turn].append(x)
            print_deck(players[player_turn])

        turn_number = turn_number + 1
        continue

    choice = int(input("Please player "+str(turn_number%num_of_players)+" pick a card to play on the discard pile:"))
    if not allow(discard[-1], players[player_turn][choice]):
        continue

    if discard[-1].value == -1:
        discard.pop(-1)
    discard.append(players[player_turn].pop(choice))
    if discard[-1].type == "+2":
        players[(turn_number+1)%num_of_players].append(deck.pop())
        players[(turn_number+1)%num_of_players].append(deck.pop())
    if discard[-1].type == "Reverse":
        print(players)
        players.reverse()
        print(players)
    if discard[-1].type == "+4 Wild":
        players[(turn_number+1)%num_of_players].append(deck.pop())
        players[(turn_number+1)%num_of_players].append(deck.pop())
        players[(turn_number+1)%num_of_players].append(deck.pop())
        players[(turn_number+1)%num_of_players].append(deck.pop())
        new_color = input("What new color would you like to make the discard pile?")
        discard[-1].color = new_color
    if discard[-1].type == "Wild":
        new_color = input("What new color would you like to make the discard pile?")
        discard[-1].color = new_color
    if discard[-1].type == "Skip":
        turn_number = turn_number+1
    if len(players[player_turn]) == 0:
        print("Congrats player "+str(player_turn)+" you win!")
        break
    print(discard[-1].color, discard[-1].type)

    print_deck(players[player_turn])
    turn_number = turn_number + 1
    print()




