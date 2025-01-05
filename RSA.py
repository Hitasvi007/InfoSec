import random
import math
import sys

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n) + 1), 2):
        if n % x == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicativeInverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi / e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi
    
def generatePrimeNumber():
    while True:
        num = random.randrange(100, 1000)
        if isPrime(num):
            return num
        
def generateKeys():
    p = generatePrimeNumber()
    q = generatePrimeNumber()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicativeInverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n) for char in ciphertext]
    return ''.join(plain)

def main():
    print ("RSA Encrypter/ Decrypter")
    print ("Generating your public/private keypairs now . . .")
    public, private = generateKeys()
    print ("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print ("Your encrypted message is: ")
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key ", private, " . . .")

import math

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n) + 1), 2):
        if n % x == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicativeInverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d % phi

def generatePrimeNumber():
    while True:
        num = random.randrange(100, 1000)
        if isPrime(num):
            return num

def generateKeys():
    p = generatePrimeNumber()
    q = generatePrimeNumber()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicativeInverse(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(pow(ord(char), key, n)) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)

def main():
    print("RSA Encrypter/ Decrypter")
    print("Generating your public/private keypairs now . . .")
    public, private = generateKeys()
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(public, message)
    print("Your encrypted message is: ")
    print(''.join(map(str, encrypted_msg)))
    print("Decrypting message with private key ", private, " . . .")
    print("Your message is: ")
    print(decrypt(private, encrypted_msg))

if __name__ == '__main__':
    main()
