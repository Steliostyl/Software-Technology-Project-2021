import transactions
import user
import stocks
import read_crypto_data
import get_crypto_data
import wallet_carrier
from datetime import date

def getCountrySpecificStocks(country):
    countrySpecificStocks = []
    for market in stocks.getMarketsInCountry(country):
        countrySpecificStocks.extend(market.stocks)
    print(countrySpecificStocks)
    return countrySpecificStocks

# Create stock markets
nsd = stocks.Stock_Market('USA', 'NASDAQ')
sp = stocks.Stock_Market('USA', 'S&P 500')
atg = stocks.Stock_Market('Greece', 'ATG')

# Get Stock Data in a specific date range
sp.getStockAttributes('TSLA',date(2020,2,2), date(2020,3,1)).printStock()

# Create two users
kypr = user.User('kypr','kyprianosmantis@gmail.com', '123456')
kypr2 = user.User('kypr2','kyprianosmantis@gmail.com', '123456')

# Create carriers (and add them to the Carrier Dictionary)
wallet_carrier.Carrier('National Bank of Greece')
wallet_carrier.Carrier('Piraeus Bank')
wallet_carrier.Carrier('PayPal')

# Create new carrier accounts and add them to 
# the corresponding carrier's accounts dictionary
tempAcc = wallet_carrier.Account(1234567890, 'Qwerty!@34', 'National Bank of Greece', 1000)
wallet_carrier.carrierDictionary[tempAcc.carrierName].accounts[tempAcc.ID] = tempAcc
tempAcc = wallet_carrier.Account(4567890123, 'Qwerty!@34', 'Piraeus Bank', 2500)
wallet_carrier.carrierDictionary[tempAcc.carrierName].accounts[tempAcc.ID] = tempAcc
tempAcc = wallet_carrier.Account('kiprianosmantis@gmail.com', 'Qwerty!@34', 'PayPal', 4000)
wallet_carrier.carrierDictionary[tempAcc.carrierName].accounts[tempAcc.ID] = tempAcc

# Add payment methods to wallet
kypr.wallet.addPaymentMethod('National Bank of Greece',(1234567890, 'Qwerty!@34'))
kypr.wallet.addPaymentMethod('Piraeus Bank',(4567890123, 'Qwerty!@34'))
kypr.wallet.addPaymentMethod('PayPal',('kiprianosmantis@gmail.com', 'Qwerty!@34'))
#wallet_carrier.printAllAccountsInAllCarriers()

# Buy 2 shares at Tesla and 3 shares at Plaisio (private transactions)
kypr.buy({sp.stocks['TSLA']:(2, False),atg.stocks['PlAIS.AT']:(3, False)})

# Show balance in accounts after payment
kypr.wallet.printPaymentMethods()

# Check user's Trading History
print('Trading History of user',kypr.username)
for transaction in kypr.getUserTransactions():
    transaction.printTransaction()

# Create Crypto Market
cm = read_crypto_data.Crypto_Market()

# Print all crypto coins in the market
cm.printAllCryptoNames()

# Get Crypto Data in a specific date range
cm.getCryptoAttributes('BTC', datetime(2021,1,1)).printCrypto()