import constants
import images
import menu
import typing

play_button = menu.StandardButton(constants.screen_x/2, constants.screen_y/2, typing.chaos_14x16, 'play', 'start menu')
settings_button = menu.StandardButton(constants.screen_x/2, constants.screen_y/2+50, typing.chaos_14x16, 'settings', 'settings')


def run():
    constants.screen.blit(images.game_logo, (constants.screen_x/2-130, 100))

    play = play_button.run()
    if play is not None:
        return play

    settings = settings_button.run()
    if settings is not None:
        return settings

    return 'main menu'
