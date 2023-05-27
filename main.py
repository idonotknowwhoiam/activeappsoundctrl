import keyboard
from volume import reset_global_volume, set_active_volume

VOLUME_UP_KEYCODE = -175
VOLUME_DOWN_KEYCODE = -174
DEFAULT_VOLUME_STEP = 0.02

# your hotkeys
volume_up_key = -175
volume_down_key = -174
modifier_key = "ctrl"

volume_step = DEFAULT_VOLUME_STEP

while True:  
    keyboard.read_event()
    
    if keyboard.is_pressed(volume_down_key) and keyboard.is_pressed(modifier_key):
        if volume_down_key == VOLUME_DOWN_KEYCODE:
            reset_global_volume(DEFAULT_VOLUME_STEP)

        set_active_volume(-volume_step)
    if keyboard.is_pressed(volume_up_key) and keyboard.is_pressed(modifier_key):
        if volume_up_key == VOLUME_UP_KEYCODE:
            reset_global_volume(-DEFAULT_VOLUME_STEP) 

        set_active_volume(volume_step)

