import constants
import globals
import worlds
import menu
import typing
import random

create_world_button = menu.StandardButton(constants.screen_x / 2, constants.screen_y / 2, typing.chaos_14x16, 'create world', 'game')

seed_box = menu.TextButton(constants.screen_x/2, constants.screen_y/2 + 60, typing.chaos_14x16, 'world seed',
                           (175, 175, 175), (100, 100, 100), 16, (200, 200, 200))
name_box = menu.TextButton(constants.screen_x/2, constants.screen_y/2 + 120, typing.chaos_14x16, 'world name',
                           (175, 175, 175), (100, 100, 100), 16, (200, 200, 200))


def check_seed(seed):
    for i in range(len(seed)):
        seed = list(seed)
        if seed[i] not in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
            seed[i] = str(random.randint(0, 10))

    seed = "".join(seed)
    return seed


def run():
    create_world = create_world_button.run()

    seed_box.run()
    name_box.run()

    if create_world is not None:

        my_seed = seed_box.run()
        my_name = name_box.run()

        if my_seed != 'world seed':
            my_seed = int(check_seed(my_seed))

        worlds.new_world(globals.current_world, my_seed, my_name)
        return create_world

    return 'create world'
