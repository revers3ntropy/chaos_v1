import pygame as py
import constants
import tick
import items
import globals
import worlds
import images
import utilities
import SFX


def run(keys):
    fps = 0

    world = worlds.worlds[globals.current_world]
    character = world[worlds.character]

    tick.tick(character, constants.screen, worlds.walk_speed, constants.screen_x,
              constants.screen_y, items.visible, world[worlds.chunks],
              constants.tile_size, worlds.x, worlds.y, worlds.z, items.solid, worlds.direction, images.up,
              images.down, images.left, images.right, worlds.action_cool_down, worlds.place_cool_down_mod,
              worlds.destroy_cool_down_mod, worlds.touching_ground, items.selected, globals.selected_x,
              globals.selected_y, worlds.destroy_range, images.unknown, worlds.in_chunk_x,
              worlds.in_chunk_y, constants.view_distance_x, constants.view_distance_y,
              worlds.worlds[globals.current_world], keys)

    if worlds.worlds[globals.current_world][worlds.tick_number] % constants.FPS_refresh_rate == 0:
        fps = globals.FPS

    character_x = str((int(character[worlds.x])+(world[worlds.character][worlds.in_chunk_x]*constants.chunk_size)))
    character_y = str((int(character[worlds.y])+(world[worlds.character][worlds.in_chunk_y]*constants.chunk_size)))
    display_message = ('Chaos | x: ' + character_x + ' | y: ' + character_y + ' | z: ' + str(
        character[worlds.z]) + ' | FPS: ' + str(fps))  # message for top of screen
    py.display.set_caption(display_message)

    worlds.worlds[globals.current_world][worlds.tick_number] += 1

    if utilities.get_new_esc(keys):
        SFX.play_sfx('button_001')
        return 'pause game'
    else:
        return 'game'
