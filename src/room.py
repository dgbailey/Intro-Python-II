# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
   def __init__(self,name,description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.room_items = []

   
   def next_direction(self,direction):
      return getattr(self,direction)

   def enumerate_items(self):
      return ''.join([item.name for item in self.room_items])


   def add_item(self,item):
      
      self.room_items.append(item)
      print(f'{item.name} added to {self.name}.  Current items:{[item.name for item in self.room_items]}')

   def remove_item(self,item_name):
      item = next(obj for obj in self.room_items if obj.name== item_name)
      #return the removed item to be used in input parser
      return self.room_items.pop(self.room_items.index(item))