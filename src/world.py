from room import Room
from player import Player
from item import Item


def game_intro():
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
    print("Items in room:", player.current_room.items.name, "\n  ", player.current_room.items.description)
    print("------------------------------")
    print("Inventory: ", player.items)
    print("------------------------------")

    return player


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                Item("Rock",
                     "A small useless rock?")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""",
                Item("Knife",
                     "A handmade knife with blood stain on it!")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, fallinginto the darkness. Ahead to the north, 
                                        a light flickers in the distance, but there is no way across the chasm.""",
                Item("Sword",
                     "A long shiny sword!!")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from westto north. The smell of gold permeates 
                                        the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been 
                                            completely emptied by earlier adventurers. The only exit is to the south.""",
                Item("Gold",
                     "One gold coin :/")),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

