#!/usr/bin/env python3
'''
    Encrypt/Decrypt using Vigenere Cipher technique

'''
alpha = ['A', 'B', 'C', 'D' ,'E' ,'F' ,'G' ,'H' ,'I' ,'J' ,'K' ,'L' ,'M' ,'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U' ,'V' ,'W' ,'X' ,'Y' ,'Z']

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
            tabularecta[i,n] = alpha[startn-1]
        else:
            startn = 1
            tabularecta[i,n] = alpha[startn-1]
        startn += 1
        n += 1
    i += 1
'''
print("Printing table from the two-dimensional array to visually verify")
row = 0
while row < 26:
    col = 0
    while col < 26:
        print("%s" % tabularecta[row,col], end=' ')
        col+=1
    print()
    row+=1

'''

# Presenting the user with a menu with options to 1)Encrypt 2)Decrypt 3)Info about Vigenere Cipher and 4)Exit
print("Please choose any one of the following:")
print("Enter 1 for Encryption")
print("Enter 2 for Decryption")
print("Enter 3 to see info about Vigenere Cipher")
print("Enter 4 to exit the program or Ctrl-C")
choice = int(input(""))
if choice == 1:
    print("Encryption mechanism work in progress.")
elif choice == 2:
    print("Decryption mechanism work in progress.")
elif choice == 3:
    print("More about Vignere Cipher... coming soon...")
elif choice == 4:
    print("Bye!")
else:
    print("Sorry, this program can offer you only these four choices, please enter only 1, 2, 3 or 4. Thanks.")