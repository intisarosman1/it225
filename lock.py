import datetime

class Order():
    def __init__(self, orderid, date, time):
        self.orderid=orderid
        self.date=datetime.date.today()
        self.time=datetime.time.strftime()
    
    def getOrderID(self):
        return self.orderid
    
    def getOrderDate(self):
        return self.date

    def getOrderTime(self):
        return self.time
