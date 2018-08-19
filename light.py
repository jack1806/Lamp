#!/usr/bin/python3

import argparse
import requests

LED_ON = "http://192.168.4.1/led/0"
LED_OFF = "http://192.168.4.1/led/1"


def req(url):
    try:
        request = requests.get(url)
        response = request.text
        if response:
            return 0
        else:
            print("Something went wrong!")
    except requests.ConnectionError or requests.ConnectTimeout:
        print("Something went wrong!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="It works!")

    parser.add_argument("mode", type=str, metavar="on/off")
    args = parser.parse_args()

    print(args.mode)

    # parser.add_argument("-on", help="Turn on", action="store_true", default=False)
    # parser.add_argument("-off", help="Turn off", action="store_true", default=False)
    # args = parser.parse_args()
    # if args.on:
    #     req(LED_ON)
    # elif args.off:
    #     req(LED_OFF)
    # else:
    #     parser.print_help()
