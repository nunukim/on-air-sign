#! /usr/bin/python3

from urllib import request
import argparse
from os import path
from datetime import datetime


# load config.py file
import config

def trigger_ifttt(event):
    """
    POST to the IFTTT webhook URL
    """

    ifttt_url = f"https://maker.ifttt.com/trigger/{event}/with/key/{config.IFTTT_KEY}"
    return request.urlopen(ifttt_url, bytes())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-device")
    parser.add_argument("-event")
    parser.add_argument("-process")

    args = parser.parse_args()

    print(f"# {datetime.now().isoformat()} - {args}")

    if args.device == 'camera':
        if args.event == 'on':
            r = trigger_ifttt('on_air_sign_enabled')
        elif args.event == 'off':
            r = trigger_ifttt('on_air_sign_disabled')


