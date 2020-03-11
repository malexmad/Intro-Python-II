from world import game_intro, room


""" 
Game Start
"""

player = game_intro()

# game loops until player quits
while True:

    action = input("\nEnter your action(s, n, w, e, q, i, take {itemname}, drop {itemname}):").lower()

    try:
        if action == 'q':
            break

        elif action == 'i':
            player.inventory()

        elif action.split()[0] == 'take' or action.split()[0] == 'drop':

                player.actions(action)

        else:
            player.travel(action)

    except:
        print("\n--------------------------------\nError: Wrong Key\n--------------------------------\n")

