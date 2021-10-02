import globals
import random
import time

tracks = 2

file = 2
name = 3
duration = 4

music = {1: {file: '',
             name: '',
             duration: 0
             }
         }


def play_music():
    return None
    if globals.playing is False:
        globals.track = random.randint(1, tracks*50000)
        if globals.track <= tracks:
            globals.playing = True
            globals.start_time = time.time()
            playsound(music[globals.track][file])
    else:
        if time.time() - globals.start_time > music[globals.track][duration] + 10:
            globals.playing = False
