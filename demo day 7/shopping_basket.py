import unittest
from dataclasses import dataclass
from typing import List

from item import Item




@dataclass
class Basket(object):
    items:List[Item]
    def total(self):


      return reduce(lambda subtotal,item:subtotal+item.unit_price,self.items,0)

