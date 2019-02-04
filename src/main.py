from src.errors import BebopError
from pyparrot.Bebop import Bebop
import threading
import cv2
import time
import vlc


def connect_bebop():
    bebop = Bebop()
    if bebop.connect(5):
        return bebop
    else:
        raise BebopError("Error connecting to drone")


def start_video_stream(bebop):
    bebop.set_video_framerate('24_FPS')
    bebop.set_video_resolutions('rec1080_stream480')
    success = bebop.start_video_stream()
    if not success:
        raise BebopError("Error starting video stream")


def play_video_stream():
    instance = vlc.Instance('--no-xlib --quiet')
    player = instance.media_player_new()
    media = instance.media_new("./bebop.sdp")
    player.set_media(media)
    player.play()


def run(bebop_vision, args):
    bebop = args[0]

    print("Vision successfully started!")

    bebop.safe_takeoff(5)
    bebop.fly_direct(roll=-20, pitch=0, yaw=0, vertical_movement=0, duration=2)
    bebop.fly_direct(roll=20, pitch=0, yaw=0, vertical_movement=0, duration=2)


    bebop.smart_sleep(15)

    if (bebop_vision.vision_running):
        print("Moving the camera using velocity")
        bebop.pan_tilt_camera_velocity(pan_velocity=0, tilt_velocity=-2, duration=4)
        bebop.smart_sleep(5)

        # land
        bebop.safe_land(5)

        print("Finishing demo and stopping vision")
        bebop_vision.close_video()

    # disconnect nicely so we don't need a reboot
    print("disconnecting")
    bebop.disconnect()


def main():
    bebop = connect_bebop()
    start_video_stream(bebop)
    play_video_stream()

    bebop.smart_sleep(5)
    bebop.stop_video_stream()
    bebop.disconnect()


if __name__ == "__main__":
    main()
