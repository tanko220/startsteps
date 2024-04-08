from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext, cipher.iv

def aes_decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_text

# Example usage:
key = get_random_bytes(16)  # Generate a random 128-bit key
plaintext = b'premier pas'
ciphertext, iv = aes_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = aes_decrypt(ciphertext, key, iv)
print("Decrypted text:", decrypted_text.decode())
