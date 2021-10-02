import pygame as py

mobs = []

# mob types
PIG = 0
WOLF = 1

# mob qualities
images = 1
x = 2
y = 3
z = 4
visible = 5
solid = 6
health = 7
type_ = 8
primary_damage = 9
secondary_damage = 10
selected = 11

floor_top = 12
floor_bottom = 13
floor_right = 14
floor_left = 15
up_top = 16
up_bottom = 17
up_right = 18
up_left = 19

# list of mobs and properties
standard_animal_passive = [images, visible, solid, health, type_, primary_damage, selected, x, y, z]
standard_animal_aggressive = [images, visible, solid, health, type_, primary_damage, secondary_damage, selected, x, y, z]

# which characteristics the mobs have
mob_types = {
    PIG: standard_animal_passive,
    WOLF: standard_animal_aggressive
}

# list of the starting properties of each item
starting_values = {
    PIG: {
        images: {
            floor_top: py.image.load('graphics/entities/pig/pig_floor_top.png'),
            floor_bottom: py.image.load('graphics/entities/pig/pig_floor_bottom.png'),
            floor_right: py.image.load('graphics/entities/pig/pig_floor_right.png'),
            floor_left: py.image.load('graphics/entities/pig/pig_floor_left.png'),
            up_top: py.image.load('graphics/entities/pig/pig_top.png'),
            up_bottom: py.image.load('graphics/entities/pig/pig_bottom.png'),
            up_right: py.image.load('graphics/entities/pig/pig_right.png'),
            up_left: py.image.load('graphics/entities/pig/pig_left.png')
            },
        visible: True,
        solid: True,
        health: 50,
        type_: PIG,
        primary_damage: 5,
        x: 0,
        y: 0,
        z: 0
    },

    WOLF: {
        images: {
            floor_top: py.image.load('graphics/entities/pig/pig_floor_top.png'),
            floor_bottom: py.image.load('graphics/entities/pig/pig_floor_bottom.png'),
            floor_right: py.image.load('graphics/entities/pig/pig_floor_right.png'),
            floor_left: py.image.load('graphics/entities/pig/pig_floor_left.png'),
            up_top: py.image.load('graphics/entities/pig/pig_top.png'),
            up_bottom: py.image.load('graphics/entities/pig/pig_bottom.png'),
            up_right: py.image.load('graphics/entities/pig/pig_right.png'),
            up_left: py.image.load('graphics/entities/pig/pig_left.png')
        },
        visible: True,
        solid: True,
        health: 35,
        type_: WOLF,
        primary_damage: 10,
        secondary_damage: 5,
        x: 0,
        y: 0,
        z: 0
    }
}
