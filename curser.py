import pygame as py
import globals


def update_mouse_clicked():
    globals.mouse_pressed_history = globals.mouse_pressed
    if py.mouse.get_pressed()[0]:
        globals.mouse_pressed = 1
    else:
        globals.mouse_pressed = 0


def check_mouse_collision(hit_box):
    mouse_pos = py.mouse.get_pos()
    if hit_box[0] < mouse_pos[0] < hit_box[0]+hit_box[2] and hit_box[1] < mouse_pos[1] < hit_box[1]+hit_box[3]:
        return True
    else:
        return False


def check_new_click():
    if py.mouse.get_pressed()[0] and not globals.mouse_pressed_history:
        return True
    else:
        return False
