#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    try:
        string = sys.argv[1]
    except IndexError:
        print("Usage: %s <string_convert>" % sys.argv[0])
        sys.exit()

    result = []
    ascii_strings = [ord(c) for c in string]


    for i in range(0,len(ascii_strings),4):
        result.append(ascii_strings[i:i+4])

    for data  in reversed(result):
        print('0x',end='')
        for b in reversed(data):
            print("{0:02x}".format(b),end='')
        print("",end='')
        print()