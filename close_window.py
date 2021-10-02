import pygame as py
import utilities
import worlds
import globals


def check_for_close(keys_pressed):
    for event in py.event.get():
        if event.type == py.QUIT:
            return False

    if globals.writing is False:
        if keys_pressed[py.K_q]:
            utilities.save_worlds(worlds.worlds)
            return False

        if keys_pressed[py.K_p]:
            return False
    return True
