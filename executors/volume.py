from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_volume(percent):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(percent / 100.0, None)

def mute():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(1, None)
