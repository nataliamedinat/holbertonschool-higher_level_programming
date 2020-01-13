#!/usr/bin/python3
import urllib.request
import urllib

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        response_read = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(response_read)))
        print("\t- content: {}".format(response_read))
        print("\t- utf8 content: {}".format(response_read.decode('utf-8')))
