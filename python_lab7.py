alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
length = len(alphabet)
vertical_spacing = '|'
horizontal_spacing = '--'

def vigenere_sq():
    square = []
    for x in range(26):
        row = []
        for i in range(26):
            row.append(alphabet[(x + i) % 26])
        square.append(row)

    print('   ', end=' ')
    for y in range(26):
        print(f"{alphabet[y]} |", end=' ')
    print()

    for z in range(36):
        print(horizontal_spacing, end='|')

    for x in range(26):
        print()
        print(f"{alphabet[x]} |", end=' ')
        for letter in square[x]:
            print(f"{letter} |", end=' ')

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)

def index_to_letter(index, alphabet):
    return alphabet[index]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    cipher_index = (key_index + plaintext_index) % length
    return index_to_letter(cipher_index, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    cipher_list = []
    key = key.upper()
    plaintext = plaintext.upper()

    for i in range (len(plaintext)):
        plain_letter = plaintext[i]
        key_letter = key[i % len(key)]

        if plain_letter in alphabet:
            encrypted_letter = vigenere_index(key_letter, plain_letter, alphabet)
            cipher_list.append(encrypted_letter)
        else:
            cipher_list.append(plain_letter)

    return ''.join(cipher_list)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    plaintext_index = (cipher_index - key_index) % length
    return index_to_letter(plaintext_index, alphabet)

def decrypt_vigenere(key, cipher_text, alphabet):
   plain_list = []
   key = key.upper()
   cipher_text = cipher_text.upper()

   for i in range (len(cipher_text)):
       cipher_letter = cipher_text[i]
       key_letter = key[i % len(key)]

       if cipher_letter in alphabet:
           decrypted_letter = undo_vigenere_index(key_letter, cipher_letter, alphabet)
           plain_list.append(decrypted_letter)
       else:
           plain_list.append(cipher_letter)

   return ''.join(plain_list)

encrypted_list = []

def menu_encrypt():
    plain_text = input("Enter text to encrypt: ")
    keyword = input("Enter a keyword: ")
    cipher_text = encrypt_vigenere(keyword, plain_text, alphabet)
    encrypted_list.append((cipher_text, keyword))
    print("Encrypted text: ", cipher_text)

def menu_decrypt():
    print("Decrypting...")
    for cipher_text, keyword in encrypted_list:
        decrypted_text = decrypt_vigenere(keyword, cipher_text, alphabet)
        print(decrypted_text)
    print()

def menu_dump():
    print("Encrypted texts currently stored:")
    for cipher_text, keyword in encrypted_list:
        print(cipher_text)
    print()

def menu_quit():
    print("Goodbye!")
    exit()

menu = [
    ["1. Encrypt", menu_encrypt],
    ["2. Decrypt", menu_decrypt],
    ["3. Dump", menu_dump],
    ["4. Quit", menu_quit]
]

while True:
    print("This is a Menu:")
    for item in menu:
        print(item[0])
    choice = input("Enter your choice: ")

    if choice == "1" or choice == "2" or choice == "3" or choice == "4":
        menu[int(choice)-1][1]()
    else:
        print("Invalid choice")