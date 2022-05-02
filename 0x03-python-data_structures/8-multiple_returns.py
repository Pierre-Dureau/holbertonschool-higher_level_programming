#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        c = sentence[0]
    else:
        c = None

    return (len(sentence), c)
