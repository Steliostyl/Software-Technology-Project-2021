import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import user
import transactions

stock_Markets = {}

def getMarketsInCountry(country):
    marketsInCountry = []
    for stockMarket in stock_Markets:
        if stockMarket.country == country:
            marketsInCountry.append(stockMarket)
    return marketsInCountry

class Stock():
    def __init__(self, name, symbol, dailyValues, country, sectors = []):
        self.symbol = symbol
        self.name = name
        self.dailyValues = dailyValues
        self.country = country
        self.sectors = sectors
    
    def getCurrentPrice(self):
        return transactions.round_decimals_up(self.dailyValues[list(self.dailyValues)[len(list(self.dailyValues))-1]]['Close'], 2)

    def printStock(self, formatted=True):
        print('--Stock information--\nName:',self.name, '\nSymbol:', self.symbol,'\nDaily Data:')
        for key in self.dailyValues:
            if formatted==True:
                formatedMonth = '{:02d}'.format(key.month)
                formatedDay = '{:02d}'.format(key.day)
            else:
                formatedMonth = key.month
                formatedDay = key.day
            print(f"{key.year}-{formatedMonth}-{formatedDay} {self.dailyValues[key]}")

class Stock_Market():
    def __init__(self, country, index):
        self.index = index
        self.country = country
        self.market_indexes = []
        self.stocks = {}
        self.getAllStocksData()
        stock_Markets[self.index] = self
    
    def dfToDictCustom(self, df, tempDict):
        finalDict = {}
        for key in tempDict:
            finalDict[dt.date(key.year, key.month, key.day)] = tempDict[key]
        return finalDict

    def getStockDataFromAPI(self, name, symbol, start, end, country):
        dailyValues = {}
        style.use('ggplot')
        df = web.DataReader(symbol, 'yahoo', start, end)
        tempDict = df.to_dict(orient='index')
        finaldict = self.dfToDictCustom(df, tempDict)
        tempStock = Stock(name, symbol, finaldict, country)
        self.stocks[symbol] = tempStock

    def getAllStocksData(self):
        tsla    = ['Tesla Inc', 'TSLA', 'USA']
        amd     = ['Advanced Micro Devices, Inc.', 'AMD', 'USA']
        googl   = ['Alphabet Inc.','GOOGL', 'USA']
        fb      = ['Facebook, Inc.','FB', 'USA']
        zm      = ['Zoom Video Communications, Inc.','ZM', 'USA']
        czr     = ['Caesars Entertainment Inc','CZR', 'USA']
        cat     = ['Caterpillar Inc.','CAT', 'USA']
        opap    = ['Greek Organization of Football Prognostics S.A.','OPAP.AT', 'Greece']
        asml    = ['ASML Holding', 'asml', 'Netherlands']
        paypal  = ['Paypal Holdings Inc','PYPL', 'USA']
        nbg     = ['National Bank of Greece S.A.', 'ETE.AT', 'Greece']
        plaisio = ['Plaisio Computers S.A.', 'PlAIS.AT', 'Greece']
        moh     = ['Motor Oil (Hellas) Corinth Refineries S.A.', 'MOH.AT', 'Greece']

        if self.index == 'NASDAQ':
            stocksToGet = [zm, asml, paypal]
        elif self.index == 'S&P 500':
            stocksToGet = [tsla, amd, googl, fb, czr, cat]
        elif self.index == 'ATG':
            stocksToGet = [opap, nbg, plaisio, moh]
        
        for aStock in stocksToGet:
            tmp = self.getStockDataFromAPI(aStock[0], aStock[1], dt.datetime(2020, 1, 1), dt.datetime.now(), aStock[2])

    def getStockAttributes(self, symbol, start = dt.date(2020,1,1), end = dt.date.today()):
        tempDailyStockValues = {}
        for val in self.stocks[symbol].dailyValues:
            if (val >= start) & (val <= end) :
                tempDailyStockValues[val] = self.stocks[symbol].dailyValues[val]
        return Stock(self.stocks[symbol].name, self.stocks[symbol].symbol, tempDailyStockValues, self.stocks[symbol].country)

    def printAllStockNames(self):
        for s in self.stocks:
            print(s, self.stocks[s].name)

#nsd = Stock_Market('USA')
##nsd.getStockAttributes('TSLA').printStock()
#print(dt.datetime(2020,1,2))
#print(nsd.getStockAttributes('TSLA').dailyValues[dt.datetime(2020,1,2)]['Close'])