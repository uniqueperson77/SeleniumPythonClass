#acnt num, acntholder name, balance,address,age
#check balance, deposit, withdraw

class Bank:
    def __init__(self,acnt_num,name,address,age):
        self.number = acnt_num
        self.name = name
        self.balance = 5000
        self.address = address
        self.age = age
        self.min_bal = 2000
        print("This is executed at default.")
        self.check_balance()

    def __str__(self):
        return str(self.number)

    def check_balance(self):
        print("Current Balance: INR- {}".format(self.balance))
        return self.balance

    def deposit(self,amount):
        curr_bal = self.check_balance()
        self.balance = curr_bal + amount
        print("Balance: INR- {}".format(self.balance))
        return self.balance

    def withdraw(self,amount):
        curr_bal = self.check_balance()
        avail_to_withdraw = curr_bal-self.min_bal
        if amount>avail_to_withdraw:
            print("No sufficeient balance to withdraw as you need to maintain min bal of {}".format(self.min_bal))
        else:
            self.balance = curr_bal - amount
            print("Amount of {} INR has been withdrawn".format(amount))

        self.check_balance()

    def fixed_deposit(self,amount,tenure):
        pass        #business logic

class Bank1:
    pass

class Bank2:
    pass


# isha = Bank(123456,"Isha","India",25)
# # print(type(isha), isha)
# isha.check_balance()
# # val = isha.deposit(3000)
# # isha.withdraw(15000)
# # isha.check_balance()
# #
# isha.withdraw(4000)