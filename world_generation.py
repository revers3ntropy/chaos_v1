import utilities
import items
import constants
import noise
import random
import globals
import worlds


def tree(wood_type, grid, x, y, z, height):
    for i in range(height):
        grid[z+i][y][x] = utilities.generate_properties(wood_type)


def generate_super_flat_grass_no_trees(chunk_x, chunk_y, chunk_size, world_size_z, level):
    chunk = utilities.generate_grid(chunk_size, chunk_size, world_size_z, 0)
    for layer in range(world_size_z):
        for row in range(chunk_size):
            for instance in range(chunk_size):
                if level > layer:
                    chunk[layer][row][instance] = utilities.generate_properties(items.GRASS_TILE)
                else:
                    chunk[layer][row][instance] = utilities.generate_properties(items.AIR)
    worlds.worlds[globals.current_world][worlds.chunks][(chunk_x, chunk_y)] = chunk


def generate_super_flat_grass_trees(chunk_x, chunk_y, chunk_size, world_size_z, level):
    chunk = utilities.generate_grid(chunk_size, chunk_size, world_size_z, 0)
    for layer in range(world_size_z):
        for row in range(chunk_size):
            for instance in range(chunk_size):
                if level > layer:
                    chunk[layer][row][instance] = utilities.generate_properties(items.GRASS_TILE)
                elif level == layer and random.randint(1, constants.tree_density) == 1:
                    chunk[layer][row][instance] = utilities.generate_properties(items.OAK_WOOD_TILE)
                else:
                    chunk[layer][row][instance] = utilities.generate_properties(items.AIR)
    worlds.worlds[globals.current_world][worlds.chunks][(chunk_x, chunk_y)] = chunk


def generate_chunk(chunk_x, chunk_y, chunk_size, world_size_z):
    seed = worlds.worlds[globals.current_world][worlds.seed]
    chunk = utilities.generate_grid(chunk_size, chunk_size, world_size_z, 0)
    for row in range(chunk_size):
        for instance in range(chunk_size):
            x_temp = (row + (chunk_y * chunk_size) + (seed/10000000))
            y_temp = (instance + (chunk_x * chunk_size) + (seed/10000000))
            height = int(round(((noise.pnoise2(x_temp / constants.scale, y_temp / constants.scale, octaves=constants.octaves,
                                 persistence=constants.persistence, lacunarity=constants.lacunarity, repeatx=seed,
                                 repeaty=seed, base=constants.shape))+1)*(world_size_z/2)))
            for i in range(height):  # height is a number between -1 and 1 I think, so make it larger and compare to something
                chunk[i][row][instance] = utilities.generate_properties(items.STONE_TILE)
            chunk[height-2][row][instance] = utilities.generate_properties(items.DIRT_TILE)
            chunk[height-1][row][instance] = utilities.generate_properties(items.GRASS_TILE)
            for i in range(world_size_z-height):
                chunk[i+height][row][instance] = utilities.generate_properties(items.AIR)

            worlds.worlds[globals.current_world][worlds.chunks][(chunk_x, chunk_y)] = chunk

    for row in range(chunk_size):
        for instance in range(chunk_size):
            if 1 < instance < constants.chunk_size-1 and 1 < row < constants.chunk_size-1:
                if random.randint(1, constants.tree_density) == 1:
                    found = False
                    for i in range(world_size_z):
                        if found is False and chunk[i - 1][row][instance][items.type_] == items.GRASS_TILE and \
                                chunk[i][row][instance][items.solid] is False:
                            found = True
                            if utilities.check_for_non_solids((chunk_x, chunk_y), instance,
                                                              row, i, worlds.worlds[globals.current_world][worlds.chunks]) == 5:
                                if random.randint(1, 2) == 1:
                                    tree(items.OAK_WOOD_TILE, chunk, instance, row, i, 5)
                                else:
                                    tree(items.WILLOW_WOOD_TILE, chunk, instance, row, i, 5)
    worlds.worlds[globals.current_world][worlds.chunks][(chunk_x, chunk_y)] = chunk
