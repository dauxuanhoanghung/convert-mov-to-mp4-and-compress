from ffmpeg_setup import set_ffmpeg_path
set_ffmpeg_path()
from moviepy.editor import VideoFileClip
import os

def convert_and_compress(input_file, output_file, target_size_mb=10):
    # Load the video file
    video = VideoFileClip(input_file)
    
    # Get the current file size in MB
    current_size = os.path.getsize(input_file) / (1024 * 1024)
    
    # Calculate the compression ratio
    compression_ratio = target_size_mb / current_size
    
    # Calculate estimated current bitrate (in kilobits per second)
    duration = video.duration
    current_bitrate = (current_size * 8192) / duration
    
    # Calculate target bitrate
    target_bitrate = int(current_bitrate * compression_ratio)
    
    # Compress and save the video
    video.write_videofile(output_file, 
                          codec='libx264', 
                          audio_codec='aac', 
                          bitrate=f'{target_bitrate}k')
    
    # Close the video to release resources
    video.close()
    
    print(f"Original size: {current_size:.2f} MB")
    print(f"Compressed size: {os.path.getsize(output_file) / (1024 * 1024):.2f} MB")

# Example usage
input_file = 'input.mov'  # or 'input.mp4'
output_file = 'output.mp4'
target_size_mb = 10  # Target size in MB
convert_and_compress(input_file, output_file, target_size_mb)