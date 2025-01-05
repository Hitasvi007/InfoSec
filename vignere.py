def vigenere_encrypt(plain_text, key):
    encrypted_text = []
    key_length = len(key)
    
    for i in range(len(plain_text)):
        key_char = key[i % key_length]
        shift = ord(key_char) - ord('A')
        
        if plain_text[i].isalpha():
            if plain_text[i].islower():
                encrypted_char = chr(((ord(plain_text[i]) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(plain_text[i]) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = plain_text[i]
        
        encrypted_text.append(encrypted_char)
    
    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)
    
    for i in range(len(encrypted_text)):
        key_char = key[i % key_length]
        shift = ord(key_char) - ord('A')
        
        if encrypted_text[i].isalpha():
            if encrypted_text[i].islower():
                decrypted_char = chr(((ord(encrypted_text[i]) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(encrypted_text[i]) - ord('A') - shift) % 26) + ord('A'))
        else:
            decrypted_char = encrypted_text[i]
        
        decrypted_text.append(decrypted_char)
    
    return ''.join(decrypted_text)

def main():
    while True:
        print("Vigenere Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            plain_text = input("Enter the plaintext: ")
            key = input("Enter the key: ")
            encrypted_text = vigenere_encrypt(plain_text, key)
            print("Encrypted:", encrypted_text)
        elif choice == '2':
            encrypted_text = input("Enter the encrypted text: ")
            key = input("Enter the key: ")
            decrypted_text = vigenere_decrypt(encrypted_text, key)
            print("Decrypted:", decrypted_text)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
