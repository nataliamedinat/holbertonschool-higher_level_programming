#!/usr/bin/python3
def multiple_returns(sentence):
    return (len(sentence), sentence[0] if sentence is not "" else None)
