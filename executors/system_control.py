from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def _get_volume_interface():
    """
    Backward-compatible way to get IAudioEndpointVolume
    """
    devices = AudioUtilities.GetSpeakers()

    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )

    return cast(interface, POINTER(IAudioEndpointVolume))


def set_volume(value: int):
    try:
        value = int(value)
        value = max(0, min(100, value))

        volume = _get_volume_interface()
        volume.SetMasterVolumeLevelScalar(value / 100.0, None)

        print(f"🔊 Volume set to {value}%")

    except Exception as e:
        print("❌ Failed to set volume:", e)


def mute():
    try:
        volume = _get_volume_interface()
        volume.SetMute(1, None)
        print("🔇 System muted")

    except Exception as e:
        print("❌ Failed to mute:", e)
