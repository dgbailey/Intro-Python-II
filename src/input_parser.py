#consume user input
        #consume user
        #2 words or one
        #if one follow programmed protocol
        #if two which one
        #conduct appropriate actions with room, player and item

        #if return == q break
        #elif return ==

class Parser:
   
    def __init__(self):
    
        self.valid_commands ={'get':'get','drop':'drop'}

        self.valid_directions = {'n':'n',
                            's':'s',
                            'e':'e',
                            'w':'w',
                            'q':'q'}

       

    def parse_player_input(self,player_input,player):     

        split_input = player_input.split()

        if player_input == 'q':

            return False, "*** QUIT GAME ***"

        elif player_input in self.valid_directions.values():

            #if valid check if room has a next direction
            if player.room.next_direction(player_input + '_to') == None:
        
                return True, '*** CANNOT GO THAT WAY. TRY AGAIN. ***'

            else:
                player.room = player.room.next_direction(player_input + '_to')

                return True, None


        #first value of split is important for identifying commands
        elif split_input[0] in self.valid_commands.values():
            command = split_input[0]
            item_name = split_input[1]
            
            if command == 'get':
                player.get_item(player.room.remove_item(item_name))

                return True, player.enumerate_inventory()

            elif command == 'drop':
                player.room.add_item(player.drop_item(item_name))

                return True, player.enumerate_inventory()


        else:
            return True,f"*** INCORRECT INPUT  {player_input}"

        
            