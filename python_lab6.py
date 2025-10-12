alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
length = len(alphabet)
vertical_spacing = '|'
horizontal_spacing = '--'

def vigenere_sq():
    print('   ', end=' ')
    for y in range(26):
        print(f"{alphabet[y]} |", end=' ')
    print()
    for z in range(36):
        print(horizontal_spacing,  end='|')
    for x in range(26):
        print()
        print(f"{alphabet[x]} |", end=' ')
        for i in range(0 + x, 26 + x, 1):
            print(f"{alphabet[i % 26]} |", end=' ')

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)

def index_to_letter(index, alphabet):
    return alphabet[index]

# keyword = pomegranate
# plaintext = I like turtles

def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    cipher_index = (key_index + plaintext_index) % length
    return index_to_letter(cipher_index, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher = ""
    key = key.upper()
    plaintext = plaintext.upper()

    for i in range (len(plaintext)):
        plain_letter = plaintext[i]
        key_letter = key[i % len(key)]

        if plain_letter in alphabet:
            encrypted_letter = vigenere_index(key_letter, plain_letter, alphabet)
            cipher += encrypted_letter
        else:
            cipher += plain_letter

    return cipher

keyword = "pomegranate"
plaintext = "I like turtles"

ciphertext = encrypt_vigenere(keyword, plaintext, alphabet)
print("Plaintext: ", plaintext)
print("Keyword: ", keyword)
print("Ciphertext: ", ciphertext)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    plaintext_index = (cipher_index - key_index) % length
    return index_to_letter(plaintext_index, alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
   uncipher = ""
   key = key.upper()
   cipher_text = cipher_text.upper()

   for i in range (len(cipher_text)):
       cipher_letter = cipher_text[i]
       key_letter = key[i % len(key)]

       if cipher_letter in alphabet:
           decrypted_letter = undo_vigenere_index(key_letter, cipher_letter, alphabet)
           uncipher += decrypted_letter
       else:
           uncipher +=cipher_letter

   return uncipher

decrypted_letter = decrypt_vigenere(keyword, ciphertext, alphabet)
print("Decrypted:", decrypted_letter)
