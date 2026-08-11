class Atm:
    def __init__(self,name, amount, balance, pin):
        self.name=name
        self.amount=amount
        self.pin=pin
        self.balance=balance
    def set_name(self, name):
        self.name=name
    def get_name(self):
        return self.name
    def set_amount(self,amount):
        self.amount=amount
    def get_amount(self):
        return self.amount
    def set_pin(self, pin):
        self.pin=pin
    def set_balance(self, balance):
        self.balance=balance
        
    def get_balance(self):
        return self.balance
    
    
    def check_pin(self, enteredPin):
        return enteredPin==self.pin
    
    def deposit(self, amount):
        self.balance += amount
        print(f"You successfully deposited {amount}. \nYour new balance is {self.balance}")
    
    def withdraw(self, amount):
        
        if self.balance< amount:
            print(f"Insufficient balance {amount}")
        else:
            self.amount> amount
            print("You have successfully withdrawl {amount}. \n New balance{self.amount}")

            
atm1=Atm("Adolphe",1,4000,1234)
pin=int(input("Enter your pin: "))
    
    
print("PIN matches") if atm1.check_pin(pin) else print("PIN don't match")

print("1 depost")
print("2 withdraw")
print("3 Exit")

option = int(input("Choose btn (1,2,3):)"))


match option:
    case(1):
        print("deposit")
        amount=int(input("Enter amount to depost: "))
        atm1.deposit(amount)
    case(2):
        print("withdraw")
        amount=int(input("Enter the amount to withdraw: "))
    case(3):
        print("Exit")       
