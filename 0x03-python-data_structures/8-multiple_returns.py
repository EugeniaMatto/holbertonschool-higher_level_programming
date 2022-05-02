#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None, 0
    return len(sentence), sentence[:1]
