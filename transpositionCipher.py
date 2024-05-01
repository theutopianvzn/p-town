def encrypt(message, key):
  """
  This function encrypts a message using a transposition cipher with the given key.

  Args:
      message: The message string to encrypt.
      key: The integer key representing the number of columns in the transposition grid.

  Returns:
      The encrypted message string.
  """
  ciphertext = ""
  # Create empty list of strings for columns
  columns = [""] * key 
  i = 0
  for char in message:
    columns[i % key] += char
    i += 1

  # Combine columns into encrypted message
  ciphertext = "".join(columns)
  return ciphertext

def decrypt(ciphertext, key):
  """
  This function decrypts a ciphertext using a transposition cipher with the given key.

  Args:
      ciphertext: The encrypted message string to decrypt.
      key: The integer key representing the number of columns in the transposition grid.

  Returns:
      The decrypted message string.
  """
  message = ""
  # Get number of rows based on ciphertext length and key
  rows = int(len(ciphertext) / key) 
  # Create empty list for storing characters row-wise
  decrypted_rows = [""] * rows
  for i in range(key):
    for j in range(rows):
      index = i + j * key
      if index < len(ciphertext):
        decrypted_rows[j] += ciphertext[index]

  # Combine rows into decrypted message
  message = "".join(decrypted_rows)
  return message

# Example usage
message = "This is a secret message!"
key = 4
ciphertext = encrypt(message, key)
print("Original message:", message)
print("Encrypted message:", ciphertext)
decrypted_message = decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)
