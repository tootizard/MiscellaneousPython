#!/bin/python3

from time import time
from random import random, seed, randint, choice
from os import system, name

VEHICLE_TYPE = ('car', 'van', 'limosine', 'truck', 'monster truck', 'semi truck', 'tow truck', 'suv', 'sedan', 'hatchback', 'smart car', 'helicopter') 
VEHICLE_COLOR = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'beige', 'black', 'white', 'grey', 'silver', 'bronze', 'gold')
TICK = 2 # In seconds.
MAX_INVENTORY = 8
EMPTY_SLOT = ''

#---------------------------------------------

class vehicle:
	def __init__(self,vtype,color):
		self.type=vtype
		self.color=color

	def __repr__(self):
		return '{} {}'.format(self.color, self.type)

#--------------------------------------------

def inventory_full(inventory):
    if inventory.count(EMPTY_SLOT) == 0:
        return True
    return False

def inventory_empty(inventory):
    if inventory.count(EMPTY_SLOT) == MAX_INVENTORY:
        return True
    return False

def get_free_spot(inventory):
    return inventory.index(EMPTY_SLOT)

def buy_vehicle(inventory):
    if inventory_full(inventory):
        return
    vehicle_type = choice(VEHICLE_TYPE)
    vehicle_color = choice(VEHICLE_COLOR)

    new_vehicle = vehicle(vehicle_type, vehicle_color)
    free_index = get_free_spot(inventory)
    inventory[free_index] = new_vehicle

def sell_vehicle(inventory):
    if inventory_empty(inventory):
        return

    vehicle = choice(inventory)
    vehicle_index = inventory.index(vehicle)
    inventory[vehicle_index] = EMPTY_SLOT

def update_inventory(inventory):
    we_buying = randint(0,1)
    we_selling = randint(0,1)

    if we_buying:
        buy_vehicle(inventory)
    if we_selling:
        sell_vehicle(inventory)

def display_inventory(inventory):
    print('Your inventory:   (Current maximum: {})'.format(MAX_INVENTORY))
    for i in range(MAX_INVENTORY):
        print('  {}. {}'.format(i+1,inventory[i]))

def clear_screen():
    # Windows
    if name == 'nt':
        system('cls')
    # Other
    else:
        system('clear')

def game_tick(inventory):
    '''Call the functions that should occur each tick cycle.'''
    update_inventory(inventory)
    clear_screen()
    display_inventory(inventory)

#-------------------------------------------

# Initialize our Chaos
seed(time())

# Initialize my inventory.
my_garage = [ EMPTY_SLOT for i in range(MAX_INVENTORY) ]

# Initialize tick timer.
last_tick_time = time()

# Game tick cycle.
clear_screen()
display_inventory(my_garage)
while True:
    try:
        current_time = time()
        if current_time - last_tick_time >= TICK:
            game_tick(my_garage)
            last_tick_time = current_time
    except KeyboardInterrupt:
        print('')
        print('Exiting...')
        exit()
