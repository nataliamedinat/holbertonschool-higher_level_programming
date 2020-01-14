#!/usr/bin/python3
import urllib.request
import urllib
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        read = response.read()
    info = response.info()
    print(info['X-Request-Id'])
