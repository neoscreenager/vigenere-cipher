#!/usr/bin/env python3

'''
    Test cases to test functions defined in vigenere cipher program.

'''

import unittest
from vigenere_cipher import encrypt, decrypt

class TestCrypto(unittest.TestCase):

    def test_encrypt(self):
        enctypted_text = encrypt('BLOCKCHAIN', 'IITIBM')
        self.assertEqual(enctypted_text, 'JTHKLOPIBV')

    def test_decrypt(self):
        decrypted_text = decrypt('JTHKLOPIBV', 'IITIBM')
        self.assertEqual(decrypted_text, 'BLOCKCHAIN')

    def test_encrypt_lowercase(self):
        enctypted_text = encrypt('blockchain', 'iitibm')
        self.assertEqual(enctypted_text, 'JTHKLOPIBV')

    def test_decrypt_lowercase(self):
        decrypted_text = decrypt('jthklopibv', 'iitibm')
        self.assertEqual(decrypted_text, 'BLOCKCHAIN')

if __name__ == '__main__':
    unittest.main(exit=False)  # to avoid the end of execution traceback