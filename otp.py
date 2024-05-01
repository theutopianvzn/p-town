import random

otp_storage = {}

def generate_otp():
    otp_value = random.randint(100000, 999999)  # Generate a 6-digit OTP
    return str(otp_value)

def send_otp(mobile_number, otp):
    # Simulating sending OTP to mobile number
    print(f"OTP sent to {mobile_number}: {otp}")
    otp_storage[mobile_number] = otp

def authenticate_user(mobile_number, entered_otp):
    stored_otp = otp_storage.get(mobile_number)
    if stored_otp and stored_otp == entered_otp:
        del otp_storage[mobile_number]  # Remove the OTP from storage
        return True
    return False

if __name__ == "__main__":
    mobile_number = "1234567890"
    otp = generate_otp()
    send_otp(mobile_number, otp)

    # Simulating user entering OTP
    entered_otp = "123456"
    if authenticate_user(mobile_number, entered_otp): # replace with otp 
        print("Authentication successful")
    else:
        print("Authentication failed")
