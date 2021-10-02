import worlds
import constants
import menu
import utilities
import typing

back_to_game = menu.StandardButton(constants.screen_x / 2, constants.screen_y / 2, typing.chaos_14x16, 'Back to Game', 'game')
main_menu = menu.StandardButton(constants.screen_x / 2, constants.screen_y / 2 - 90, typing.chaos_14x16, 'Save and Exit', 'main menu')


def run(keys):
    save_and_exit = main_menu.run()
    if save_and_exit is not None:
        utilities.save_worlds(worlds.worlds)
        return save_and_exit

    exit_pause = back_to_game.run()
    if exit_pause is not None:
        return exit_pause

    if utilities.get_new_esc(keys):
        return 'game'

    return 'pause game'
