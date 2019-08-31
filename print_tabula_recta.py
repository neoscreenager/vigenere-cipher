#!/usr/bin/env python3
'''
    The code prints the "Tabula Recta", the 26 x 26 table of alphabets used to
    encrypt and decrypt using Vigenère Cipher method.
    The code does not encrypt/decrypt, it just print the table and storing it
    into a two-dimensional array.
    This technique will be used in the program to encrypt/decrypt text using
    Vigenère Cipher for lookup in tabula recta.
'''
i = 0
startn = 0
tabularecta = {}
alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
         'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print("-" * 100)
while i < 26:
    n = 0
    startn = i+1
    endn = 26
    while n <= 25:
        if(startn <= endn):
            tabularecta[i, n] = alpha[startn-1]
            print("%s" % alpha[startn-1], end=' ')
            # print("%2d" % startn, end=' ') # uncomment to print numbers
        else:
            startn = 1
            tabularecta[i, n] = alpha[startn-1]
            print("%s" % alpha[startn-1], end=' ')
            # print("%2d" % startn, end=' ') # uncomment to print numbers
        startn += 1
        n += 1
    print()
    i += 1
print("-" * 100)
print("Printing table from the two-dimensional array")
row = 0
while row < 26:
    col = 0
    while col < 26:
        print("%s" % tabularecta[row, col], end=' ')
        col += 1
    print()
    row += 1

print(tabularecta[alpha.index('G'), alpha.index('A')])