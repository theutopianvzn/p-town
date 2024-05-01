def create_vigenere_table(alphabet):
  """
  This function creates a Vigenère table using the given alphabet.

  Args:
      alphabet: A string containing the alphabet characters to use.

  Returns:
      A list of lists representing the Vigenère table.
  """
  table = []
  for i in range(len(alphabet)):
    shifted_alphabet = alphabet[i:] + alphabet[:i]
    table.append(shifted_alphabet)
  return table

def encrypt(message, key, alphabet):
  """
  This function encrypts a message using the Vigenère cipher with the given key and alphabet.

  Args:
      message: The message string to encrypt.
      key: The secret key string for the cipher.
      alphabet: A string containing the alphabet characters to use.

  Returns:
      The encrypted message string.
  """
  vigenere_table = create_vigenere_table(alphabet)
  cipher = ''
  i = 0
  for char in message.lower():
    if char in alphabet:
      key_index = ord(key[i % len(key)]) - ord('a')
      original_index = alphabet.find(char)
      shifted_char = vigenere_table[key_index][original_index]
      cipher += shifted_char
      i += 1
    else:
      cipher += char
  return cipher

def decrypt(ciphertext, key, alphabet):
  """
  This function decrypts a ciphertext using the Vigenère cipher with the given key and alphabet.

  Args:
      ciphertext: The encrypted message string to decrypt.
      key: The secret key string for the cipher.
      alphabet: A string containing the alphabet characters to use.

  Returns:
      The decrypted message string.
  """
  vigenere_table = create_vigenere_table(alphabet)
  message = ''
  i = 0
  for char in ciphertext:
    if char in alphabet:
      key_index = ord(key[i % len(key)]) - ord('a')
      shifted_index = vigenere_table[key_index].index(char)
      original_char = alphabet[shifted_index]
      message += original_char
      i += 1
    else:
      message += char
  return message

# Example usage
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = "secret"
message = "This is a secret message!"
ciphertext = encrypt(message, key, alphabet)
print("Original message:", message)
print("Encrypted message:", ciphertext)
decrypted_message = decrypt(ciphertext, key, alphabet)
print("Decrypted message:", decrypted_message)
