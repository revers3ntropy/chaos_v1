import main_menu
import start_menu
import create_world
import Game
import tick


def check_all_programs():

    fails = 0
    list_of_fails = []

    # check functions #

    try:
        if main_menu.run() != 'main menu':
            fails += 1
            list_of_fails[0] = 'main_menu.run did not return main menu'
    except:
        fails += 1
        list_of_fails[0] = 'main_menu.run did not return main menu'

    try:
        if start_menu.run() != 'start menu':
            fails += 1
            list_of_fails[0] = 'start_menu.run did not return start menu'
    except:
        fails += 1
        list_of_fails[0] = 'start_menu.run did not return start menu'

    # record fails #

    if fails > 0:
        fail_report = '%s tests failed. Fails:' % fails
    else:
        fail_report = ''
    print(fail_report)
    for i in range(fails):
        print('Test:')
        print('   %s' % list_of_fails[i])
        print('')
