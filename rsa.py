import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
# #Get a list of primes from the interval [lo, hi).
    primes_list = _primes(lo, hi)

# – Sample two distinct random primes p and q from that list. *USING _SAMPLE*
    p, q = _sample(primes_list, 2)

# – Set n and m to pq and (p − 1)(q − 1), respectively.
    n = p * q
    m = (p - 1) * (q - 1)

# – Get a list primes from the interval [2, m).
    primes_list = _primes(2, m)
    
# – Choose a random prime e from the list such that e does not divide m, until it is not divisible .
    # IGNORE (SELF COMMENTS): after while loop, e is set correctly I need random prime e but it cannot divide m
    
    #initialize e 
    e = _choice(primes_list)
    
    while m % e == 0:
        e = _choice(primes_list)
        
    #after while loop, e is set correctly 

# – Find a d ∈ [1, m) such that ed mod m = 1.
    #IGNORE (SELF COMMENTS): if (e * d) % m = 1 and  while d < m: --> d += 1 
    
    #initialize d
    d = 1 
    while d < m:
        if e * d % m == 1:
            break
        d += 1

# – Return the tuple1 --> (n, e, d)
    return (n, e, d)

# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    Ex = (x ** e) % n
    return Ex
    


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    Dy = (y ** d) % n
    return Dy
    


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    #initialize list
    primes = []
   
    #way to do prime numbers:
    for num in range(lo, hi):
        #numbers greater than 2, continue, set i to 2 (beginning of primes)
        if num < 2:
            continue   
        i = 2
        
        #runs through checks for prime numbers, append to list if conditions are met 
        while i <= num / i:
            if num % i == 0:
                break
            i += 1 
        if i > num / i:
            primes += [num]
    return primes
    

# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    #Create a list b that is a copy (not an alias) of a.
    b = a[:]

    #intialize list
    random_sample = []

    #create random numbers for the segment k
    for i in range(k):
        
        #we are going to replace a part of the list with a shuffle of the of the orignal list up to point k
        random = stdrandom.uniformInt(i, len(a))
        
        #swap the points (orignal part of the list with shuffled)
        temp = b[i]
        b[i] = b[random]
        b[random] = temp
        
        #append 
        random_sample += [b[i]]

    return random_sample


        
    #(IGNORE, COMMMENTS ARE THOUGHTS OF DOING IT OTHER WAYS)
    #– Shuffle the first k elements of b
    # so we need a range from 0 -> k (so index from 0 to k) we need the length
    #b needs to get shuffled, so can we go from each index of the list given, randomize, output?
    #temp, slicing? 
    ## for i in range(k):
    #b_first_k = b[:k]
    #stdrandom.shuffle(b_first_k)
    #now the a_first_k is shuffled
    #want to place back into a
    # a[0] = 10
    #b[:k] = b_first_k
    #return b
    # [1,2,3,4] idx: 0,1,2,3
    # k = 4

# Returns a random item from the list a.
def _choice(a):
    ran = stdrandom.uniformInt(0, len(a))
    return a[ran]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))
    # print(decrypt(encrypt(80, 5917, 5669), 5917, 1349))


if __name__ == '__main__':
    _main()




