#!/usr/bin/python3
import hidden_4


def main():
    dir_s = dir(hidden_4)
    for i in range(len(dir_s)):
        if (dir_s[i][0] != '_'):
            print("{}".format(dir_s[i]))


if __name__ == "__main__":
    main()
