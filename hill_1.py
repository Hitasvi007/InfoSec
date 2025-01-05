import numpy as np

def create_matrix_from(key):
    m=[[0] * 3 for i in range(3)]
    for i in range(3):
        for j in range(3):
            m[i][j] = ord(key[3*i+j]) % 65
    return m
def encrypt(P, K):
    C=[0,0,0]
    C[0] = (K[0][0]*P[0] + K[1][0]*P[1] + K[2][0]*P[2]) % 26
    C[1] = (K[0][1]*P[0] + K[1][1]*P[1] + K[2][1]*P[2]) % 26
    C[2] = (K[0][2]*P[0] + K[1][2]*P[1] + K[2][2]*P[2]) % 26
    return C

def Hill(message, K):
    cipher_text = []
    for i in range(0,len(message), 3):
        P=[0, 0, 0]
        for j in range(3):
            P[j] = ord(message[i+j]) % 65
        
        C = encrypt(P,K)
        
        for j in range(3):
            cipher_text.append(chr(C[j] + 65))
    
    return "".join(cipher_text)

def matrix_inverse_mod26(matrix):
    det = int(np.round(np.linalg.det(matrix)))
    inv_det = pow(det, -1, 26)
    adj = np.round(inv_det * np.linalg.inv(matrix) * det) % 26
    return adj.astype(int)


plain_text=input("Enter the message: ")
key =input("Enter the key: ")
K = create_matrix_from(key)
print(K)
cipher_text = Hill(plain_text, K)

print(cipher_text) 
ki=matrix_inverse_mod26(K)
dect=input("Enter the ciphered text: ")
dec=Hill(dect,ki)
print(dec)