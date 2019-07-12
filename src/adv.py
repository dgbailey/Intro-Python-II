from room import Room
from player import Player
from item import Item
from input_parser import Parser

# declare items

item1 = Item("cleaver","A powerful tool for cutting meat")
# Declare all the rooms

#room class will now be imported with correct args & methods for initialization of instances
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

#link items to room

room['outside'].add_item(item1)
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def main(player):

    response_parser = Parser()

    while True:
       
        print('\n' '\n' +"Your Current Room is: " + player.room.name + '\n' '\n' +  
                "Room Description: " + player.room.description + '\n' '\n' + 
                "Room Items: " + player.room.enumerate_items() + '\n'
                    + 
                f"Inventory Items: " + player.enumerate_inventory() + '\n')

                    
        player_input = input("Choose a direction: n,s,e,w or 'q' for quit --->")

        #parser returns boolean False with error message
        #OR parser returns boolean true with success message
        boolean, parser_response = response_parser.parse_player_input(player_input,player)

        if boolean is False:
            print(parser_response)
            break
        
        else:
            print(parser_response)
            


       
        
    
        


main(Player("Dustin",room['outside']))


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
