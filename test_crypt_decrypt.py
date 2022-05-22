import unittest
from crypt_decrypt import AESCipher


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.cipher = AESCipher("abc")

    def test_pad_unpad(self):
        self.assertEqual("1234", self.cipher._AESCipher__unpad(self.cipher._AESCipher__pad("1234")))

    def test_encrypt_and_decrypt(self):
        self.assertEqual("1234", self.cipher.decrypt(self.cipher.encrypt("1234")))  # add assertion here


if __name__ == '__main__':
    unittest.main()
