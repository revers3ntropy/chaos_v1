import pygame as py
import constants

typeable_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

typeable_characters_py_game = [py.K_a, py.K_b, py.K_c, py.K_d, py.K_e, py.K_f, py.K_g, py.K_h, py.K_i, py.K_j, py.K_k, py.K_l,
                               py.K_m, py.K_n, py.K_o, py.K_p, py.K_q, py.K_r, py.K_s, py.K_t, py.K_u, py.K_v, py.K_w, py.K_x,
                               py.K_y, py.K_z, py.K_1, py.K_2, py.K_3, py.K_4, py.K_5, py.K_6, py.K_7, py.K_8, py.K_9, py.K_0]

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

size_x = 27
size_y = 28

chaos_14x16 = 29

fonts = {
    chaos_14x16: {
        size_x: 28,
        size_y: 32,
        'a': py.image.load('graphics/chaos_14x16/A.png'),
        'b': py.image.load('graphics/chaos_14x16/B.png'),
        'c': py.image.load('graphics/chaos_14x16/C.png'),
        'd': py.image.load('graphics/chaos_14x16/D.png'),
        'e': py.image.load('graphics/chaos_14x16/E.png'),
        'f': py.image.load('graphics/chaos_14x16/F.png'),
        'g': py.image.load('graphics/chaos_14x16/G.png'),
        'h': py.image.load('graphics/chaos_14x16/H.png'),
        'i': py.image.load('graphics/chaos_14x16/I.png'),
        'j': py.image.load('graphics/chaos_14x16/J.png'),
        'k': py.image.load('graphics/chaos_14x16/K.png'),
        'l': py.image.load('graphics/chaos_14x16/L.png'),
        'm': py.image.load('graphics/chaos_14x16/M.png'),
        'n': py.image.load('graphics/chaos_14x16/N.png'),
        'o': py.image.load('graphics/chaos_14x16/O.png'),
        'p': py.image.load('graphics/chaos_14x16/P.png'),
        'q': py.image.load('graphics/chaos_14x16/Q.png'),
        'r': py.image.load('graphics/chaos_14x16/R.png'),
        's': py.image.load('graphics/chaos_14x16/S.png'),
        't': py.image.load('graphics/chaos_14x16/T.png'),
        'u': py.image.load('graphics/chaos_14x16/U.png'),
        'v': py.image.load('graphics/chaos_14x16/V.png'),
        'w': py.image.load('graphics/chaos_14x16/W.png'),
        'x': py.image.load('graphics/chaos_14x16/X.png'),
        'y': py.image.load('graphics/chaos_14x16/Y.png'),
        'z': py.image.load('graphics/chaos_14x16/Z.png'),
        '-': py.image.load('graphics/chaos_14x16/-.png'),
        '/': py.image.load('graphics/chaos_14x16/forward_slash.png'),
        '!': py.image.load('graphics/chaos_14x16/!.png'),
        '?': py.image.load('graphics/chaos_14x16/?.png'),
        '@': py.image.load('graphics/chaos_14x16/@.png'),
        '#': py.image.load('graphics/chaos_14x16/#.png'),
        '%': py.image.load('graphics/chaos_14x16/%.png'),
        '^': py.image.load('graphics/chaos_14x16/^.png'),
        '=': py.image.load('graphics/chaos_14x16/=.png'),
        '+': py.image.load('graphics/chaos_14x16/+.png'),
        '_': py.image.load('graphics/chaos_14x16/_.png'),
        ':': py.image.load('graphics/chaos_14x16/;.png'),  # wrong file, I know
        '0': py.image.load('graphics/chaos_14x16/0.png'),
        '1': py.image.load('graphics/chaos_14x16/1.png'),
        '2': py.image.load('graphics/chaos_14x16/2.png'),
        '3': py.image.load('graphics/chaos_14x16/3.png'),
        '4': py.image.load('graphics/chaos_14x16/4.png'),
        '5': py.image.load('graphics/chaos_14x16/5.png'),
        '6': py.image.load('graphics/chaos_14x16/6.png'),
        '7': py.image.load('graphics/chaos_14x16/7.png'),
        '8': py.image.load('graphics/chaos_14x16/8.png'),
        '9': py.image.load('graphics/chaos_14x16/9.png'),
    }
}


def write(font, message, x_pos, y_pos):
    my_font = fonts[font]
    message = str.lower(message)
    if len(message) > 0:
        for i in range(len(message)):
            if message[i] != ' ':
                letter_image = my_font[message[i]]
                pos_y = y_pos - my_font[size_y]/2
                pos_x = (i-(len(message)/2))*(my_font[size_x]+5) + x_pos
                constants.screen.blit(letter_image, (pos_x, pos_y))


def write_from_left(font, message, x_pos, y_pos):
    my_font = fonts[font]
    message = str.lower(message)
    if len(message) > 0:
        for i in range(len(message)):
            if message[i] != ' ':
                letter_image = my_font[message[i]]
                pos_y = y_pos - my_font[size_y]/2
                pos_x = i*(my_font[size_x]+20) + x_pos
                constants.screen.blit(letter_image, (pos_x, pos_y))
