#!/bin/bash
# Takes an URL and displays all HTTP methods that the server will accept
curl -sI $1 | grep "Allow" | cut -c8-
