#!/usr/bin/python3
"""Write a file module."""


def write_file(filename="", text=""):
    """
    Write a file with the given text.

    Args:
        filename: The name of the file to write to.
        text: The text to write to the file.

        Returns:
            The number of characters written."""
    with open(filename, "w") as f:
        return f.write(text)
