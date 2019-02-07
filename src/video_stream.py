import os


class VideoStream:
    def __init__(self, bebop, frame_rate='24_FPS', video_resolution='rec1080_stream480'):
        self.bebop = bebop
        self.frame_rate = frame_rate                # This can be '24_FPS', '25_FPS', or '30_FPS'
        self.video_resolution = video_resolution    # This can be 'rec1080_stream480', or 'rec720_stream720'

    def _start_drone_stream(self):
        self.bebop.set_video_framerate(self.frame_rate)
        self.bebop.set_video_resolutions(self.video_resolution)
        self.bebop.start_video_stream()

    @staticmethod
    def _start_local_receive():
        os.system("/Applications/VLC.app/Contents/MacOS/VLC bebop.sdp")

    def start(self):
        self._start_drone_stream()
        self._start_local_receive()
