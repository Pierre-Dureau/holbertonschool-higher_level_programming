#!/bin/bash
# display size of a HTTP response
curl -s "$1" | wc -c
