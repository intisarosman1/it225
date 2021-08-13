import unittest
from order import Order
from itemdetails import Itemdetails 
import datetime

class TestOrder(unittest.TestCase):
    #set up an instance of the class
    def setUp(self):
        self.order=Order(18907, '2021-08-11', '7:50')
    #test the get methods
    def test_getOrderID(self):
        self.assertEqual(self.order.getOrderID(), 18907)

    def test_setOrderID(self):
        self.order.setOrderID(18907)
        self.assertEqual(self.order.getOrderID(), 18907)

    def test_date(self):
        self.assertEqual(self.order.getOrderDate(),'2021-08-11')
    
    def test_time(self):
        self.assertEqual(self.order.getOrderTime(),'7:50')

    # test the item details
    class TestItemdetails(unittest.TestCase):
    def setUp(self):
        self.itemdetails=Itemdetails(700462, 'Romaine lettuce', 2, 4.99)

    def test_getItemName(self):
        self.assertEqual(self.itemdetails.getItemName(), 'Romaine Lettuce')

    def test_getItemID(self):
        self.assertEqual(self.itemdetails.getItemID(), 700462)

    def test_setItemId(self):
        self.itemdetails.setItemID(700462)
        self.assertEqual(self.itemdetails.getItemID(), 700462)

    def test_GetOrderQuantity(self):
        self.assertEqual(self.itemdetails.getOrderQuantity(), 2)

    def test_SetOrderQuantity(self):
        self.itemdetails.setItemID(700462)
        self.assertEqual(self.itemdetails.getOrderQuantity(), 2)

def test_GetOrderPrice(self):
        self.assertEqual(self.itemdetails.getOrderQuantity(), 4.99)

    def test_SetOrderPrice(self):
        self.itemdetails.setItemID(700462)
        self.assertEqual(self.itemdetails.getOrderQuantity(), 4.99)


   