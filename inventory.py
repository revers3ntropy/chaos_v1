import globals
import constants
import worlds
import pygame as py


def add_to_inventory(item):
    inventory = worlds.worlds[globals.current_world][worlds.inventory]
    found_place = False
    for j in range(constants.inventory_size):  # loops through possible places in the inventory
        if inventory[j] == 0 and found_place is False:  # checks if location is valid or not - will assign item to first available slot
            inventory[j] = item  # assigns item to inventory slot if there is nothing in it
            found_place = True
    if found_place is False:
        return 'no space'


def draw_inventory():
    pass


def scroll_through_inventory(keys_pressed, world):
    if keys_pressed[py.K_UP]:   # inventory selection
        if world[worlds.inventory_selected] == 0:
            globals.inventory_selected = constants.inventory_size-1
        else:
            world[worlds.inventory_selected] -= 1
    if keys_pressed[py.K_DOWN]:
        if world[worlds.inventory_selected] == constants.inventory_size-1:
            world[worlds.inventory_selected] = 0
        else:
            world[worlds.inventory_selected] += 1
