#!/bin/bash
# sends a JSON POST request
curl -sX POST "$1" -H "Content-Type: application/json" --data-binary @"$2"
