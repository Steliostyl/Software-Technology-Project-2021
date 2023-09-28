from datetime import datetime, date
import math

def round_decimals_up(number:float, decimals:int=2):
    #Returns a value rounded up to a specific number of decimal places.
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10 ** decimals
    return math.ceil(number * factor) / factor

class Transaction():
    def __init__(self, user, itemBought, ammountBought, public):
        self.user = user
        self.itemBought = itemBought
        self.ammountBought = ammountBought
        self.public = public
        self.ID = len(user.tradingHistory)
        #self.price = itemBought.dailyValues[datetime.now().date().isoformat()]['Close']
        #itemBought.printStock()
        self.price = round_decimals_up(itemBought.getCurrentPrice()*ammountBought)
        self.payment = None
        self.dateTime = datetime.now()

    def printTransaction(self):
        print('Bought:',self.ammountBought, 'shares of', self.itemBought.name, 'for', self.price, 'at' , self.dateTime)

class Payment():
    def __init__(self, user, price, paymentMethod, transactionList):
        self.price = price
        self.paymentMethod = paymentMethod # Account saved in Wallet
        #self.paymentID = len(user.tradingHistory)
        self.transactionList = transactionList
    
    def setPayment(user, pm, transactionList):
        paymentMethod = user.wallet.accounts[list(user.wallet.accounts)[pm]]
        print('Payment for buying:')
        totalSum = 0
        for transaction in transactionList:
            transaction.printTransaction()
            totalSum += transaction.price
            
        totalSum = round_decimals_up(totalSum)
        print('Total price:', totalSum)
        ans = paymentMethod.pay(totalSum)
        print(ans[1])
        if ans[0] == True:
            user.tradingHistory.extend(transactionList) # Adds transactions to user's Trading History
            return Payment(user, totalSum, paymentMethod, transactionList)
        return ans