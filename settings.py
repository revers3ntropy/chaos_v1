import constants
import menu
import utilities
import settings_variables
import worlds
import typing

render_distance_states = []
for i in range(constants.max_view_distance_z-1):  # 1 for the min render distance
    render_distance_states.append('View distance: ' + str(i+1))
render_distance_switch = menu.SwitchButton(constants.screen_x / 2, constants.screen_y / 2 - 100, typing.chaos_14x16,
                                           render_distance_states, 2)

music_switch = menu.SwitchButton(constants.screen_x / 2, constants.screen_y / 2, typing.chaos_14x16,
                                 ('music: on', 'music: off'), 0)

sfx_switch = menu.SwitchButton(constants.screen_x / 2, constants.screen_y / 2 - 50, typing.chaos_14x16,
                               ('sfx: on', 'sfx: off'), 0)

exit_button = menu.StandardButton(constants.screen_x / 2 - 150, constants.screen_y / 2 + 50, typing.chaos_14x16, 'exit', '1')
save_button = menu.StandardButton(constants.screen_x / 2 + 150, constants.screen_y / 2 + 50, typing.chaos_14x16, 'save', '1')


def run():
    settings_variables.music = music_switch.run()
    settings_variables.view_distance_z = render_distance_switch.run()
    settings_variables.sfx = sfx_switch.run()

    if save_button.run():
        utilities.save_worlds(worlds.worlds)

    if exit_button.run():
        return 'main menu'

    return 'settings'
