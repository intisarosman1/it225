class ItemDetails():
    def __init__(self, itemid, itemname, orderquantity, orderprice):
        self.itemid=itemid
        self.itemname=itemname
        self.orderquantity=orderquantity
        self.orderprice=orderprice
    
    
    def getItemID(self):
        return self.itemid

    def getItemName(self):
        return self.itemname
    
    def getOrderQuantity(self):
        return self.orderquantity

    def getOrderPrice(self):
        return self.orderprice

