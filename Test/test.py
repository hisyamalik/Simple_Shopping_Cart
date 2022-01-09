'''
This unitest file for Shopping cart function

@Author : Hisyam M
'''

import io
import sys
sys.path.insert(0,"..")
import unittest
from Dev.cart import Cart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        pass

    def test_tambah_produk_success(self):
        testCart = Cart()
        testCart.tambahProduk("Apel",1)
        testCart.tambahProduk("Jeruk",2)
        actual = testCart.readJson() 
        expected = {"Apel": 1, "Jeruk": 2}
        self.assertEqual(actual, expected)

    def test_tambah_produk_success_key_exist(self):
        testCart = Cart()
        testCart.tambahProduk("Apel",1)
        testCart.tambahProduk("Jeruk",2)
        testCart.tambahProduk("Apel",1)
        actual = testCart.readJson() 
        expected = {"Apel": 3, "Jeruk": 4}
        self.assertEqual(actual, expected)

    def test_tambah_produk_wrong_param_1(self):
        testCart = Cart()
        with self.assertRaises(TypeError) as exception_context:
            testCart.tambahProduk(11,1)
        self.assertEqual(
            str(exception_context.exception),
            "kodeProduk must be a string!"
        )

    def test_tambah_produk_wrong_param_1(self):
        testCart = Cart()
        with self.assertRaises(TypeError) as exception_context:
            testCart.tambahProduk("Apel","1")
        self.assertEqual(
            str(exception_context.exception),
            "kuantitas must be an integer!"
        )

    def test_hapus_produk_if_not_exist(self):
        testCart = Cart()
        with self.assertRaises(KeyError) as exception_context:
            testCart.hapusProduk("Durian")
        self.assertEqual(
            str(exception_context.exception),
            "'Produk tidak tersedia'"
        )
        
    def test_tampilkan_produk(self):
        testCart = Cart()
        capturedOutput = io.StringIO()         
        sys.stdout = capturedOutput                   
        testCart.tampilkanCart()                    
        sys.stdout = sys.__stdout__                  
        print ('', capturedOutput.getvalue())   
        expected = "Here is you current shopping cart : \nApel (3)\nJeruk (4)\n"
        self.assertEqual(capturedOutput.getvalue(), expected)


    def test_hapus_produk_if_exist(self):
        testCart = Cart()
        testCart.tambahProduk("Apel",1)
        testCart.tambahProduk("Apel",1)
        testCart.hapusProduk("Apel")
        actual = testCart.readJson() 
        expected = {"Jeruk": 4}
        # self.assertEqual(actual, expected)

    def tearDown(self):
        pass