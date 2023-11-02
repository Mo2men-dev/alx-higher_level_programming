#!/usr/bin/python3
import sys

if __name__ == "__main__":
    l = len(sys.argv) - 1
    argstr = "{:d} argument"
    
    if l == 1:
        argstr += ":"
    elif l == 0:
        argstr += "."
    else:
        argstr += "s:"

    print(argstr.format(l))

    i = 1
    for a in sys.argv[1:]:
        print("{:d}: {:s}".format(i, a))
        i += 1
