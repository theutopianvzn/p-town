import hashlib
import os
import base64

shared_secret = "my_secret_key"

def generate_challenge():
    return base64.b64encode(os.urandom(16)).decode()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def generate_authentication_token(username, hashed_password, challenge):
    return hashlib.sha256((username + hashed_password + challenge + shared_secret).encode()).hexdigest()

def authenticate(username, hashed_password, challenge, authentication_token):
    expected_token = generate_authentication_token(username, hashed_password, challenge)
    return expected_token == authentication_token

if __name__ == "__main__":
    username = "user1232"
    password = "password13"

    challenge = generate_challenge()
    hashed_password = hash_password(password)
    # authentication_token = generate_authentication_token(username, hashed_password, challenge) # Simulate correct token i.e True
    authentication_token = "incorrect" # Simulate incorrect token i.e False

    is_authenticated = authenticate(username, hashed_password, challenge, authentication_token)

    print("Authenticated:", is_authenticated)

# In this example, the server generates a random challenge and sends it to the client. The client then calculates an authentication token using the challenge, 
# the hashed password, and a shared secret key. The server verifies the authentication token by recalculating it and comparing it to the received token. 
# If they match, the client is authenticated.
