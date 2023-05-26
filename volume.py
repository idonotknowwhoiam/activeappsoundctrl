from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
import ctypes
import enum

class Event(enum.Enum):
    up = 2
    down = 1

VOLUME_STEP = 0.02

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
volume_control = interface.QueryInterface(IAudioEndpointVolume)

def set_volume(event):
    foreground_window = ctypes.windll.user32.GetForegroundWindow()
    active_window_pid = ctypes.wintypes.DWORD()
    ctypes.windll.user32.GetWindowThreadProcessId(foreground_window, ctypes.byref(active_window_pid))

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
        process_id = session.Process.pid

        if process_id == active_window_pid.value:
            volume_level = volume_interface.GetMasterVolume()

            if event == Event.up:
                volume_level = clamp(volume_level + VOLUME_STEP, 0, 1)
            elif event == Event.down:
                volume_level = clamp(volume_level - VOLUME_STEP, 0, 1)

            volume_interface.SetMasterVolume(volume_level, None)
            break

def reset_global_volume(event):
    volume_level = volume_control.GetMasterVolumeLevelScalar()

    if event == Event.up:
        volume_level = clamp(volume_level - VOLUME_STEP, 0, 1)
    if event == Event.down:
        volume_level = clamp(volume_level + VOLUME_STEP, 0, 1)

    volume_control.SetMasterVolumeLevelScalar(volume_level, None)

def clamp(num, min, max):
    return min if num < min else max if num > max else num

