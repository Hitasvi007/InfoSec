def encrypt_columnar_cipher(plaintext, key):
    # Remove spaces and convert the key to uppercase for consistency
    key = ''.join(sorted(set(key.upper()), key=key.upper().index))
    plaintext = plaintext.replace(" ", "").upper()

    # Calculate the number of rows needed in the grid
    num_rows = len(plaintext) // len(key)
    if len(plaintext) % len(key) != 0:
        num_rows += 1

    # Create the grid
    grid = [[' ' for _ in range(len(key))] for _ in range(num_rows)]

    # Fill in the grid with the plaintext
    index = 0
    for col in range(len(key)):
        for row in range(num_rows):
            if index < len(plaintext):
                grid[row][col] = plaintext[index]
                index += 1

    # Read out the columns to get the ciphertext
    ciphertext = ''
    for col in range(len(key)):
        for row in range(num_rows):
            ciphertext += grid[row][col]

    return ciphertext

def decrypt_columnar_cipher(ciphertext, key):
    # Remove spaces and convert the key to uppercase for consistency
    key = ''.join(sorted(set(key.upper()), key=key.upper().index))
    ciphertext = ciphertext.replace(" ", "").upper()

    # Calculate the number of rows needed in the grid
    num_rows = len(ciphertext) // len(key)
    if len(ciphertext) % len(key) != 0:
        num_rows += 1

    # Create the grid
    grid = [[' ' for _ in range(len(key))] for _ in range(num_rows)]

    # Calculate the number of characters in the last column
    last_col_chars = len(ciphertext) % len(key)

    # Fill in the grid with the ciphertext
    index = 0
    for col in range(len(key)):
        for row in range(num_rows):
            if col < last_col_chars and row == num_rows - 1:
                continue
            grid[row][col] = ciphertext[index]
            index += 1

    # Read out the rows to get the plaintext
    plaintext = ''
    for row in range(num_rows):
        for col in range(len(key)):
            plaintext += grid[row][col]

    return plaintext

# Example usage:
plaintext = "HELLO WORLD"
key = "KEY"

# Encryption
encrypted_text = encrypt_columnar_cipher(plaintext, key)
print("Encrypted:", encrypted_text)

# Decryption
decrypted_text = decrypt_columnar_cipher(encrypted_text, key)
print("Decrypted:", decrypted_text)
