#!/usr/bin/python3

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    url = requests.get(url)
    url_retri = url.headers
    print(url_retri.get('X-Request-Id'))
