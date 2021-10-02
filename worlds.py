import constants
import random
import utilities

try:
    worlds = utilities.load_worlds_from_last_save()
except Exception as err:
    print('Welcome new player!')
    worlds = {}
    for i in range(constants.number_of_worlds):  # sets a empty dict of worlds ready to be made
        worlds[i] = 0

# world qualities
seed = 1
chunks = 2
tick_number = 3
name = 4

chunk_boarders = 5

inventory = 6
show_inventory = 7
inventory_selected = 8

character = 9

x = 10
y = 11
z = 12
visible = 13
solid = 14
walk_speed = 15
walking = 16
direction = 17
action_cool_down = 18
place_cool_down_mod = 19
destroy_cool_down_mod = 20
touching_ground = 21
movement_action = 22
destroy_range = 23
in_chunk_x = 24
in_chunk_y = 25


def new_world(world_number, world_seed, world_name):
    worlds[world_number] = {
        seed: world_seed,
        chunks: {},
        tick_number: 0,
        name: world_name,
        inventory: {},
        chunk_boarders: False,
        show_inventory: False,
        inventory_selected: 0,
        character: {
            x: int(constants.chunk_size / 2),
            y: int(constants.chunk_size / 2),
            z: int((constants.world_size_z / 2) + constants.world_size_z / 10),
            walk_speed: 1,
            walking: False,
            visible: True,
            solid: False,
            direction: 0,
            action_cool_down: 0,
            place_cool_down_mod: 3,
            destroy_cool_down_mod: 5,
            touching_ground: False,
            movement_action: False,
            destroy_range: 2,
            in_chunk_x: random.randint(-10, 10),
            in_chunk_y: random.randint(-10, 10),
        }
    }

    for o in range(constants.inventory_size):
        worlds[world_number][inventory][o] = 0
