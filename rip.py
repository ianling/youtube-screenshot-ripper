import ffmpeg
import subprocess
from youtube_dl import YoutubeDL
from argparse import ArgumentParser


def get_duration(url):
    """
    Get duration of video in seconds (truncated/rounded down)
    """
    cmd = f'''ffprobe -i '{url}' -show_entries format=duration -v quiet -of csv="p=0"'''
    output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).decode()

    return int(output[:output.index('.')])


def get_video_info(url):
    """
    Get info about video from Youtube
    """
    opts = {'format': args.format}
    youtube_dl = YoutubeDL(opts)
    info = youtube_dl.extract_info(url, download=False)

    return info


arg_parser = ArgumentParser()
arg_parser.add_argument('urls', nargs='+')
arg_parser.add_argument('-f', '--format', default='248')  # 248 == 1080p, no audio
arg_parser.add_argument('-s', '--split-length', type=int, default=60)
args = arg_parser.parse_args()

videos = [get_video_info(url) for url in args.urls]
for video in videos:
    url = video['url']
    video_id = video['id']
    duration = get_duration(url)
    timestamps = range(duration, 0, -(args.split_length))
    for timestamp in timestamps:
        stream = ffmpeg.input(url, ss=timestamp).output(f'{video_id}_{timestamp}.png', vframes=1)
        stream.run_async()
