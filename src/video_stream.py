import os


class VideoStream:
    def __init__(self, bebop, frame_rate='24_FPS', video_resolution='rec1080_stream480'):
        self.bebop = bebop
        self.frame_rate = frame_rate
        self.video_resolution = video_resolution

    def _start_drone_stream(self):
        self.bebop.set_video_framerate('24_FPS')
        self.bebop.set_video_resolutions('rec1080_stream480')
        self.bebop.start_video_stream()

    @staticmethod
    def _start_local_receive():
        os.system("/Applications/VLC.app/Contents/MacOS/VLC bebop.sdp")

    def start(self):
        self._start_drone_stream()
        self._start_local_receive()
