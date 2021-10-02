import pygame as py
import globals


def select_block(character, x, y, z, tile_size, chunks, character_chunk, selected, solid):
    x_temp = int(character[x] + round((py.mouse.get_pos()[0] - 2) / tile_size) - 23)
    y_temp = int(character[y] + round((py.mouse.get_pos()[1] - 52) / tile_size) - 13)
    try:
        if chunks[character_chunk][character[z]][y_temp][x_temp][solid]:
            chunks[character_chunk][character[z]][y_temp][x_temp][selected] = True
            globals.selected_up = True
        else:
            chunks[character_chunk][character[z] - 1][y_temp][x_temp][selected] = True
            globals.selected_up = False
        globals.selected_x = x_temp
        globals.selected_y = y_temp
    except:
        pass
