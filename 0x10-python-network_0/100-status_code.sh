#!/bin/bash
# Get the status code of the request
curl -LI "$1" -o /dev/null -w '%{http_code}\n' -s
