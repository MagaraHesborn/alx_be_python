class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
            self.__balance += amount
    
    def withdraw(self, amount):
        if amount > self.__balance:
            return False
        else:
            self.__balance -= amount
            return True
            
    def display_balance(self):
        print(f"Current Balance: ${self.__balance :.2f}")
