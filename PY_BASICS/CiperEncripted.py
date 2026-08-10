import random
import string

# Characters set
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Create key by shuffling characters
key = chars.copy()
random.shuffle(key)

# Debug (optional)
print(f"chars: {chars}")
print(f"key  : {key}")

# ---------------- ENCRYPT ----------------
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message  : {plain_text}")
print(f"encrypted message : {cipher_text}")


# ---------------- DECRYPT ----------------
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"original message  : {plain_text}")
print(f"encrypted message : {cipher_text}")
