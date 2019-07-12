# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self,name,room):
        self.name = name
        self.room = room
        self.inventory = []
        self.input = ''


    
    def get_item(self,item):
        self.inventory.append(item)

    def drop_item(self,item_name):
        item = next(obj for obj in self.inventory if obj.name == item_name)
      
        return self.inventory.pop(self.inventory.index(item))
        

    def enumerate_inventory(self):
        return  ''.join([item.name for item in self.inventory])

    

