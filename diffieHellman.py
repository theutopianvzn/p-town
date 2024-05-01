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

def generate_secret(p):
  """
  This function generates a random secret integer less than the prime p.

  Args:
      p: The prime number to use as a modulus.

  Returns:
      A random integer less than p.
  """
  import random
  return random.randint(1, p - 1)

def calculate_public_key(g, secret, p):
  """
  This function calculates the public key based on the generator, secret, and prime modulus.

  Args:
      g: The generator (primitive root) for the Diffie-Hellman algorithm.
      secret: The private secret integer.
      p: The prime number used as the modulus.

  Returns:
      The calculated public key.
  """
  return pow(g, secret, p)

def encrypt_message(message, key):
  """
  This function encrypts a message using a simple XOR encryption with the given key.

  Args:
      message: The message string to encrypt.
      key: The secret key (integer) for XOR encryption.

  Returns:
      The encrypted message as a list of integers.
  """
  ciphertext = []
  for char in message:
    cipher_char = ord(char) ^ key
    ciphertext.append(cipher_char)
  return ciphertext

def decrypt_message(ciphertext, key):
  """
  This function decrypts an encrypted message using XOR encryption with the given key.

  Args:
      ciphertext: The encrypted message as a list of integers.
      key: The secret key (integer) for XOR decryption.

  Returns:
      The decrypted message string.
  """
  message = ""
  for cipher_char in ciphertext:
    char = cipher_char ^ key
    message += chr(char)
  return message

def main():
  """
  The main function demonstrates the Diffie-Hellman key exchange and message encryption.
  """
  # Select a large prime number (replace with a stronger prime in practice)
  p = 23  # Weak for demonstration, use much larger primes in real applications

  # Choose a generator (primitive root) modulo p
  g = 5

  # Alice and Bob generate their own private secrets
  alice_secret = generate_secret(p)
  bob_secret = generate_secret(p)

  # Diffie-Hellman key exchange
  alice_public_key = calculate_public_key(g, alice_secret, p)
  bob_public_key = calculate_public_key(g, bob_secret, p)
  alice_shared_key = calculate_public_key(bob_public_key, alice_secret, p)
  bob_shared_key = calculate_public_key(alice_public_key, bob_secret, p)

  # Verify that Alice and Bob share the same secret key
  print("Alice's shared key:", alice_shared_key)
  print("Bob's shared key:", bob_shared_key)

  # Message encryption (simple XOR for demonstration)
  message = "This is a secret message!"
  print("Original message:", message)

  # Alice encrypts the message using the shared key
  encrypted_message = encrypt_message(message, alice_shared_key)
  print("Encrypted message:", encrypted_message)

  # Bob decrypts the message using the shared key
  decrypted_message = decrypt_message(encrypted_message, bob_shared_key)
  print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
  main()
