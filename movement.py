import pygame as py
import constants


def move(character, direction, chunks, character_chunk, x, y, z, solid, walk_speed, in_chunk_x, in_chunk_y, touching_ground, keys_pressed):

    if keys_pressed[py.K_a]:
        character[direction] = 3
        if character[x] > 0:
            if chunks[character_chunk][character[z]][character[y]][character[x] - 1][solid] is False:
                character[x] -= character[walk_speed]
            else:
                if not chunks[character_chunk][character[z] + 1][character[y]][character[x] - 1][solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[x] -= 1
        else:
            if chunks[(character[in_chunk_x] - 1, character[in_chunk_y])][character[z]][character[y]][constants.chunk_size - 1][solid] is False:
                character[in_chunk_x] -= 1
                character[x] = constants.chunk_size - 1
                character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))
            else:
                if not chunks[(character[in_chunk_x] - 1, character[in_chunk_y])][character[z] + 1][character[y]][
                    constants.chunk_size - 1][solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[in_chunk_x] -= 1
                    character[x] = constants.chunk_size - 1
                    character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))

    if keys_pressed[py.K_d]:
        character[direction] = 1
        if character[x] < constants.chunk_size - 1:
            if chunks[character_chunk][character[z]][character[y]][character[x] + 1][solid] is False:
                character[x] += character[walk_speed]
            else:
                if not chunks[character_chunk][character[z] + 1][character[y]][character[x] + 1][solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[x] += 1

        else:
            if chunks[(character[in_chunk_x] + 1, character[in_chunk_y])][character[z]][character[y]][0][solid] is False:
                character[in_chunk_x] += 1
                character[x] = 0
                character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))
            else:
                if not chunks[(character[in_chunk_x] + 1, character[in_chunk_y])][character[z] + 1][character[y]][0][
                    solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[in_chunk_x] += 1
                    character[x] = 0
                    character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))

    if keys_pressed[py.K_w]:
        character[direction] = 0
        if character[y] > 0:
            if chunks[character_chunk][character[z]][character[y] - 1][character[x]][solid] is False:
                character[y] -= character[walk_speed]
            else:
                if not chunks[character_chunk][character[z] + 1][character[y] - 1][character[x]][solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[y] -= 1

        else:
            if chunks[(character[in_chunk_x], character[in_chunk_y] - 1)][character[z]][constants.chunk_size - 1][character[x]][solid] is False:
                character[in_chunk_y] -= 1
                character[y] = constants.chunk_size - 1
                character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))
            else:
                if not chunks[(character[in_chunk_x], character[in_chunk_y] - 1)][character[z] + 1][constants.chunk_size - 1][
                    character[x]][solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[in_chunk_y] -= 1
                    character[y] = constants.chunk_size - 1
                    character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))

    if keys_pressed[py.K_s]:
        character[direction] = 2
        if character[y] < constants.chunk_size - 1:
            if chunks[character_chunk][character[z]][character[y] + 1][character[x]][solid] is False:
                character[y] += character[walk_speed]
            else:
                if not chunks[character_chunk][character[z] + 1][character[y] + 1][character[x]][solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[y] += 1
        else:
            if chunks[(character[in_chunk_x], character[in_chunk_y] + 1)][character[z]][0][character[x]][solid] is False:
                character[in_chunk_y] += 1
                character[y] = 0
                character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))
            else:
                if not chunks[(character[in_chunk_x] + 1, character[in_chunk_y])][character[z] + 1][0][character[x]][
                    solid] and \
                        not chunks[character_chunk][character[z] + 1][character[y]][character[x]][solid]:
                    character[z] += 1
                    character[in_chunk_y] += 1
                    character[y] = 0
                    character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))

    try:
        if chunks[character_chunk][character[z] - 1][character[y]][character[x]][solid] is False and 1 < character[z] < constants.world_size_z - 1:  # gravity
            character[z] -= 1
            character[touching_ground] = False
        else:
            character[touching_ground] = True
    except:
        pass

    return character_chunk
