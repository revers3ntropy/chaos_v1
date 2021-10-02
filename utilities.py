import items
import pygame as py
import math
import mobs
import random
import constants
import globals
import pickle


def throw_error(message):
    print('An error has occurred:')
    print('Error: ' + str(message))
    py.quit()
    quit()


def generate_properties(item_type):
    properties = {}
    for p in items.item_types[item_type]:
        properties[p] = items.starting_values[item_type][p]
    return properties


def generate_mob(mob_type):
    properties = {}
    for p in mobs.mob_types[mob_type]:
        properties[p] = mobs.starting_values[mob_type][p]
    return properties


def generate_grid(width, height, depth, fill):
    grid = []
    for i in range(depth):
        rectangle = []
        for j in range(width):
            line = []
            for k in range(height):
                line.append(fill)
            rectangle.append(line)
        grid.append(rectangle)
    return grid


def generate_2d_grid(width, height, fill):
    grid = []
    for j in range(width):
        line = []
        for k in range(height):
            line.append(fill)
        grid.append(line)
    return grid


def print_grid(grid):
    for o in range(len(grid)):
        layer = grid[o]
        for i in range(len(layer)):
            print(layer[i])


def check_surroundings(grid, item_type, x, y, z, search_range):
    found = 0
    for i in range(-search_range, search_range+1):  # y search
        for j in range(-search_range, search_range+1):  # x search
            try:
                if grid[z][y + i][x + j][items.type_] == item_type:
                    found += 1
            except:
                pass
    return found


def check_for_non_solids(chunk, x, y, z, chunks):
    # Returns the number of non-solid blocks surrounding the specified block.
    found = 0
    for i in range(-1, 2):  # y search
        for j in range(-1, 2):  # x search
            if i == 0 or j == 0:
                chunk_ = chunk
                y_mod = i
                x_mod = j

                if i + y > constants.chunk_size-1:
                    chunk_ = (chunk[0], int(chunk[1])+1)
                    y_mod = -y
                elif i + y < 0:
                    chunk_ = (chunk[0], int(chunk[1])-1)
                    y_mod = constants.chunk_size - y - 1

                if j + x > constants.chunk_size-1:
                    chunk_ = (int(chunk[0])+1, chunk[1])
                    x_mod = -x
                elif j + x < 0:
                    chunk_ = (int(chunk[0])-1, chunk[1])
                    x_mod = constants.chunk_size - x - 1

                if not chunks[chunk_][z][y + y_mod][x + x_mod][items.solid]:
                    found += 1

    return found


def check_collision(hit_a, hit_b):
    if hit_a[0] < hit_b[0] or hit_a[0] > hit_b[2]:
        return False
    elif hit_a[3] < hit_b[1] or hit_a[1] > hit_b[3]:
        return False
    return True


def get_distance(coords_a, coords_b):
    s = dict()
    s[1] = coords_a[1] - coords_b[1]  # finds length of vertical side using the y coords passed in
    s[2] = coords_a[0] - coords_b[0]  # finds length of horizontal side using the y coords passed in
    temp = abs(s[1] ^ 2) + abs(s[2] ^ 2)
    s[3] = math.sqrt(temp)
    return int(round(s[3]))


def gen_random_number_with_x_digits(length):
    if length > 0:
        number = random.randint(1, 9)
        if length > 1:
            for i in range(length-1):
                number = int(str(number) + str(random.randint(1, 9)))
    else:
        number = 0
    return number


def search(database, item):
    place = 0
    for i in range(len(database)):
        if database[i] == item:
            if place != 0:
                throw_error('multiple items found in search')
            else:
                place = i
    if place == 0:
        return False
    else:
        return place


def update_esc(keys):
    globals.esc_pressed_history = globals.esc_pressed
    if keys[py.K_ESCAPE]:
        globals.esc_pressed = 1
    else:
        globals.esc_pressed = 0


def get_new_esc(keys):
    if keys[py.K_ESCAPE] and not globals.esc_pressed_history:
        return True
    else:
        return False


def save_worlds(data):
    with open('worlds_data.txt', 'wb') as pickle_file:
        pickle.dump(data, pickle_file)

    print('Saved!')


def load_worlds_from_last_save():
    with open('worlds_data.txt', 'rb') as pickle_file:
        return pickle.load(pickle_file)
