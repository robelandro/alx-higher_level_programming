#!/usr/bin/python3


class LockedClass:
    """[Class locked]"""
    __slots__ = ["first_name"]

    def __init__(self, first=""):
        self.first_name = first
