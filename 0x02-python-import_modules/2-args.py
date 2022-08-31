#!/usr/bin/python3
import sys


def main(*argv):
    i = 0
    len_s = len(sys.argv) - 1
    if len_s == 1:
        print("{:d} argument:".format(len_s))
    elif len_s == 0:
        print("{:d} arguments.".format(len_s))
    else:
        print("{:d} arguments:".format(len_s))
    for args in sys.argv:
        if (i != 0):
            print("{}: {}".format(i, args))
        i += 1


if __name__ == "__main__":
    main()
