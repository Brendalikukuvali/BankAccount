 class BankAccount:
   
    def __init__(self, first_name, last_name, phone_Number, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_Number = phone_Number
        self.bank = bank
        self.balance = 0
        self.withdrawal_statement = []
        self.deposit_statement = []
        self.loan_balance = 0

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name, self.phone_Number, self.bank)
        return name

    def deposit(self, amount):
      
      if amount <= 0:
               
          print("You cannot deposit zero or negative")
      else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))
            return 
            
            
          
    def withdraw(self, amount):
         
      if amount <= 0:
          print("You cannot withdraw zero or negative")
          
       
      elif amount > self.balance:
            print("You don't have enough balance")
      self.balance += amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p %d/%m/%Y")
            get_time = time.strftime("%H:%M%p , %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
            }
            print("Dear {} you have deposited {} at {}.Your current account balance is {}".format(self.account_name(),amount,get_time,self.balance))
            print("Dear {} ,you have deposited {} at {}.Your current account balance is {}".format(self.account_name(),amount,get_time,self.balance))

    def withdraw(self,amount):
        try:
@@ -63,7 +63,7 @@ def withdraw(self,amount):
        else:
            self.balance -= amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
@@ -73,19 +73,19 @@ def withdraw(self,amount):

    def get_balance(self):
        time = datetime.now()
        get_time = time.strftime("%H:%M%p  %d/%m/%Y")
        get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
        return "The balance for {} is {} at".format(self.account_name(), self.balance,get_time)

    def deposit_statements(self):
        for deposit in self.deposits:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p  , %d/%m/%Y")
            print("{} at {}".format(deposit(),get_time))

    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            get_time = time.strftime("%H:%M%p , ++ %d/%m/%Y")
            print("{} at {}".format(withdraw(),get_time))
             def request_loan(self, amount):
      if amount<= 0:
        print("You cannot request for loan of that amount")
        
      else: 
        self.loan = amount
        print("You have been given loan of {}".format (amount)
      
    def repay_loan(self, amount):
      if amount<= 0:
        print("You cannot repay with that amount")
      elif self.loan == 0:
        print("You don't have loan at the moment")
        elif amount > self.loan:
          print("Your loan is {}, please enter amount that is less or equal to the amount")
        else:
        print(" You have repayed your loan with {}.your loan balance is{}".format(mount))
      

    def deposit_statement(self, amount):
      self.deposit(self, amount)
      
      return self.deposit_summary.append(amount)
       
      
    
    
acc1 = BankAccount(" Brenda", "Anne", +254710456739
, " Equity")
print(acc1.phone_no)
acc1.deposit(50000)
acc1.withdraw(15000)
acc1.withdraw(1200)
acc1.deposit(4000)
acc1.deposit(2400)
acc1.lend_loan(7000)
acc1.lend_loan(20000)
acc1.pay_loan(15000) 
print(acc1.loan_balance)

print(acc1.deposit_summary) 