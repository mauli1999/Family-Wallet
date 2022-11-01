class BankAccount:
    def __init__(self, role, amount):
        self.role = role
        self.amount = amount

    # Function to subtract money from the bank account balance
    def withdraw_bank_account(self, money):
        self.amount -= money
        print("Your new bank_account balance is:", self.amount)

    # Function to add money to the bank account balance
    def deposit_bank_account(self, money):
        self.amount += money
        print("Your new bank_account balance is:", self.amount)

    # Function to view the bank account balance
    def view_bank_account_balance(self):
        print("This is your current bank_account balance:", self.amount)
