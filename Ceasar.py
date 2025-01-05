def Encrypt(nor_tx):
    code_en=""
    for i in range(len(nor_tx)):
        ch = nor_tx[i]
        if ch == " ":
            code_en+=" "
        elif (ch.isupper()):
            code_en+= chr((ord(ch)+ 2-65)%26 + 65)
        else:
            code_en+= chr((ord(ch)+ 2-97)%26 +97)
    return code_en 
def Decrypt(nor_tx):
    code_de=""
    for i in range(len(nor_tx)):
        ch = nor_tx[i]
        if ch == " ":
            code_de+=" "
        elif (ch.isupper()):
            code_de+= chr((ord(ch)- 2-65)%26 + 65)
        else:
            code_de+= chr((ord(ch)- 2-97)%26 +97)
    return code_de 

tx=input("Enter the text: ")
z=input("Press 1 to encrypt or 2 to decrypt: ")
if z=='1':

    print("The encrypted word is: "+Encrypt(tx))
else:
    print("The decrypted word is: "+Decrypt(tx))