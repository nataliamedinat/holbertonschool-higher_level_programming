#!/usr/bin/python3
import urllib.request
import urllib
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            read = response.read()
            print(read.decode('utf-8'))
    except urllib.error.HTTPERROR as error:
        print("Error code: {}".format(error.code))
