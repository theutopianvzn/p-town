def create_key(alphabet):
  """
  This function generates a random key for encryption/decryption.

  Args:
      alphabet: A string containing the alphabet characters to use.

  Returns:
      A string representing the randomly shuffled key.
  """
  key = list(alphabet)
  import random
  random.shuffle(key)
  return ''.join(key)

def encrypt(message, key, alphabet):
  """
  This function encrypts a message using the given key and alphabet.

  Args:
      message: The message string to encrypt.
      key: The secret key string for substitution.
      alphabet: A string containing the alphabet characters to use.

  Returns:
      The encrypted message string.
  """
  cipher = ''
  for char in message.lower():
    if char in alphabet:
      index = alphabet.find(char)
      cipher += key[index]
    else:
      cipher += char
  return cipher

def decrypt(ciphertext, key, alphabet):
  """
  This function decrypts a ciphertext using the given key and alphabet.

  Args:
      ciphertext: The encrypted message string to decrypt.
      key: The secret key string for substitution.
      alphabet: A string containing the alphabet characters to use.

  Returns:
      The decrypted message string.
  """
  message = ''
  for char in ciphertext:
    if char in key:
      index = key.find(char)
      message += alphabet[index]
    else:
      message += char
  return message

# Example usage
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = create_key(alphabet)
message = "This is a secret message!"
ciphertext = encrypt(message, key, alphabet)
print("Original message:", message)
print("Encrypted message:", ciphertext)
decrypted_message = decrypt(ciphertext, key, alphabet)
print("Decrypted message:", decrypted_message)
