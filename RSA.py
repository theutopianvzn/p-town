def is_prime(num):
  """
  Basic primality check (not cryptographically secure for large numbers)
  """
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

def generate_keypair(p, q):
  """
  Generates public (e, n) and private (d, n) key pairs
  """
  if not (is_prime(p) and is_prime(q)):
    raise ValueError('Both numbers must be prime')
  n = p * q
  phi = (p - 1) * (q - 1)
  e = 1
  while e < phi and gcd(e, phi) != 1:
    e += 1
  d = pow(e, -1, phi)  # Modular inverse using pow (not cryptographically secure)
  return ((e, n), (d, n))

def gcd(a, b):
  """
  Euclidean algorithm for greatest common divisor
  """
  while b != 0:
    a, b = b, a % b
  return a

def encrypt(pk, plaintext):
  """
  Encrypts plaintext using public key (e, n)
  """
  key, n = pk
  cipher = pow(plaintext, key, n)
  return cipher

def decrypt(sk, ciphertext):
  """
  Decrypts ciphertext using private key (d, n)
  """
  key, n = sk
  plain = pow(ciphertext, key, n)
  return plain

# Example usage (for illustration purposes only)
p = 11
q = 13
public, private = generate_keypair(p, q)
print("Public key:", public)
print("Private key:", private)

message = "This is a secret message"
encrypted_text = encrypt(public, ord(message[0]))  # Encrypt only the first character for simplicity
decrypted_text = decrypt(private, encrypted_text)
print("Original message:", chr(decrypted_text))
