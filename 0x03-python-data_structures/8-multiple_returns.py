#!/usr/bin/python3
def multiple_returns(sentence):
    length, first = 0, None
    if sentence:
        length = len(sentence)
        first = sentence[0]

    return (length, first)
