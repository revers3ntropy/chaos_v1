timers = {}


def create_timer(timer, tick):
    timers[timer] = tick


def get_timer(timer, current_tick):
    try:
        return current_tick - timers[timer]
    except:
        print('Error: timer ', timer, ' does not exist')
        return 0


def reset_timer(timer):
    try:
        timers[timer] = 0
    except:
        print('Error: timer ', timer, ' does not exist')
