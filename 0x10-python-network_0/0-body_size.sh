#!/bin/bash
# Send a request to URL and display the size of the body of the response
curls -s $1 | wc-c
