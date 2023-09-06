#!/usr/bin/python3
"""
LockedClass => that prevents the user from dynamically
creating new instanceattributes, except if the
new instance attribute is called first_name
"""


class LockedClass(object):
    """
        implementation of LockedClass
    """
    def __setattr__(self, name: str, value) -> None:
        if name != "first_name":
            raise AttributeError(f"'LockedClass'\
 object has no attribute '{name}'")
        super().__setattr__(name, value)
