# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.inventory = []

  def add_to_inventory(self, item):
    self.inventory.append(item)
    print(f"\nYou pick up the {item.name}")

  def remove_from_inventory(self, name):
    self.inventory = [item for item in self.inventory if item.name != name]
    print(f"\nYou drop the {name}")