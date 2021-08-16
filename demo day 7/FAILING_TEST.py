import unittest
@dataclass
class Basket(object):
    items:List

    def total(self):
      if len(self.items)>0:

class ShoppingBasketTest(unittest,TestCase):
      def test_empty_basket_total(self):
          basket=Basket([])
          self.assertEqual(basket.total(),0)
      def test_single_item_

if __name__=='__main__':
    pass