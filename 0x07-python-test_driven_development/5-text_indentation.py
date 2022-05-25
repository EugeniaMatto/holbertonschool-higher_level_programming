#!/usr/bin/python3
"""
Module to task 5
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    i = 0
    buf = ""
    while i < len(text):
        buf += text[i]
        if (text[i] == '.' or text[i] == '?' or text[i] == ':' or
                text[i] == '\n' or (i == (len(text) - 1))):
            if len(buf) > 1:
                while (buf[0] == ' '):
                    buf = buf[1:]
            if (len(buf) > 1 and text[i] != '.' and
                    text[i] != '?' and text[i] != ':'):
                buf = buf[:-1]
                while (buf[-1] == ' '):
                    buf = buf[:-1]
                if text[i] != ' ':
                    buf += text[i]
            if not(len(buf) == 1 and buf[0] == ' '):
                print(buf, end="")
            if ((text[i] == '.' or text[i] == '?' or text[i] == ':') or
                    len(buf) == 1 and buf[0] == ' '):
                if not(len(buf) == 1 and buf[0] == ' '):
                    print()
                print()
            buf = ""
        i += 1
