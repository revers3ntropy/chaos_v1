import typing
import curser
import constants
import SFX
import pygame as py
import globals


class Buttons:
    def __init__(self, x, y, font):
        self.x = x
        self.y = y
        self.font = font
        self.moused = False
        self.sfx_when_pressed = 'button_001'

    def display(self, message):
        typing.write(self.font, message, self.x, self.y)

    def check_mouse(self, hit_box):
        if curser.check_mouse_collision(hit_box):
            self.moused = True
        else:
            self.moused = False

    def check_clicked(self):
        if self.moused and curser.check_new_click():
            return True
        return False


class StandardButton(Buttons):
    def __init__(self, x, y, font, message, leads_to):
        super().__init__(x, y, font)
        self.size_x = (typing.fonts[font][typing.size_x]+5) * len(message)
        self.hit_box = (x-self.size_x/2, y-typing.fonts[font][typing.size_y]/2, self.size_x, typing.fonts[font][typing.size_y])
        self.message = message
        self.leads_to = leads_to

    def run(self):
        self.check_mouse(self.hit_box)
        if self.moused:
            self.display('-'+self.message+'-')
        else:
            self.display(self.message)

        if self.check_clicked():
            SFX.play_sfx(self.sfx_when_pressed)
            return self.leads_to


class SwitchButton(Buttons):
    def __init__(self, x, y, font, states, starting_state):
        super().__init__(x, y, font)
        self.states = states  # list of messages
        self.current_state = starting_state  # number to start on

        self.number_of_states = len(states)
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * len(self.states[self.current_state])
        self.hit_box = (x-self.size_x/2, y-typing.fonts[font][typing.size_y]/2, self.size_x, typing.fonts[font][typing.size_y])

    def update_state(self):
        if self.number_of_states > 2:
            if self.current_state >= self.number_of_states-1:
                self.current_state = 1
            else:
                self.current_state += 1
            self.size_x = (typing.fonts[self.font][typing.size_x] + 5) * len(self.states[self.current_state])
            self.hit_box = (self.x - self.size_x / 2, self.y - typing.fonts[self.font][typing.size_y] / 2, self.size_x,
                            typing.fonts[self.font][typing.size_y])
        else:
            if self.current_state == 1:
                self.current_state = 0
            else:
                self.current_state = 1

    def run(self):
        self.check_mouse(self.hit_box)
        if self.moused:
            self.display('-'+self.states[self.current_state]+'-')
        else:
            self.display(self.states[self.current_state])

        if self.check_clicked():
            self.update_state()

        return self.current_state


class TextButton(Buttons):
    def __init__(self, x, y, font, initial_message, colour1, colour2, max_length, selected_colour):
        super().__init__(x, y, font)
        self.size_x = (typing.fonts[font][typing.size_x] + 5) * max_length
        self.hit_box = (self.x - self.size_x / 2 - 5, self.y - typing.fonts[self.font][typing.size_y] / 2 - 5, self.size_x + 10,
                        typing.fonts[self.font][typing.size_y] + 10)
        self.message = initial_message
        self.initial_message = initial_message
        self.outside_colour = colour1
        self.inside_colour = colour2
        self.selected_colour = selected_colour
        self.selected = False
        self.max_length = max_length

    def display_box(self):
        if self.moused:
            py.draw.rect(constants.screen, self.selected_colour, self.hit_box)
        else:
            py.draw.rect(constants.screen, self.outside_colour, self.hit_box)
        new_hit_box = (self.hit_box[0]+2, self.hit_box[1]+2, self.hit_box[2]-4, self.hit_box[3]-4)
        py.draw.rect(constants.screen, self.inside_colour, new_hit_box)

    def check_selected(self):
        if curser.check_new_click():
            if self.moused:
                SFX.play_sfx(self.sfx_when_pressed)
                self.selected = True
                globals.writing = True
            else:
                self.selected = False
                globals.writing = False

    def remove_last_character_from_message(self):
        new_message = ''
        for i in range(len(self.message)):
            if i < len(self.message)-1:
                new_message += self.message[i]
        return new_message

    def check_message(self):
        if self.selected and globals.session_tick % 50:
            character = ''
            keys = py.key.get_pressed()
            for i in range(len(keys)):
                try:
                    if keys[typing.typeable_characters_py_game[i]]:
                        character = typing.typeable_characters[i]
                except IndexError:
                    pass

            if keys[py.K_BACKSPACE]:
                self.message = self.remove_last_character_from_message()

            if keys[py.K_KP_ENTER]:
                self.selected = False
                globals.writing = False

            if character != '':
                if len(self.message) < self.max_length:
                    if self.message == self.initial_message:
                        self.message = character
                    else:
                        self.message += character

    def run(self):
        self.display_box()
        self.check_mouse(self.hit_box)
        self.check_selected()
        self.check_message()
        self.display(self.message)
        return self.message
