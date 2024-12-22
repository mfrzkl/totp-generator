# TOTP-Based Authorization Header Generator

This Python script generates a TOTP (Time-based One-Time Password) and creates a Basic Authorization header. It is designed to provide enhanced security by using dynamic TOTP values that change over time.

## How It Works

### 1. **Generate TOTP**
The `generate_totp` function creates a TOTP using the following steps:
- **Shared Secret:** Combines the `userid` with a fixed `key_suffix` to create a unique shared secret.
- **Timestamp:** Retrieves the current Unix timestamp and divides it by a configurable time step (default is 30 seconds).
- **HMAC-SHA-512 Hash:** Computes a hash using the shared secret and a counter derived from the timestamp.
- **OTP Extraction:** Extracts a 10-digit OTP from the hash using truncation.

### 2. **Generate Authorization Header**
The `generate_authorization_header` function:
- Calls `generate_totp` to generate a dynamic password based on the `userid`.
- Concatenates the `userid` and TOTP password to create credentials in the format `userid:totp_password`.
- Base64-encodes the credentials and formats them into a standard Basic Authorization header.

### Example Output
For a `userid` of `example.com`, the script outputs an authorization header like:

```
Authorization Header: Basic ZXhhbXBsZS5jb206MTIzNDU2Nzg5MA==
```

---

## Key Components

### **`userid`**
This is a unique identifier for the user or application using the system. It is used as part of the shared secret to ensure that each user generates a unique TOTP.

- Example: `example.com`, `user123`, or any unique identifier in your system.

### **`key_suffix`**
This is a static string appended to the `userid` to form the shared secret. The purpose of the suffix is to:
1. Add an extra layer of security to the shared secret.
2. Allow a consistent yet unique TOTP generation process for all users.

- Default Value: `"examplesuffix"`
- Customize this value to suit your application's needs, ensuring it remains consistent across implementations.

---

## Security Considerations
- **Shared Secret:** Ensure that the `userid` and `key_suffix` combination is kept confidential.
- **Time Synchronization:** Since the TOTP relies on timestamps, ensure the system time is synchronized.
- **10-Digit OTP:** The OTP is truncated to 10 digits for additional security. Modify this as needed for your application.

---

## Usage

Here’s how to use the script:

1. Replace `userid` with the unique identifier for your user/application.
2. Optionally, modify the `key_suffix` if needed for your implementation.
3. Call `generate_authorization_header(userid)` to generate the Authorization header.
4. Use the generated header in your API requests.

---
