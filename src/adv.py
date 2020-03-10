from player import Player
from world import room

""" 
Game Start
"""
# Intro
print("Welcome, try to reach the treasure room\nYou will start outside of the cave!\n"
      "You will have 4 options to move from room to room(North(n), South(s), West(w), East(e))\n"
      "To quit enter 'q'\n ")

# Player enter their name, default starting room is outside
player = Player(input('Enter your name:'), room['outside'])
print("Player: ", player.name)
print("\n---------Current Room---------")
print(player.current_room.name)
print(player.current_room.description)
print("------------------------------")

# game loops until player quits
while True:

    move = input("\nEnter your move(s, n, w, e, q):").lower()

    try:
        if move == 'q':
            break
        else:
            player.travel(move)

    except:
        print("\n--------------------------------\nError: Wrong Key\n--------------------------------\n")
