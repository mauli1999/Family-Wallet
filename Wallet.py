import datetime

from Notification import Notification

e = datetime.datetime.now()


class Wallet:
    balance = 1000.0
    transactions = []
    block_list = []

    def __init__(self):
        self.transactions = []
        self.notification = Notification()

    # Function to view wallet balance
    @staticmethod
    def view():
        print("This is your current wallet balance: $", Wallet.balance)

    # Function to add amount to the wallet balance
    @classmethod
    def add_balance(cls, amount):
        Wallet.balance += amount
        return Wallet.balance

    # Function to subtract amount from the wallet balance
    @classmethod
    def subtract_balance(cls, amount):
        Wallet.balance -= amount
        return Wallet.balance

    # Function to block the user.The names are appended by the parents.
    @classmethod
    def block(cls, name):
        cls.block_list.append(name)

    # Function to check the wallet balance. It send notification to the parents when balance is less than 100
    def check_balance(self):
        if self.balance < 100:
            notify = 'Balance is: ' + str(Wallet.balance) + ' Please deposit money soon'
            self.notification.receive_notifications(notify)

    # Function is used to pay money for the transaction
    def pay(self, Role, amount, Name, purpose):

        if Name in Wallet.block_list:
            msg = 'your access to wallet has been blocked!'

            return msg

        if Wallet.balance == 0:
            print('Balance is')
            print(Wallet.balance)
            print('transaction declined')
            if Role == 'Child':
                message = 'money deposit requested from ' + Name

                # Sends message to parents regarding 0 balance
                self.notification.receive_messages(message)
                return
            else:
                print('please deposit money')
                return

        # Obstructs user from using wallet when requested amount is greater than wallet balance
        elif amount > Wallet.balance:
            print('Insufficient balance, transaction declined')

        else:
            Wallet.subtract_balance(amount)
            timestamp = e.strftime("%Y-%m-%d %H:%M:%S")

            # Appends the transaction list
            self.notification.add_transactions(Name, amount, purpose, timestamp)
            self.view()
