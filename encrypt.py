import rsa
import stdio
import sys


# Entry point.
def main():

#Accept public-key n (int) and e (int) as command-line arguments.    
    n = int(sys.argv[1])
    e = int(sys.argv[2])

#Get the number of bits per character(call it width), ie, number of bits needed to encode n. (rsa.bitlength)
    Width = rsa.bitLength(n)

#Accept message to encrypt from standard input. READALL not READALLINT
    Message = stdio.readAll()


#For each character c in message:
    for c in Message:

#Use the built-in function ord() to turn c into an integer x.
        x = ord(c)

#Encrypt x~.
        y = rsa.encrypt(x, n, e)

#Write the encrypted value as a width-long binary string, returns decimal represent. as n express. as binary
        stdio.write(rsa.dec2bin(y, Width))

#Write a newline character.
    stdio.writeln()

if __name__ == '__main__':
    main()
