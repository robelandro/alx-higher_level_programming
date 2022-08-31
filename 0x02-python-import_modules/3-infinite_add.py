#!/usr/bin/python3
import sys


def main(*argv):
    len_s = len(sys.argv)
    sum = 0
    if len_s > 1:
        for args in sys.argv:
            if args != sys.argv[0]:
                sum = sum + int(args)
    print(sum)


if __name__ == "__main__":
    main()
