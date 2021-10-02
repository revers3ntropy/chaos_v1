import constants
import worlds
import menu
import globals
import typing


def init_start_buttons():
    play_buttons = {}
    delete_buttons = {}
    for i in range(constants.number_of_worlds):
        delete_buttons[i] = 0
        if worlds.worlds[i] != 0:
            play_buttons[i] = menu.StandardButton(constants.screen_x / 2, (constants.screen_y / 2) + i * 50, typing.chaos_14x16,
                                                  worlds.worlds[i][worlds.name], 'game')
            delete_buttons[i] = menu.StandardButton(constants.screen_x / 2 + 300, (constants.screen_y / 2) + i * 50,
                                                    typing.chaos_14x16, 'delete', '1')
        else:
            play_buttons[i] = menu.StandardButton(constants.screen_x / 2, (constants.screen_y / 2) + i * 50, typing.chaos_14x16,
                                                  'create world', 'create world')
    return play_buttons, delete_buttons


def run():
    buttons = init_start_buttons()
    for j in range(constants.number_of_worlds):
        world_button = buttons[0][j].run()
        if world_button is not None:
            globals.current_world = j
            return world_button
        if buttons[1][j] != 0:
            delete = buttons[1][j].run()
            if delete is not None:
                worlds.worlds[j] = 0
                # possibly save here, although would mean ou could never get your world back

    return 'start menu'
