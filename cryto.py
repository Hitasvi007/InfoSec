from cryptography.fernet import Fernet
Key = Fernet.generate_key()  
txt = Fernet(Key)   
theToken = txt.encrypt(b"Hell")  
print("Encrypted Message: ", theToken)   
decryptMsg = txt.decrypt(theToken)    
print("\nDecrypted Message: ", decryptMsg)  