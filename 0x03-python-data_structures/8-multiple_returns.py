#!/usr/bin/python3
def multiple_returns(sentence):
    sentence_len = len(sentence)
    if (sentence_len != 0):
        return (sentence_len, sentence[0])
    else:
        return (0, None)
