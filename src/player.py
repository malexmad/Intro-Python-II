# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    """
    Player class
    """

    def __init__(self, name, starting_room, items=None):
        self.name = name
        self.current_room = starting_room

        if items is None:
            self.items = []
        else:
            self.items = items

    def travel(self, direction):
        """ method for moving the player to a new room """

        next_room = getattr(self.current_room, f"{direction}_to")

        if next_room != None:
            self.current_room = next_room
            print("\n--------------New Room--------------")
            print(self.current_room.name)
            print(self.current_room.description)
            if self.current_room.items != []:
                print("Items in room:", self.current_room.items.name, "\n  ", self.current_room.items.description)
            else:
                print("Room is empty!")
            print("-------------------------------------")

        else:
            print("\nYou can't move that direction\n")


    def actions(self, actions=None):
        """ method for picking and dropping items"""

        # picking up item
        if actions.split()[0] == 'take' and actions.split()[1] == self.current_room.items.name.lower():
            add_item = self.current_room.items.name

            if add_item != None:
                self.items.append(add_item)
                self.current_room.items.on_take()
                self.current_room.items = []

        # dropping item
        elif actions.split()[0] == 'drop' and actions.split()[1].title() in self.items:
            drop_item = actions.split()[1].title()

            if drop_item != None:
                self.items.remove(drop_item)
                self.current_room.items.on_drop()

        # error
        else:
            print("\nNo item available\n")

    def inventory(self):
        """ method for player to check their inventory """

        print("\n****************************")
        print("Inventory:", self.items)
        print("****************************")
