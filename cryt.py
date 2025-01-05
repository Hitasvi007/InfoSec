import cryptocode
import hashlib
plaint=input("Enter the plain text: ")
password=input("Enter the password: ")
encrypt=cryptocode.encrypt(plaint,password)
print("Encryted Data is: ",encrypt)
decrypt=cryptocode.decrypt(encrypt,password)
print('Decrytpted Data: ',decrypt)
plaintext=input("Enter the plaintext: ").encode()
encrytedata=hashlib.sha256(plaintext)
convert=encrytedata.hexdigest()
print(convert)
