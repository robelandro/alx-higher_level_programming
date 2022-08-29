#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = ()
    for j in (tuple_a, tuple_b):
        if len(j) == 0:
            j = (0, 0)
        elif len(j) == 1:
            j = (j[0], 0)
        if i == ():
            i = j
    return j[0] + i[0], j[1] + i[1]
