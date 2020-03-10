from world import game_intro, room, item

""" 
Game Start
"""

player = game_intro()

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
