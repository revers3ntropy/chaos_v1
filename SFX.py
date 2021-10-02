import settings_variables

file = 2
name = 3

sound_effects = {0: {file: 'SFX/SF_Button_Press_SFX.mp3',
                     name: 'button_001',
                     },
                 }


def play_sfx(name_of_sfx):
    return None
    if settings_variables.sfx:
        for i in range(len(sound_effects)):
            if sound_effects[i][name] == name_of_sfx:
                pass
