from src.video_stream import VideoStream
from src.errors import BebopError
from pyparrot.Bebop import Bebop


def connect_bebop():
    bebop = Bebop()
    if bebop.connect(5):
        return bebop
    else:
        raise BebopError("Error connecting to drone")


def main():
    bebop = connect_bebop()
    video_stream = VideoStream(bebop)
    video_stream.start()
    bebop.smart_sleep(30)
    bebop.stop_video_stream()
    bebop.disconnect()


if __name__ == "__main__":
    main()
