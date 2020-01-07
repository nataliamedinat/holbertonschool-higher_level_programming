#!/bin/bash
# Takes an URL and displays all HTTP methods that the server will accept
curl -s -X OPTIONS *
