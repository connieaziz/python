from datetime import datetime
class Account:
    def __init__(self,firstname,lastname,balance,loan):
        self.firstname=firstname
        self.lastname=lastname
        self.balance=0
        self.deposits=[]
        self.withdrawals=[]
        self.loan=0
    
    def welcome(self):
        return "Dear {} {},welcome,your balance is {}".format(self.firstname,self.lastname,self.balance)
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        time = datetime.now()
        object={"time":time, "amount":amount}
        self.deposits.append(object)
        return "Hello {} {},your balance is {}".format(self.firstname,self.lastname,amount)
    
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance=self.balance-amount
            time = datetime.now()
            object ={"time":time, "amount":amount}
            self.withdrawals.append(object)
            return "Dear {} {},you have withdrawn {}".format(self.firstname,self.lastname,amount)
        else:
            return "Dear {} {},you have insufficient balance to withdraw {}".format(self.firstname,self.lastname,amount)
    
    def showbalance(self):
        showbalance=self.showbalance
        return "Hello {} {},current balance is {}".format(self.firstname,self.lastname,self.balance)
    
    def show_deposits(self):
        for deposit in self.deposits:
            time = deposit["time"]
            formated_time = time.strftime("%c")
            amount = deposit["amount"]
            print("On {} you deposited {}".format(formated_time,amount))
    
    def show_withdrawals(self):
        for withdraw in self.withdrawals:
            time = withdraw["time"]
            formated_time = time.strftime("%c")
            amount = withdraw["amount"]
            print("On {} you withdrew {}".format(formated_time,amount))

    def give_loan(self,amount):
    	len(self.deposits)>=5
    	Amount <total/3 of_total_deposits
    		total=0
    		for deposit in self.deposits:
    			amount=deposit["amount"]
    			total+ = amount
    			self.amount.append (total)

    def pay_loan(self,amounts):
    	diff = amount,sum
    	loan=0
    	self.deposit(diff)

