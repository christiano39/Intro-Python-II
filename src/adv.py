from room import Room
from player import Player
from item import Item

# Declare all the rooms
item = {
	'key': Item("Key", "A strange key that seems like it could be useful")
}

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

room['foyer'].add_item(item['key'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Christian", room['outside'])

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

print(f'\nWelcome, {player.name}')

while True:
	print()
	print(player.current_room.name)
	print(player.current_room.description + '\n')
	# print(f"\ninv: {player.inventory}, room items: {player.current_room.items}")

	if len(player.current_room.items) > 0:
		print('You spot something in the area')
		for item in player.current_room.items:
			print(f"{item.name}: {item.description}")
		print()

	choice = input('What is your action? ')

	if len(choice.split(' ')) == 1:
		if choice == 'q':
			print('Exiting game...')
			break
		elif choice == 'i' or choice == 'inventory':
			if len(player.inventory) > 0:
				print('Your inventory:')
				for item in player.inventory:
					print(f"{item.name}: {item.description}")
			else:
				print("Your inventory is empty")
		elif choice == 'n':
			if player.current_room.n_to:
				player.current_room = player.current_room.n_to
			else:
				print()
				print("There is nothing for you that way, try a new direction...")
		elif choice == 's':
			if player.current_room.s_to:
				player.current_room = player.current_room.s_to
			else:
				print()
				print("There is nothing for you that way, try a new direction...")
		elif choice == 'e':
			if player.current_room.e_to:
				player.current_room = player.current_room.e_to
			else:
				print()
				print("There is nothing for you that way, try a new direction...")
		elif choice == 'w':
			if player.current_room.w_to:
				player.current_room = player.current_room.w_to
			else:
				print()
				print("There is nothing for you that way, try a new direction...")
	elif len(choice.split(' ')) == 2:
		command = choice.split(' ')
		if command[0] == 'take' or command[0] == 'get':
			room_has_item = [item for item in player.current_room.items if command[1].lower() == item.name.lower()]
			if len(room_has_item) > 0:
				player.current_room.remove_item(room_has_item[0].name)
				player.add_to_inventory(room_has_item[0])
			else:
				print(f"\nThere is no {command[1]} in this room")
		elif command[0] == 'drop':
			player_has_item = [item for item in player.inventory if command[1].lower() == item.name.lower()]
			if len(player_has_item) > 0:
				player.remove_from_inventory(player_has_item[0].name)
				player.current_room.add_item(player_has_item[0])
			else:
				print(f"\nThere is no {command[1]} in your inventory")
	else:
		print('Unable to do that')
	print("\n---------------------------------------------------------------------------")