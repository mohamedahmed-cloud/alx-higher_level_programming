#!/usr/bin/python3
"""
text_indentation - print a text with specific way.
"""


def text_indentation(text):
    """
        text_indentation: print passing text with specific way.
        args:
            text: text needed to printed
        return:
            new text to print.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    result = ""
    curr = ""
    check = set((".", "?", ":"))

    for i in text:
        curr += i
        if i in check:
            curr = curr.strip()
            result += curr
            result += "\n"
            curr = ""

    curr = curr.strip()
    result += curr
    result = result.strip()

    print(result)
