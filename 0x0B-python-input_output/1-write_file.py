#!/usr/bin/python3
"""
write_file: function that writes a string to a text
            file (UTF8) and returns the number of
            characters written
"""


def write_file(filename="", text=""):
    """
    args:
        filename: file to write text from it
        text: text to be writen in the filename
    """

    with open(filename, "w", encoding="utf-8") as file:
        text_written_number = file.write(text)
        return text_written_number
