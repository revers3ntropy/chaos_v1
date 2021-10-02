import random
import pygame as py

py.init()
screen = py.display.set_mode((0, 0), py.FULLSCREEN)
screen_x = screen.get_rect().width
screen_y = screen.get_rect().height
clock = py.time.Clock()

background_colour = (140, 140, 140)
run_FPS = 60
FPS_refresh_rate = 3

number_of_worlds = 5

shape = 1  # -10000000 to 10000000 | try to keep 1, or at least not a random number until you know what it actually does
scale = 15000
octaves = 5
persistence = 0.01
lacunarity = 2500

tile_size = 32

world_size_z = 256

chunk_size = 8

tree_density = random.randint(10, 15)  # the higher the number, the less trees will
tree_range = 3

inventory_size = 3

view_distance_x = 4
view_distance_y = 3
max_view_distance_z = 10

screen.fill(background_colour)
