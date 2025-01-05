def rail_fence_cipher(message, n):
  ciphertext = ""
  rows = []
  for i in range(n):
    rows.append("")

  i = 0
  direction = 1
  for c in message:
    rows[i] += c
    i += direction
    if i == n or i == -1:
      direction = -direction
      i += direction

  for row in rows:
    ciphertext += row

  return ciphertext


def rail_fence_cipher_decrypt(ciphertext, n):

  plaintext = ""
  rows = []
  for i in range(n):
    rows.append("")

  i = 0
  direction = 1
  for c in ciphertext:
    rows[i] += c
    i += direction
    if i == n or i == -1:
      direction = -direction
      i += direction

  for i in range(n):
    plaintext += rows[i][::direction]
  return plaintext


def main():
  mode = input("Do you want to encrypt (e) or decrypt (d) a message? ")
  message = input("Enter the message: ")
  n = int(input("Enter the number of rails: "))

  if mode == "e":
    ciphertext = rail_fence_cipher(message, n)
    print("Ciphertext:", ciphertext)
  elif mode == "d":
    plaintext = rail_fence_cipher_decrypt(message, n)
    print("Plaintext:", plaintext)
  else:
    print("Invalid mode.")


if __name__ == "__main__":
  main()
