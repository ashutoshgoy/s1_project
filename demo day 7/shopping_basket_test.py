import unittest
from dataclasses import dataclass
from typing import List
from shopping_basket import Basket
@dataclass
class Item(object):
    unit_price:float
    quantity:1


 

class ShoppingBasketTest(unittest.TestCase):
    def test_empty_basket_total(self):
        basket=Basket([])
        self.assertEqual(basket.total(),0)


    def test_single_item_quantity_one(self):
         basket=Basket([Item(100.0,1)])
         self.assertEqual(basket.total(),100.0)
    # def test_no_of_items_quantity_one(self):
    #     basket=Basket([Item(100.0,1),Item(100,0,1)])
    def test_double_item_quantity_two(self):
         basket=Basket([Item(100.0,1),Item(100.0,1)])

if __name__=='__main__':
    pass
