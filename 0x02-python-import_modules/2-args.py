#!/usr/bin/python3
import sys

if __name__ == "__main__":
    exit()

length = len(sys.argv) - 1
argstr = "{:d} argument"

if length == 1:
    argstr += ":"
elif length == 0:
    argstr += "."
else:
    argstr += "s:"

print(argstr.format(length))

i = 1
for a in sys.argv[1:]:
    print("{:d}: {:s}".format(i, a))
    i += 1
