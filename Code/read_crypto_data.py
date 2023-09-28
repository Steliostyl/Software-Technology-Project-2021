import pandas as pd
import get_crypto_data as gcd
import csv
from datetime import datetime, date
from matplotlib import style
import user

from_symbol = 'BTC'
to_symbol = 'USD'
exchange = 'Bitstamp'
datetime_interval = 'day'
name = 'Bitcoin'

class Crypto_Coin():
    def __init__(self, name, symbol, dailyValues):
        self.symbol = symbol
        self.name = name
        self.dailyValues = dailyValues
        
    def getCurrentPrice(self):
        return transactions.round_decimals_up(self.dailyValues[list(self.dailyValues)[len(list(self.dailyValues))-1]]['Close'], 2)

    def printCrypto(self, formatted=True):
        print('--Crypto Coin information--\nName:',self.name, '\nSymbol:', self.symbol,'\nDaily Data:')
        for key in self.dailyValues:
            if formatted==True:
                formatedMonth = '{:02d}'.format(key.month)
                formatedDay = '{:02d}'.format(key.day)
            else:
                formatedMonth = key.month
                formatedDay = key.day
            print(f"{key.year}-{formatedMonth}-{formatedDay} {self.dailyValues[key]}")

class Crypto_Market():
    def __init__(self):
        self.cryptoCoins = {}
        self.getAllCryptoData()
    
    def createCryptoFromCSV(self, filename):
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            cryptocoinDict = {}
            for row in csv_reader:
                #if line_count == 0:
                #    print(f'Column names are {", ".join(row)}')
                #    line_count += 1
                tempDailyCryptoValues = {}
                tempDailyCryptoValues['low'] = row['low']
                tempDailyCryptoValues['high'] = row['high']
                tempDailyCryptoValues['open'] = row['open']
                tempDailyCryptoValues['close'] = row['close']
                tempDailyCryptoValues['volumefrom'] = row['volumefrom']
                tempDailyCryptoValues['volumeto'] = row['volumeto']
                #Convert row['datetime'] from string to datetime
                tmp = datetime.strptime(row['datetime'], '%Y-%m-%d')
                cryptocoinDict[date(tmp.year,tmp.month,tmp.day)] = tempDailyCryptoValues
                line_count += 1
        #print(f'Processed {line_count} lines.')
        cryptocoin = Crypto_Coin(name, from_symbol, cryptocoinDict)
        return cryptocoin
    
    def getCryptoAttributes(self, symbol, start = date(2020,1,1), end = date.today()):
        tempDailyStockValues = {}
        for val in self.cryptoCoins[symbol].dailyValues:
            print(type(start))
            if (val >= start) & (val <= end):
                tempDailyStockValues[val] = self.cryptoCoins[symbol].dailyValues[val]
        return Crypto_Coin(self.cryptoCoins[symbol].name, self.cryptoCoins[symbol].symbol, tempDailyStockValues)

    def getAllCryptoData(self):
        tempfilename = gcd.get_filename(from_symbol, to_symbol, exchange, datetime_interval, datetime.now().date().isoformat())
        self.cryptoCoins[from_symbol] = self.createCryptoFromCSV(tempfilename)

    def printAllCryptoNames(self):
        for s in self.cryptoCoins:
            print(s, self.cryptoCoins[s].name, self.cryptoCoins[s].symbol)


#cm = Crypto_Market()
#cm.printAllCryptoNames()
#cm.getCryptoAttributes('BTC', date(2021,1,1)).printCrypto()

#filename = gcd.get_filename(from_symbol, to_symbol, exchange, datetime_interval, datetime.now().date().isoformat())
#btc = Cryptocoin.createCryptoFromCSV(gcd.get_filename(from_symbol, to_symbol, exchange, datetime_interval, datetime.now().date().isoformat()))
#btc.printCrypto()