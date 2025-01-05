keyMatrix = [[0] * 3 for i in range(3)]
messageVector = [[0] for i in range(3)]
cipherMatrix = [[0] for i in range(3)]
plainMatrix = [[0] for i in range(3)]
inverseKeyMatrix=[[0]*3 for i in range(3)]

def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def decrypt(cipherMatrix):
    
    determinant = (keyMatrix[0][0] * (keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1])) - \
                  (keyMatrix[0][1] * (keyMatrix[1][0] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][0])) + \
                  (keyMatrix[0][2] * (keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0]))

    inverseDet = 0
    for i in range(26):
        if (determinant * i) % 26 == 1: 
            inverseDet = i
            break

    inverseKeyMatrix[0][0] = ((keyMatrix[1][1] * keyMatrix[2][2] - keyMatrix[1][2] * keyMatrix[2][1]) * inverseDet) % 26
    inverseKeyMatrix[0][1] = ((-keyMatrix[0][1] * keyMatrix[2][2] + keyMatrix[0][2] * keyMatrix[2][1]) * inverseDet) % 26
    inverseKeyMatrix[0][2] = ((keyMatrix[0][1] * keyMatrix[1][2] - keyMatrix[0][2] * keyMatrix[1][1]) * inverseDet) % 26
    inverseKeyMatrix[1][0] = ((-keyMatrix[1][0] * keyMatrix[2][2] + keyMatrix[1][2] * keyMatrix[2][0]) * inverseDet) % 26
    inverseKeyMatrix[1][1] = ((keyMatrix[0][0] * keyMatrix[2][2] - keyMatrix[0][2] * keyMatrix[2][0]) * inverseDet) % 26
    inverseKeyMatrix[1][2] = ((-keyMatrix[0][0] * keyMatrix[1][2] + keyMatrix[0][2] * keyMatrix[1][0]) * inverseDet) % 26
    inverseKeyMatrix[2][0] = ((keyMatrix[1][0] * keyMatrix[2][1] - keyMatrix[1][1] * keyMatrix[2][0]) * inverseDet) % 26
    inverseKeyMatrix[2][1] = ((-keyMatrix[0][0] * keyMatrix[2][1] + keyMatrix[0][1] * keyMatrix[2][0]) * inverseDet) % 26
    inverseKeyMatrix[2][2] = ((keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0]) * inverseDet) % 26
    for i in range(3):
        for j in range(1):
            plainMatrix[i][j] = 0
            for x in range(3):
                plainMatrix[i][j] += (inverseKeyMatrix[i][x] * cipherMatrix[x][j])
            plainMatrix[i][j] = plainMatrix[i][j] % 26

def HillCipher(message, key):
    getKeyMatrix(key)
    
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    encrypt(messageVector)
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    print("Ciphertext:", "".join(CipherText))

def hildi(message,key):
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65
    decrypt(cipherMatrix)
    DecryptedText = []
    for i in range(3):
        DecryptedText.append(chr(plainMatrix[i][0] + 65))

    print("Decrypted Text:", "".join(DecryptedText))

def main():
    message=input("Enter the text: ")
    key=input("Enter the key: ")
    x=int(input("Press 1 to encrypt or 2 to decrypt: "))
    if x==1:
        HillCipher(message,key)
    else:
        hildi(message,key)


if __name__ == "__main__":
    main()
