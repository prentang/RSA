import rsa
import stdio
import sys


# Entry point.
def main():
    #Accept command line arugments
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    #Get keys as a tuple (public/private) using rsa.keygen (API)
    key = rsa.keygen(lo,hi)

    #Write the three values in the tuple, separated by a space inbetween each one.
    stdio.writef("%d %d %d\n", key[0], key[1], key[2])


if __name__ == '__main__':
    main()
