import os

def set_ffmpeg_path():
    # Set relative path to the ffmpeg binary
    current_dir = os.path.dirname(os.path.abspath(__file__))
    ffmpeg_path = os.path.join(current_dir, 'bin', 'ffmpeg')
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_path
    print(f"Success in setting FFmpeg path: {os.environ['IMAGEIO_FFMPEG_EXE']}")