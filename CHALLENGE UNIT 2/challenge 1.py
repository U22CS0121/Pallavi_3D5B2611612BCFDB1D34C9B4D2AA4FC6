class bankAccount:

  def __init__(self, account_number, Account_holder_name,initial_balance=0.0):
    self.__Account_number = account_number
    self.__account_holder_holder_name = Account_holder_name
    self.__account_balance =initial_balance

def deposit(self, amount):
  if amount >0:
    self.__account_balance += amount
    print("Deposied ₹{}. new balance: ₹{}".format(amount,self.__account_balance))
  else:
    print("invalid deposit amount. please deposit a positive amount.")

  def withdraw(self,amount):
    if amount > 0 and amount <=self.__account_balance:
      self.__account_balance -= amount
      print("withdrew ₹{}. new balance: ₹{}".format(amount,self.__account_balance))
      
  else:
    Print("Invalid withdrawal amount or insufficient balance.")
   
  def display_balance(self):
  print("Account balance for {} (Account #{}): ₹{}".format( 
    self.__account_holder_name,
    Self.__account_number, self._account_balance))


# Create an instance of the bankaccount class
account = bankAccount(account_number="123456789",
                     account_holder_name="hari prabu",
                     initial_balance=5000.0)

# Test deposit and withdrawal functionality
account.display_balance()
#account.deposit(500.0)
#account.withdraw(200.0)
#account.display_balanace()