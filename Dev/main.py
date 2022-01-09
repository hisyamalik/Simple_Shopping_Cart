'''
This file is main program to execute Shopphing Cart Lib

@Author : Hisyam 
'''
from cart import Cart

myCart = Cart()
myCart.tambahProduk("Apel",1)
myCart.tambahProduk("Semangka",2)
myCart.tambahProduk("Jeruk",1)

myCart.tampilkanCart()

myCart.hapusProduk("Apel")

myCart.tampilkanCart()