# -*- coding: utf-8 -*-

from configparser import ConfigParser
from os import listdir
from assrt import ASSRT

def is_video_file(name):
    video_types = ['.mkv', '.mp4', '.avi']
    for video_type in video_types:
        if video_type in name:
            return True
    return False

if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini')
    token_assrt = cfg.get('tokens', 'assrt')
    dir = cfg.get('dirs', 'dir')


    assrt = ASSRT(token_assrt)

    for file in listdir(dir):
        if is_video_file(file) is False:
            continue
        print("Search Subtitiles for [%s]." % file)
        assrt.search(file, dir)
        break
