from room import Room
from player import Player


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
    while True:
        valid_directions = ['n','s','e','w','q']
        print('\n' '\n' +"Your Current Room is: " + player.room.name + '\n' '\n' +  "Room Description: " + player.room.description + '\n' '\n')
        
        player_input = input("Choose a direction: n,s,e,w or 'q' for quit --->")

        try:
            if player_input in valid_directions and player_input != 'q':
                
                #using getattr instead of multiple if conditions. This allows us to call an attribute dynamically with a string value
                if getattr(player.room, player_input + '_to') is None:
                   print('\n' '\n' + "**** DEAD END TRY AGAIN ****")
                else:
                    player.room = getattr(player.room, player_input + '_to')
                
                    
                

            else:
                print('\n' '\n' +" ** QUIT GAME**")
                break
        
        except:
            print("** Unexpected Error **")


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
