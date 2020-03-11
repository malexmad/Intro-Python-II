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
        next_room = getattr(self.current_room, f"{direction}_to")

        if next_room != None:
            self.current_room = next_room
            print("\n-----------New Room-----------")
            print(self.current_room.name)
            print(self.current_room.description)
            if self.current_room.items != []:
                print("Items in room:", self.current_room.items.name, "\n  ", self.current_room.items.description)
            print("------------------------------")
            print("Inventory: ", self.items)
            print("------------------------------")
        else:
            print("\nYou can't move that direction\n")


    def actions(self, actions=None):

        if actions.split()[0] == 'take' and actions.split()[1] == self.current_room.items.name.lower():
            add_item = self.current_room.items.name

            if add_item != None:
                self.items.append(add_item)
                self.current_room.items = []
                print("\n---------new item---------")
                print('You have picked up a',self.items[-1])
                print("--------------------------")

        elif actions.split()[0] == 'drop':
            drop_item = actions.split()[1]

            if drop_item != None:
                self.items.remove(drop_item)
                print("\n---------inventory---------")
                print(self.items)
                print("--------------------------")

        else:
            print("\nNo item available\n")


    # def __str__(self):
    #     return (f'{self.name},\n {self.description}')