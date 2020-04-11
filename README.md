# youtube-screenshot-ripper
Rips individual frames/screenshots at specified intervals in given Youtube videos.
Screenshots are saved as .PNG files in the same folder as the script.

This script utilizes ffmpeg, ffprobe, and youtube-dl. The full video is not downloaded as a result of using this script, only the parts necessary to obtain the requested frames are downloaded.

# Usage
Save screenshots of the video every 10 seconds. 
    $ python3 rip.py -s 10 https://www.youtube.com/watch?v=Rt-74t2VgeM

# Requirements
 * python3.6+ (and the following packages from pip)
   * ffmpeg-python
   * youtube-dl
 * ffmpeg binaries
