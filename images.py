import pygame as py
import items

highlighter = {
    1: py.image.load('graphics/menu/game/selector_up.png'),
    2: py.image.load('graphics/menu/game/selector_up_unselected.png'),
    3: py.image.load('graphics/menu/game/selector_down.png'),
    4: py.image.load('graphics/menu/game/selector_down_unselected.png')
}

up = 32
left = 33
right = 34
down = 35
chunk_boarder = {up: py.image.load('graphics/menu/game/chunk_boarder_top.png'),
                 down: py.image.load('graphics/menu/game/chunk_boarder_bottom.png'),
                 left: py.image.load('graphics/menu/game/chunk_boarder_left.png'),
                 right: py.image.load('graphics/menu/game/chunk_boarder_right.png')
                 }

unknown = py.image.load('graphics/blocks/background.png')

hot_bar_image = py.image.load('graphics/menu/game/inventory_slot.png')

down_shader = py.image.load('graphics/blocks/down_shader.png')
up_shader = py.image.load('graphics/blocks/up_shader.png')

pointerImg = py.image.load('graphics/menu/game/curser.png')

moused = 2
hit_box = 3

game_logo = py.image.load('graphics/menu/main_menu/chaos_logo.png')

character_images = {
    up: py.image.load('graphics/entities/character/character_up.png'),
    left: py.image.load('graphics/entities/character/character_left.png'),
    right: py.image.load('graphics/entities/character/character_right.png'),
    down: py.image.load('graphics/entities/character/character_down.png')
}

floor = 1
item = 27

block_images = {items.GRASS_TILE: {
    floor: py.image.load('graphics/blocks/grass/grass.png'),
    item: py.image.load('graphics/blocks/grass/grass_item.png')
}, items.DIRT_TILE: {
    floor: py.image.load('graphics/blocks/dirt/dirt.png'),
    item: py.image.load('graphics/blocks/dirt/dirt_item.png')
}, items.STONE_TILE: {
    floor: py.image.load('graphics/blocks/stone/stone.png'),
    item: py.image.load('graphics/blocks/stone/stone_item.png')
}, items.OAK_WOOD_TILE: {
    floor: py.image.load('graphics/blocks/wood/oak/oak.png'),
    item: py.image.load('graphics/blocks/wood/oak/oak_item.png')
}, items.WILLOW_WOOD_TILE: {
    floor: py.image.load('graphics/blocks/wood/willow/willow.png'),
    item: py.image.load('graphics/blocks/wood/willow/willow_item.png')
},
}
