import items
import globals
import utilities
import worlds
import pygame as py


def break_block(x, y, z, grid):
    my_item = grid[z][y][x]
    if my_item[items.breakable]:
        my_item[items.durability] -= 1
        if my_item[items.durability] < 1:
            my_item[items.item] = True
            my_item[items.block] = False
            my_item[items.solid] = False
            my_item[items.durability] = items.starting_values[my_item[items.type_]][items.durability]


def place_block(x, y, z, world, character_chunk):
    if not world[worlds.chunks][character_chunk][z][y][x][items.solid]:
        world[worlds.chunks][character_chunk][z][y][x] = utilities.generate_properties(world[worlds.inventory][world[worlds.inventory_selected]][items.type_])
        world[worlds.inventory][world[worlds.inventory_selected]] = 0


def check_actions(character, action_cool_down, selected_x, selected_y, x, y, z, destroy_range, chunks, character_chunk,
                  destroy_cool_down_mod, place_cool_down_mod):
    if py.mouse.get_pressed()[0]:  # break block
        if character[action_cool_down] == 0:
            if utilities.get_distance((selected_x, selected_y), (character[x], character[y])) <= character[destroy_range]:
                if globals.selected_up:
                    break_block(selected_x, selected_y, character[z], chunks[character_chunk])
                else:
                    break_block(selected_x, selected_y, character[z]-1, chunks[character_chunk])
                character[action_cool_down] = character[destroy_cool_down_mod]
    elif py.mouse.get_pressed()[2]:  # place block
        if worlds.worlds[globals.current_world][worlds.inventory][worlds.worlds[globals.current_world][worlds.inventory_selected]] != 0:
            if utilities.get_distance((selected_x, selected_y), (character[x], character[y])) <= character[destroy_range]:
                if globals.selected_up:
                    place_block(selected_x, selected_y, character[z], worlds.worlds[globals.current_world], character_chunk)
                else:
                    if chunks[character_chunk][character[z]-1][selected_y][selected_x][items.solid]:
                        place_block(selected_x, selected_y, character[z], worlds.worlds[globals.current_world], character_chunk)
                    else:
                        place_block(selected_x, selected_y, character[z]-1, worlds.worlds[globals.current_world], character_chunk)
                character[action_cool_down] = character[place_cool_down_mod]


def pick_up_items(chunks, character_chunk, character, x, y, z, inventory):
    if chunks[character_chunk][character[z]][character[y]][character[x]][items.item]:
        if inventory.add_to_inventory(utilities.generate_properties(
                chunks[character_chunk][character[z]][character[y]][character[x]][items.type_])) != 'no space':
            worlds.worlds[globals.current_world][worlds.chunks][character_chunk][character[z]][character[y]][character[x]] = utilities.generate_properties(items.AIR)


def cool_down_action(character, action_cool_down):
    if character[action_cool_down] != 0:
        character[action_cool_down] -= 1
