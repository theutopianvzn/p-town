import random

def gcd(a, b):
  """
  This function calculates the greatest common divisor (GCD) of two integers.

  Args:
      a: The first integer.
      b: The second integer.

  Returns:
      The GCD of a and b.
  """
  while b != 0:
    a, b = b, a % b
  return a

def is_prime(num):
  """
  This function checks if a number is prime.

  Args:
      num: The number to check.

  Returns:
      True if the number is prime, False otherwise.
  """
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def generate_keypair(p, q):
  """
  This function generates a public/private key pair using two prime numbers.

  Args:
      p: The first prime number.
      q: The second prime number.

  Returns:
      A tuple containing the public key (e, n) and the private key (d, n).
  """
  n = p * q
  phi_n = (p - 1) * (q - 1)
  e = random.randrange(1, phi_n)
  while gcd(e, phi_n) != 1:
    e = random.randrange(1, phi_n)
  d = pow(e, -1, phi_n)
  return ((e, n), (d, n))

def encrypt(plaintext, public_key):
  """
  This function encrypts a plaintext message using the public key.

  Args:
      plaintext: The message string to encrypt.
      public_key: The public key (e, n) for encryption.

  Returns:
      The encrypted ciphertext as a list of integers.
  """
  e, n = public_key
  ciphertext = []
  for char in plaintext:
    if char.isnumeric():
      char_num = ord(char) - ord('0')
    else:
      char_num = ord(char) - ord('a') + 26
    cipher_char = pow(char_num, e, n)
    ciphertext.append(cipher_char)
  return ciphertext

def decrypt(ciphertext, private_key):
  """
  This function decrypts an encrypted ciphertext using the private key.

  Args:
      ciphertext: The encrypted message as a list of integers.
      private_key: The private key (d, n) for decryption.

  Returns:
      The decrypted plaintext message as a string.
  """
  d, n = private_key
  plaintext = ""
  for cipher_char in ciphertext:
    char_num = pow(cipher_char, d, n)
    if char_num < 26:
      plaintext += chr(char_num + ord('a'))
    else:
      plaintext += chr(char_num - 26 + ord('0'))
  return plaintext

# Example usage
p = 11
q = 13
public_key, private_key = generate_keypair(p, q)
message = "This is a secret message!"
ciphertext = encrypt(message, public_key)
print("Original message:", message)
print("Encrypted message:", ciphertext)
decrypted_message = decrypt(ciphertext, private_key)
print("Decrypted message:", decrypted_message)
