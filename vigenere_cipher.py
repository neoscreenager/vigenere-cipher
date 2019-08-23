#!/usr/bin/env python3
'''
    Encrypt/Decrypt using Vigenere Cipher technique
    Vigenere Cipher is a method of encrypting alphabetic text.
    It uses a simple form of polyalphabetic substitution. A polyalphabetic
    cipher is any cipher based on substitution, using multiple substitution alphabets .
    The encryption of the original text is done using the Vigenère square aka Vigenère table aka Tabula Recta.
    The table consists of the alphabets written out 26 times in different rows, each alphabet
    shifted cyclically to the left compared to the previous alphabet, corresponding to
    the 26 possible Caesar Ciphers.
    At different points in the encryption process, the cipher uses a different alphabet from one of the rows.
    The alphabet used at each point depends on a repeating keyword.

'''
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Creating the Tebula Recta for encryption/decryption

i = 0
startn = 0
tabularecta = {}
while i < 26:
    n = 0
    startn = i+1
    endn = 26
    while n <= 25:
        if(startn <= endn):
            tabularecta[i, n] = alpha[startn-1]
        else:
            startn = 1
            tabularecta[i, n] = alpha[startn-1]
        startn += 1
        n += 1
    i += 1

# function to enlarge the key by repeting the key in circular manner until it
# matches the length of plain text
def key_enlarge(key, text_length):
    enlarged_key = key
    key_length = len(key)
    q = text_length // key_length
    r = text_length % key_length
    for i in range(0, q-1):
        enlarged_key += key
    enlarged_key += key[0:r]
    return enlarged_key

# function to shrink the key to make it equal to the text if text length is
# less than the key length
def key_shrink(key, text_length):
    shrinked_key = key[0:text_length]
    return shrinked_key

# Presenting the user with a menu with options to 1)Encrypt 2)Decrypt 3)Info
# about Vigenere Cipher and 4)Exit
print("Please choose any one of the following:")
print("Enter 1 for Encryption")
print("Enter 2 for Decryption")
print("Enter 3 to see info about Vigenere Cipher")
print("Enter 4 to exit the program or Ctrl-C")
choice = int(input(""))
if choice == 1:
    '''
        For Encryption, plain text characters will be used as row and key
        characters will be used as column to identify the character from
        tabularecta as tabularecta[row, column]
        Steps to encrypt:
        #1 : Take plain text and key as input in upper case
        #2 : Enlarge or shrink key to match with the length of plain text
        #3 : Loop through each character of plain text and key to find out
             the character from tabularecta and append these characters to
             get the cipher text

        A more easy implementation could be to visualize Vigenère
        algebraically by converting [A-Z] into numbers [0–25].
        The the plaintext(P) and key(K) are added modulo 26.
        Ei = (Pi + Ki) mod 26
        But we are implementing above steps for encryption, algebraically
        implementation we will do for decryption
    '''
    # 1
    plain_text = str(input("Enter plain text:")).upper()
    key = str(input("Enter key:")).upper()
    cipher_text = ""
    # 2
    plain_text_len = len(plain_text)
    key_len = len(key)
    if plain_text_len > key_len:
        key = key_enlarge(key, plain_text_len)
    elif plain_text_len < key_len:
        key = key_shrink(key, plain_text_len)
    # 3
    for x in range(0, plain_text_len):
        cipher_text += tabularecta[alpha.index(plain_text[x]), alpha.index(key[x])]
    print(f"Encrypted text is : {cipher_text}")
elif choice == 2:
    '''
        Decryption is performed by going to the row
        in the table corresponding to the key, finding
        the position of the ciphertext letter in this row,
        and then using the column’s label as the plaintext.

        Decryption will be done algebraically by converting [A-Z]
        into numbers [0–25].
        Di = (Ei - Ki + 26) mod 26
    '''
    # 1
    cipher_text = str(input("Enter cipher text:")).upper()
    key = str(input("Enter key:")).upper()
    plain_text = ""
    # 2
    cipher_text_len = len(cipher_text)
    key_len = len(key)
    if cipher_text_len > key_len:
        key = key_enlarge(key, cipher_text_len)
    elif cipher_text_len < key_len:
        key = key_shrink(key, cipher_text_len)
    # 3
    for x in range(0, len(key)):
        plain_text += alpha[(alpha.index(cipher_text[x]) - alpha.index(key[x]) + 26) % 26]
    print(f"Dcrypted text: {plain_text}")
elif choice == 3:
    print('''
    Vigenere Cipher is a method of encrypting alphabetic text.
    It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher
    based on substitution, using multiple substitution alphabets .
    The encryption of the original text is done using the Vigenère square aka Vigenère table aka Tabula Recta.
    The table consists of the alphabets written out 26 times in different rows, each alphabet
    shifted cyclically to the left compared to the previous alphabet, corresponding to
    the 26 possible Caesar Ciphers.
    At different points in the encryption process, the cipher uses a different alphabet from one of the rows.
    The alphabet used at each point depends on a repeating keyword.
    For generating key, the given keyword is repeated in a circular manner until it matches the length of
    the plain text. Letter of the plain text is then used as row and letter of key is used as column to pick
    the cipher text letter from tabula recta.
    Decryption is performed by going to the row in the table corresponding to the key,
    finding the position of the ciphertext letter in this row,
    and then using the column’s label as the plaintext.
    ''')
elif choice == 4:
    print("Bye!")
else:
    print("Sorry, this program can offer you only these four choices,\
          please enter only 1, 2, 3 or 4. Thanks.")