carrierDictionary = {}

# The class Account is being used by both the class Wallet and by the class Carrier. 
# In the 1st case, only the ID, password and carrier names are being used, so that
# the user doesn't have to input his credentials every time. 
# However, the balance attribute of the class is irrelevant in this case. 
# In the 2nd case, it's externally stored in a Carrier's Database

class Account():
    def __init__(self, ID, password, carrierName, balance=None):
        self.ID = ID
        self.password = password
        self.carrierName = carrierName #string
        self.balance = balance
    
    def pay(self, ammount):
        return carrierDictionary[self.carrierName].chargeAccount((self.ID, self.password), ammount)

    def printAccount(self):
        print('Account ID:', self.ID, '\nBalance:', self.balance)

class Carrier():
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        carrierDictionary[name] = self

    def verifyCredentials(self, credentials):
        # Credentials is a tuple of 2 elements, 
        # in which the 1st element is the account ID and 
        # the 2nd element the password
        if self.accounts[credentials[0]] is not None:
            if self.accounts[credentials[0]].password == credentials[1]:
                return (True, '')
            else: 
                return (False, 'Incorrect Credentials')
        else: 
            return(False, 'Incorrect Credentials')

    def getAccountBalance(self, credentials):
        response = self.verifyCredentials(credentials)
        if  response[0] == True:
            return (True, self.accounts[credentials[0]].balance)
        else: 
            return response

    def chargeAccount(self, credentials, ammount):
        if self.verifyCredentials(credentials)[0] == True:
            if self.accounts[credentials[0]].balance >= ammount :
                self.accounts[credentials[0]].balance = self.accounts[credentials[0]].balance - ammount
                #print(self.accounts[credentials[0]].balance)
                return (True, 'Payment successful')
            else:
                return (False, 'Not enough funds in account')
        else:
            return (False, 'Incorrect Credentials')

    def printAllAccounts(self):
        print(self.name)
        for account in self.accounts:
            self.accounts[account].printAccount()
        

class Wallet():
    def __init__(self):
        self.accounts = {}
        self.balance = 0
    
    def addPaymentMethod(self, carrierName, credentials):
        responseFromCarrier = carrierDictionary[carrierName].getAccountBalance(credentials)
        if responseFromCarrier[0] == True:
            tmp = Account(credentials[0], credentials[1], carrierName, responseFromCarrier[1])
            self.accounts[credentials[0]] = tmp
            #print('Account added successfully.')

    def printPaymentMethods(self):
        c = 0
        for account in self.accounts:
            c += 1
            acc = self.accounts[account]
            response = carrierDictionary[acc.carrierName].getAccountBalance((acc.ID, acc.password))
            if response[0] != False:
                self.accounts[account].balance = response[1]
                print(f"{c}. {self.accounts[account].carrierName} \nBalance: {self.accounts[account].balance}")
            else:
                print("Connection with bank failed.")

# Print every account of every carrier
def printAllAccountsInAllCarriers():
    for carrier in carrierDictionary:
        carrierDictionary[carrier].printAllAccounts()
        print()