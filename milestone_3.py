class Stock:
    def __init__( self, name, date, open, high, low, close, volume):
        self.name = name
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def stock_openprice(self):
        print(self.name, "open price in", self.date, ":", self.open)
    
    def stock_highprice(self):
        print(self.name, "high price in", self.date, ":", self.high)

    def stock_lowprice(self):
        print(self.name, "low price in", self.date, ":", self.low)
    
    def stock_closingprice(self):
        print(self.name, "close price in", self.date, ":", self.close)

    def stock_tradingvolume(self):
        print(self.name, "trading volume in", self.date, ":", self.volume)

    def stock_pricechange(self):
        price_change = ((float(self.close) - float(self.open))/float(self.open))*100
        print(self.name, "price change (in percentage) in", self.date, ":", price_change, "%")


    

