class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Enter a valid amount to deposit.")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            self.__balance = self.__balance  # No change to balance
            return False
        else:
            self.__balance -= amount
            return True
            
    def display_balance(self):
        print(f"Current Balance: ${self.__balance :.2f}")
