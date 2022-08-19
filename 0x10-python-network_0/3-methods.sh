#!/bin/bash
# displays the size of the body of the response
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
