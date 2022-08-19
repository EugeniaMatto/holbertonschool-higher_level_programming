#!/bin/bash
# task 6
curl -sI "$1" | grep "HTTP/1.0" | cut -d " " -f2
