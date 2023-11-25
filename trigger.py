#! /usr/local/bin/python3

from urllib import request
import argparse
from os import path
from datetime import datetime

from magichue import LocalLight

# load config.py file
import config

def trigger_local(on:bool):
    light = LocalLight(config.MAGIC_HUE_LOCAL_IP)
    light.on = on

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-device")
    parser.add_argument("-event")
    parser.add_argument("-process")
    parser.add_argument("-activeCount", type=int)
    args = parser.parse_args()

    print(f"# {datetime.now().isoformat()} - {args}")
    trigger_local(args.activeCount > 0)

