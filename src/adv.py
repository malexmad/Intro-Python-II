from world import game_intro, room


""" 
Game Start
"""

# game introduction and input for player's name
player = game_intro()

# game loops until player quits
while True:

    # player input
    action = input("\nEnter your action(s, n, w, e, q, i, take {itemname}, drop {itemname}):").lower()

    try:
        # to quit game
        if action == 'q':
            break

        # to check inventory
        elif action == 'i':
            player.inventory()

        # to take or drop items
        elif action.split()[0] == 'take' or action.split()[0] == 'drop':

                player.actions(action)

        # to move player
        else:
            player.travel(action)
            player.room_info()

    except:
        print("\n--------------------------------\nError: Wrong Key\n--------------------------------\n")

