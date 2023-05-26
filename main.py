import keyboard
from volume import reset_global_volume, set_volume, Event

VOLUME_DOWN_KEY = -174
VOLUME_UP_KEY = -175
WIN_KEY = 91


while True:  
    keyboard.read_event()
    
    event = None

    if keyboard.is_pressed(VOLUME_DOWN_KEY) and keyboard.is_pressed(WIN_KEY):
        event = Event.down
        
        reset_global_volume(event)
        set_volume(event)
    if keyboard.is_pressed(VOLUME_UP_KEY) and keyboard.is_pressed(WIN_KEY):
        event = Event.up
        reset_global_volume(event)
        set_volume(event)

