import hmac
import hashlib
import time
import struct
import base64

def generate_totp(userid, time_step=30, key_suffix="examplesufix"):
    # Step 1: Prepare the shared secret by concatenating userid and key_suffix
    shared_secret = userid + key_suffix
    
    # Step 2: Get the current Unix timestamp
    timestamp = int(time.time())
    
    # Step 3: Divide the timestamp by the time step (30 seconds)
    time_counter = timestamp // time_step
    
    # Step 4: Create the HMAC-SHA-512 hash using the shared secret and time_counter
    key = shared_secret.encode('utf-8')  # Shared secret in bytes
    message = struct.pack('>Q', time_counter)  # Convert time_counter to 8 bytes (big-endian)
    hmac_sha512 = hmac.new(key, message, hashlib.sha512).digest()
    
    # Step 5: Extract the OTP from the HMAC hash
    # We need to get a 10-digit OTP (adjusted to 10 digits by truncation)
    offset = hmac_sha512[-1] & 0x0F  # The offset is the last 4 bits of the hash
    otp = struct.unpack(">I", hmac_sha512[offset:offset+4])[0] & 0x7FFFFFFF  # Get 4 bytes and truncate
    otp = otp % 10000000000  # Ensure it's a 10-digit OTP
    
    return f"{otp:010d}"  # Format to 10 digits

def generate_authorization_header(userid):
    # Generate TOTP for the userid
    totp = generate_totp(userid)
    
    # Create the Basic Auth credentials string (userid:totp_password)
    credentials = f"{userid}:{totp}"
    
    # Base64 encode the credentials
    base64_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
    
    # Return the final Authorization header value
    return f"Basic {base64_credentials}"

# Example usage
userid = "example.com"
authorization_header = generate_authorization_header(userid)
print("Authorization Header:", authorization_header)
