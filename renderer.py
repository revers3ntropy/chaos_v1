import constants
import globals
import settings_variables
import items
import utilities
import worlds
import images
import pygame as py


def render_character(screen_x, screen_y, character, direction, up, left, right, down, screen):
    x_temp = screen_x / 2  # centers character in the screen
    y_temp = screen_y / 2
    if character[direction] == 0:  # renders character in different directions
        screen.blit(images.character_images[up], (x_temp, y_temp))
    elif character[direction] == 3:
        screen.blit(images.character_images[left], (x_temp, y_temp))
    elif character[direction] == 1:
        screen.blit(images.character_images[right], (x_temp, y_temp))
    elif character[direction] == 2:
        screen.blit(images.character_images[down], (x_temp, y_temp))
    else:
        character[direction] = 0


def render_world(shown_chunks, screen, right, left, up, down, character, x, y, z, chunks, unknown,
                 solid, character_chunk, tile_size, screen_x, screen_y, visible, selected, destroy_range):
    for o in shown_chunks:
        for i in range(constants.chunk_size):
            for j in range(constants.chunk_size):

                x_temp = ((j - character[x] + (o[0] * constants.chunk_size) - (
                            character_chunk[0] * constants.chunk_size)) * tile_size) + screen_x / 2
                y_temp = ((i - character[y] + (o[1] * constants.chunk_size) - (
                            character_chunk[1] * constants.chunk_size)) * tile_size) + screen_y / 2

                for p in range(-settings_variables.view_distance_z, 0):
                    z_coord = character[z]+p+1
                    instance = chunks[o][z_coord][i][j]
                    if instance[visible]:
                        if instance[items.item]:
                            if z_coord == character[z]:
                                if utilities.check_for_non_solids(o, j, i, z_coord, chunks) > 0:
                                    screen.blit(images.block_images[instance[items.type_]][images.item], (x_temp, y_temp))
                                    screen.blit(images.up_shader, (x_temp, y_temp))
                                else:
                                    screen.blit(unknown, (x_temp, y_temp))
                            else:
                                if not chunks[o][z_coord + 1][i][j][solid]:
                                    screen.blit(images.block_images[instance[items.type_]][images.item], (x_temp, y_temp))
                                    for u in range(character[z] - z_coord - 1):
                                        screen.blit(images.down_shader, (x_temp, y_temp))
                        elif instance[items.block]:
                            if z_coord == character[z]:
                                if utilities.check_for_non_solids(o, j, i, z_coord, chunks) > 0:
                                    screen.blit(images.block_images[instance[items.type_]][images.floor], (x_temp, y_temp))
                                    screen.blit(images.up_shader, (x_temp, y_temp))
                                else:
                                    screen.blit(unknown, (x_temp, y_temp))
                            else:
                                if not chunks[o][z_coord+1][i][j][solid]:
                                    screen.blit(images.block_images[instance[items.type_]][images.floor], (x_temp, y_temp))
                                    for u in range(character[z] - z_coord - 1):
                                        screen.blit(images.down_shader, (x_temp, y_temp))

                    if instance[selected]:
                        instance[selected] = False
                        selected_x = j
                        selected_y = i
                        if globals.selected_up:
                            if utilities.get_distance((selected_x, selected_y), (character[x], character[y])) <= character[destroy_range]:
                                screen.blit(images.highlighter[1], (x_temp, y_temp))
                            else:
                                screen.blit(images.highlighter[2], (x_temp, y_temp))
                        else:
                            if utilities.get_distance((selected_x, selected_y), (character[x], character[y])) <= character[destroy_range]:
                                screen.blit(images.highlighter[3], (x_temp, y_temp))
                            else:
                                screen.blit(images.highlighter[4], (x_temp, y_temp))

                if worlds.worlds[globals.current_world][worlds.chunk_boarders]:
                    if j == 0:
                        screen.blit(images.chunk_boarder[right], (x_temp, y_temp))
                    if j == constants.chunk_size:
                        screen.blit(images.chunk_boarder[left], (x_temp, y_temp))
                    if i == 0:
                        screen.blit(images.chunk_boarder[down], (x_temp, y_temp))
                    if i == constants.chunk_size:
                        screen.blit(images.chunk_boarder[up], (x_temp, y_temp))


def draw_selector(screen):
    screen.blit(images.highlighter[1], (14, (worlds.worlds[globals.current_world][worlds.inventory_selected] * 43) + 14))


def draw_hotbar(screen):
    inventory = worlds.worlds[globals.current_world][worlds.inventory]
    for o in range(constants.inventory_size):
        screen.blit(images.hot_bar_image, (10, (10+(o*43))))  # (10 # modifier # +(o*43 # size of the slot +
        # distance between them #), 15 # distance to edge of screen) placement for inventory
        if inventory[o] != 0:
            screen.blit(images.block_images[inventory[o][items.type_]][images.item], (15, (15+(o*43))))
    draw_selector(screen)


def curser():
    py.mouse.set_visible(False)
    constants.screen.blit(images.pointerImg, ((py.mouse.get_pos()[0] - 12), (py.mouse.get_pos()[1] - 12)))
