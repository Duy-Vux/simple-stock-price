print("This program will give you the daily information of the stock market")
print("\n")

while True:
    print("For the daily stock's open price press 1")
    print("For the daily stock's high price press 2")
    print("For the daily stock's low price press 3")
    print("For the daily stock's close price press 4")
    print("For the daily stock's trading volume press 5")
    print("For the daily stock's price change in percentage press 6")
    print("To exit press 0")
    print("\n")

    option = int(input("Make a selection: "))

    if option != 0:
        import json
        import requests 
        from milestone_3 import Stock
        stock_d = {}

        stock_symbol = input("Enter the stock's symbol: ") 

        strAPI = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + stock_symbol + "&outputsize=full&apikey=IWW8S2HK4VEOV7ZQ"
        response = requests.get(strAPI)
        json_data = json.loads(response.text)

        for date in json_data["Time Series (Daily)"]:
            stock_d[date] = Stock(json_data["Meta Data"]["2. Symbol"], date, json_data["Time Series (Daily)"][date]["1. open"],\
                                json_data["Time Series (Daily)"][date]["2. high"], json_data["Time Series (Daily)"][date]["3. low"],\
                                json_data["Time Series (Daily)"][date]["4. close"], json_data["Time Series (Daily)"][date]["6. volume"])

        while True:
            stock_date = input("Enter a trading date following the format year-month-day: ")
            if stock_date in json_data["Time Series (Daily)"]:
                if option == 1:
                    stock_d[stock_date].stock_openprice()
                    break

                if option == 2:
                    stock_d[stock_date].stock_highprice()
                    break

                if option == 3:
                    stock_d[stock_date].stock_lowprice()
                    break

                if option == 4:
                    stock_d[stock_date].stock_closingprice()
                    break

                if option == 5:
                    stock_d[stock_date].stock_tradingvolume()
                    break

                if option == 6:
                    stock_d[stock_date].stock_pricechange()
                    break
            else:
                print("\nThere is no data for the given date, please enter a valid trading date")
                continue

        option_2 = int(input("\nAnything else (Press 1 for Yes and Press 0 for No)?: "))
        print("\n")
        if option_2 == 1:
            continue
        else:
            break
    else:
        break
    

    



