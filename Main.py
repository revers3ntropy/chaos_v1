import main_menu
import pygame as py
import globals
import start_menu
import settings
import pause_game
import create_world
import utilities
import settings_variables
import Game
import checker
import close_window
import constants
import typing
import music
import time
import renderer
import curser


def main ():
    checker.check_all_programs()

    py.display.set_caption('Chaos')

    go = True
    while go:
        try:

            start_time = time.time()

            globals.session_tick += 1

            keys = py.key.get_pressed()

            curser.update_mouse_clicked()
            utilities.update_esc(keys)

            state = globals.state

            if state == 'main menu':
                globals.state = main_menu.run()
            elif state == 'start menu':
                globals.state = start_menu.run()
            elif state == 'settings':
                globals.state = settings.run()
            elif state == 'create world':
                globals.state = create_world.run()
            elif state == 'pause game':
                globals.state = pause_game.run(keys)
            elif state == 'game':
                globals.state = Game.run(keys)
            else:
                utilities.throw_error('State is not known: ' + str(state))

            if settings_variables.music:
                music.play_music()

            renderer.curser()

            typing.write(typing.chaos_14x16, str(globals.FPS), constants.screen_x-50, 20)

            py.display.set_caption('Chaos')
            py.display.update()
            constants.clock.tick(constants.run_FPS)

            constants.screen.fill(constants.background_colour)

            go = close_window.check_for_close(keys)

            globals.FPS = str(round(1.0 / (time.time() - start_time)))

        except:
            utilities.throw_error('System error')

    py.quit()

if __name__ == '__main__':
    main()
