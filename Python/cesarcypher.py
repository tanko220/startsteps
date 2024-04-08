def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():  # check if the character is alphabet
            base = ord('A') if char.isupper() else ord('a')  # set base according to uppercase or lowercase
            result += chr((ord(char) - base + shift) % 26 + base)  # apply Caesar cipher shift
        else:
            result += char  # if not alphabet, keep it unchanged
    return result

# Example usage:
text = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print("Encrypted text:", encrypted_text)

# Decrypting the text
decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text:", decrypted_text)
