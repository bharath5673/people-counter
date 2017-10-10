#
# Maintainer:   jeffskinnerbox@yahoo.com / www.jeffskinnerbox.me
# Version:      0.3.0
#

import os
import cv2
import argparse


# default parameters when stating the algorithm
defaults = {
    "version": "0.3.0",                               # this algorithm version number
    "platform": os.uname(),                           # host name your running on
    "trace_on": False,                                # turn on trace messaging
    "show": True,                                     # turn on video display of real-time image
    "video_write_off": 'store_false',                 # turn on trace messaging
    "path": "/home/pi/Videos",                        # path to video storage
    "file_in": "People-Walking-Shot-From-Above.mp4",  # video to be processed
    "file_rec": "recording.mp4",                      # video before processing
    "file_recP": "recordingP.mp4",                    # video after processing
    "warmup_time": 1.5,                               # sec for camera warm up
    "device_no": 0,                                   # usb video device number
    "color_blue": (255, 0, 0),                        # opencv BGR color
    "resolution": [(640, 480)],                       # image resolution for processing
    "color_green": (0, 255, 0),                       # opencv BGR color
    "color_red": (0, 0, 255),                         # opencv BGR color
    "color_white": (255, 255, 255),                   # opencv BGR color
    "color_black": (0, 0, 0),                         # opencv BGR color
    "font": cv2.FONT_HERSHEY_SIMPLEX,                 # font used on frame
    "max_p_age": 5
}


def rez(s):
    """ This function is designed to support a specific data type used
    by the class ArgParser.  This function accepts two comma separated values,
    splits them, and returns them as a tuple.  There must be no white space
    before or after the comma. """
    try:
        x, y = map(int, s.split(','))
        return (x, y)
    except:
        raise argparse.ArgumentTypeError("parameter for -r, --resolution \
                must be expressed as x,y")


def ArgParser():
    """ This class establish a parsing mechanism for all
    types of command line argument, switches, and options."""

    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser(description=
                                 'This is the MassMutual Raspberry Pi \
                                 + OpenCV people counter')

    # store actions - tuple parameters
    ap.add_argument("-z", "--resolution",
                    help="resolution of the process imaged",
                    nargs=1,
                    type=rez,
                    default=defaults["resolution"])

    # store actions - single parameter
    ap.add_argument("-s", "--source",
                    help="include if the Raspberry Pi Camera should be used",
                    action='store',
                    required=False,
                    choices=['file', 'usbcamera', 'picamera'],
                    default='file')
    ap.add_argument("-d", "--video_device",
                    help="device number for input video",
                    action='store',
                    required=False,
                    type=int,
                    default=defaults["device_no"])
    ap.add_argument("-i", "--file_in",
                    help="path to video file that will be processed",
                    action='store',
                    required=False,
                    default=defaults["path"] + '/' + defaults["file_in"])
    ap.add_argument("-o", "--file_recP",
                    help="path to file where the processed video is stored",
                    action='store',
                    required=False,
                    default=defaults["path"] + '/' + defaults["file_recP"])
    ap.add_argument("-r", "--file_rec",
                    help="path to file where the unprocessed camera \
                    video will be recorded",
                    action='store',
                    required=False,
                    default=defaults["path"] + '/' + defaults["file_rec"])
    ap.add_argument("-w", "--warmup_time",
                    help="number of seconds to wait so camera can warm up",
                    action='store',
                    required=False,
                    type=int,
                    default=defaults["warmup_time"])

    # switches actions - store_true / store_false
    ap.add_argument("-p", "--video_write_off",
                    help="turn off the writing of video files \
                    (even when file name is provided)",
                    action='store_true',
                    default=defaults["video_write_off"])
    ap.add_argument("-x", "--show",
                    help="show the real-time video",
                    action='store_false',
                    default=defaults["show"])
    ap.add_argument("-y", "--trace_on",
                    help="turn on tracing",
                    action='store_true',
                    default=defaults["trace_on"])

    # version actions
    ap.add_argument("-v", "--version", action="version",
                    version="%(prog)s " + defaults["version"])

    return ap.parse_args()