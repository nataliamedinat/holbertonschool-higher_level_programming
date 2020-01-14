#!/usr/bin/python3

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = requests.post(url, data={"email": email})
    print(values.text)
