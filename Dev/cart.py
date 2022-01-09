'''
This file contain Cart library

@Author : Hisyam M
'''
import json
import os
from typing import Type 

class Cart:
    '''
    This class contain main function of Shopphing cart
    '''
    def __init__(self):
        pass

    def readJson(self) :
        cur_path = os.path.dirname(__file__)
        path = os.path.relpath('..\\Lib\\shoppingCart.json', cur_path)
        jsonfile = open(path,'r')
        data = json.load(jsonfile)

        return data

    def writeJson(self, dataInput) :
        cur_path = os.path.dirname(__file__)
        path = os.path.relpath('..\\Lib\\shoppingCart.json', cur_path)
        with open(path, 'w') as outfile:
            json.dump(dataInput, outfile)

    def tambahProduk(self, kodeProduk, kuantitas):
        '''
        This function will add kodeProduk as key and kuantitas as value to local dict
        '''
        if isinstance(kodeProduk, str) :
            if isinstance(kuantitas, int) :   
                json_object = self.readJson()
                if kodeProduk in json_object :
                    json_object[kodeProduk] = json_object[kodeProduk] + kuantitas
                else :
                    json_object[kodeProduk] = kuantitas 

                self.writeJson(json_object)
            else : 
                raise TypeError("kuantitas must be an integer!")
        else :
            raise TypeError("kodeProduk must be a string!")

    def hapusProduk(self, kodeProduk):
        '''
        This function will remove all record with kodeProduk as key from local dict
        '''
        json_object = self.readJson()
        if kodeProduk in json_object :
            del json_object[kodeProduk]
        else :
            raise KeyError("Produk tidak tersedia")
        self.writeJson(json_object)

    def tampilkanCart(self):
        '''
        This fuction will show latest update of cart value
        '''
        print("Here is you current shopping cart : ")
        json_object = self.readJson()
        for k, v in json_object.items() :
            print("{0} ({1})".format(k,v))