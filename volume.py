from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
import ctypes

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, 0, None)
volume_control = interface.QueryInterface(IAudioEndpointVolume)

def set_active_volume(volume):
    active_window_pid = get_active_window_pid()

    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
        process_id = session.Process.pid

        if process_id == active_window_pid.value:
            current_volume = volume_interface.GetMasterVolume()

            volume_level = clamp(current_volume + volume, 0, 1)

            volume_interface.SetMasterVolume(volume_level, None)
            break

def reset_global_volume(volume):
    current_level = volume_control.GetMasterVolumeLevelScalar()

    volume_level = clamp(current_level + volume, 0, 1)

    volume_control.SetMasterVolumeLevelScalar(volume_level, None)

def get_active_window_pid():
    foreground_window = ctypes.windll.user32.GetForegroundWindow()
    active_window_pid = ctypes.wintypes.DWORD()
    ctypes.windll.user32.GetWindowThreadProcessId(foreground_window, ctypes.byref(active_window_pid))
    return active_window_pid

def clamp(num, min, max):
    return min if num < min else max if num > max else num

