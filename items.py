items = []

# item types
AIR = 0
GRASS_TILE = 1
DIRT_TILE = 2
STONE_TILE = 3
OAK_WOOD_TILE = 4
WILLOW_WOOD_TILE = 5

# item qualities
visible = 5
solid = 6
durability = 21
resistance = 23
type_ = 24
block = 26
item = 27
entity = 28
stackable_to = 29
breakable = 30
selected = 31
floor = 32
contains = 36

# list of items and properties
standard_block = [visible, solid, durability, resistance, type_, block, item, entity, breakable, selected]

item_types = {
    AIR: [visible, solid, type_, block, item, entity, breakable, selected, contains],
    GRASS_TILE: standard_block,
    DIRT_TILE: standard_block,
    STONE_TILE: standard_block,
    OAK_WOOD_TILE: standard_block,
    WILLOW_WOOD_TILE: standard_block
}

# list of the starting properties of each item
starting_values = {
    AIR: {
        visible: False,
        solid: False,
        durability: 0,
        resistance: 0,
        type_: AIR,
        block: True,
        item: False,
        entity: False,
        breakable: False,
        selected: False,
        contains: False
    },
    GRASS_TILE: {
        visible: True,
        solid: True,
        durability: 10,
        resistance: 10,
        type_: GRASS_TILE,
        block: True,
        item: False,
        entity: False,
        breakable: True,
        selected: False
    },
    DIRT_TILE: {
        visible: True,
        solid: True,
        durability: 10,
        resistance: 10,
        type_: DIRT_TILE,
        block: True,
        item: False,
        entity: False,
        breakable: True,
        selected: False
    },
    STONE_TILE: {
        visible: True,
        solid: True,
        durability: 50,
        resistance: 50,
        type_: STONE_TILE,
        block: True,
        item: False,
        entity: False,
        breakable: True,
        selected: False
    },
    OAK_WOOD_TILE: {
        visible: True,
        solid: True,
        durability: 30,
        resistance: 30,
        type_: OAK_WOOD_TILE,
        block: True,
        item: False,
        entity: False,
        breakable: True,
        selected: False
    },
    WILLOW_WOOD_TILE: {
        visible: True,
        solid: True,
        durability: 25,
        resistance: 25,
        type_: WILLOW_WOOD_TILE,
        block: True,
        item: False,
        entity: False,
        breakable: True,
        selected: False
    }
}
