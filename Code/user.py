from enum import Enum
import wallet_carrier
from datetime import datetime, date
import transactions

def addYears(d, years):
    try:
        #Return same day of the current year        
        return d.replace(year = d.year + years)
    except ValueError:
        #If not same day, it will return other, i.e.  February 29 to March 1 etc.        
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

class Subscription_Plan():
    def __init__(self, subPlanTitle, cost, features):
        self.subPlanTitle = subPlanTitle
        self.cost = cost
        self.features = features # List of plan features
    def printSubPlan(self):
        print(self.subPlanTitle, self.cost, self.features)

class Subscription_Plan_List(Enum):
    STANDARD = Subscription_Plan('Standard', 0, ['default features'])
    ADVANCED = Subscription_Plan('Advanced', 10, ['default features','extra feature 1', 'extra feature 2'])
    PREMIUM = Subscription_Plan('Premium', 20, ['default features','extra feature 1', 'extra feature 2','extra feature 3','extra feature 4'])

class User():
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.prefferedPM = None
        self.following = []
        self.portofolio = {} # A dictionary containing all bought stocks and crypto coins (one array for each)
        self.wallet = wallet_carrier.Wallet()
        self.subscriptionPlan = Subscription_Plan_List.STANDARD.value
        self.planExpDate = addYears(datetime.now(), 1)
        self.tradingHistory = [] # A list of transactions

    def getUserTransactions(self, start=None):
        if start == None:
            return self.tradingHistory
        #else:
        #    filteredTable = []
        #    for transaction in self.tradingHistory:
        #        if transaction.dateTime 
        
    def buy(self, itemsToBuy):
        transactionList = []
        # itemsToBuy = Dictionary with the stock/crypto object as key and 
        # a tuple consisted of (ammount, public) as value
        for item in itemsToBuy:
            transactionList.append(transactions.Transaction(self, item, itemsToBuy[item][0],itemsToBuy[item][1]))

        print('Choose payment method from wallet:')
        self.wallet.printPaymentMethods()
        pm = int(input()) - 1
        while pm not in range(len(self.wallet.accounts)):
            print('Please choose a valid option!')
            pm = int(input()) - 1
        #self.wallet.accounts[list(self.wallet.accounts)[pm]].printAccount()
        transactions.Payment.setPayment(self, pm, transactionList)
        #self.wallet.accounts[list(self.wallet.accounts)[pm]].pay()
        #Payment.setPayment(self, paymentMethod, transactionList)

#kypr = User('kypr','kyprianosmantis@gmail.com', '123456')
#kypr2 = User('kypr2','kyprianosmantis@gmail.com', '123456')

#kypr.tradingHistory.append(transactions.Transaction(kypr, 10, False))

# Testing to see if the to plans are the same class object

#if kypr.subscriptionPlan is kypr2.subscriptionPlan:
#    print('True')
#    kypr.subscriptionPlan.printSubPlan()
#else:
#    print('False')