import itertools
import string

# Function to generate all possible passwords of a given length
def generate_passwords(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return (''.join(candidate) for candidate in itertools.product(characters, repeat=length))

# Function to crack the password
def brute_force_crack(password):
    max_length = 8  # Maximum length of the password to consider
    for length in range(1, max_length + 1):
        for guess in generate_passwords(length):
            if guess == password:
                return guess
    return None  # Password not found

# Example usage
if _name_ == "_main_":
    target_password = "secret123"  # Change this to the password you want to crack
    cracked_password = brute_force_crack(target_password)
    if cracked_password:
        print("Password cracked:", cracked_password)
    else:
        print("Password not cracked. Try a longer password or different character set.")
