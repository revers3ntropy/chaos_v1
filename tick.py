import constants
import inventory
import action
import world_generation
import renderer
import movement
import globals
import block_selector


def chunk_refresh(view_distance_x, view_distance_y, character, chunks, shown_chunks, in_chunk_x, in_chunk_y):
    for i in range(-view_distance_x, view_distance_x):
        for j in range(-view_distance_y, view_distance_y):
            current_chunk = (i + character[in_chunk_x], j + character[in_chunk_y])
            if current_chunk in chunks:
                shown_chunks.append(current_chunk)
            else:
                world_generation.generate_chunk(current_chunk[0], current_chunk[1], constants.chunk_size, constants.world_size_z)
                shown_chunks.append(current_chunk)

    for i in range(-view_distance_x-1, view_distance_x+1):
        for j in range(-view_distance_y-1, view_distance_y+1):
            current_chunk = (i + character[in_chunk_x], j + character[in_chunk_y])
            if current_chunk not in chunks:
                world_generation.generate_chunk(current_chunk[0], current_chunk[1], constants.chunk_size, constants.world_size_z)


def tick(character, screen, walk_speed, screen_x, screen_y, visible, chunks, tile_size, x, y, z, solid,
         direction, up, down, left, right, action_cool_down, place_cool_down_mod, destroy_cool_down_mod, touching_ground,
         selected, selected_x, selected_y, destroy_range, unknown, in_chunk_x, in_chunk_y, view_distance_x,
         view_distance_y, world, keys_pressed):

    shown_chunks = []
    character_chunk = tuple((character[in_chunk_x], character[in_chunk_y]))
    chunk_refresh(view_distance_x, view_distance_y, character, chunks, shown_chunks, in_chunk_x, in_chunk_y)

    if globals.writing is False:
        character_chunk = movement.move(character, direction, chunks, character_chunk, x, y, z, solid, walk_speed,
                                        in_chunk_x, in_chunk_y, touching_ground, keys_pressed)

    action.cool_down_action(character, action_cool_down)
    action.check_actions(character, action_cool_down, selected_x, selected_y, x, y, z, destroy_range, chunks,
                         character_chunk, destroy_cool_down_mod, place_cool_down_mod)
    action.pick_up_items(chunks, character_chunk, character, x, y, z, inventory)

    inventory.scroll_through_inventory(keys_pressed, world)

    block_selector.select_block(character, x, y, z, tile_size, chunks, character_chunk, selected, solid)

    renderer.render_world(shown_chunks, screen, right, left, up, down, character, x, y, z, chunks, unknown,
                          solid, character_chunk, tile_size, screen_x, screen_y, visible, selected, destroy_range)
    renderer.render_character(screen_x, screen_y, character, direction, up, left, right, down, screen)
    renderer.draw_hotbar(screen)
    renderer.draw_selector(screen)
