#!/usr/bin/env python
"""
docstring

"""
from sys import argv
def main(argv):
    a = int(argv[1])
    b = int( argv[2] )
    if a < b:
        (b,a) = (a,b)
    mod    = a % b
    while mod != 0:
       a = b
       b = mod
       mod = a % b
    print "gcd: %d" % b


if __name__ == "__main__":
    main(argv)
