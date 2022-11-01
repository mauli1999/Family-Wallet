from BankAccount import BankAccount
from Mother import Mother
from Notification import Notification
from Wallet import Wallet


class Father(Mother):

    def __init__(self, name, role):
        super().__init__(name, role)
        self.name = name
        self.role = role
        self.account = BankAccount('Father', 1000)
        self.notification = Notification()
        self.wallet = Wallet()

    # Function is used to block the user form accessing the wallet
    # This function overrides the class Mother block_user()
    def block_user(self):
        name = str(input('Enter the name to be blocked'))
        self.wallet.block(name)

    # Function to add money to the wallet from the users bank account
    # This function overrides the class Mother deposit_wallet()
    def deposit_wallet(self, amount):
        self.account.view_bank_account_balance()
        # Subtracts the amount from bank account balance of the Fathers account
        self.account.withdraw_bank_account(amount)
        # Adds the amount to the wallet balance
        result_amount = Wallet.add_balance(amount)
        print("Your new wallet balance is:", result_amount)

    # Function to add money to the users bank account from the wallet
    # This function overrides the class Mother withdraw_wallet()
    def withdraw_wallet(self, amount):
        # Subtracts the amount from the wallet balance
        result_amount = Wallet.subtract_balance(amount)
        # Adds the amount to the bank account balance
        self.account.deposit_bank_account(amount)
        print("Your new wallet balance is:", result_amount)

    # Function shows the total requests count including the transferred requests made by mother
    # This function overrides the class Mother request_count()
    def request_count(self):
        # Fetches the requests from notification class
        dic_1 = self.notification.view_request()
        # Fetches the transferred requests from notification class
        dic_2 = self.notification.get_transfer_request()
        dic = {**dic_1, **dic_2}
        if len(dic) == 0:
            print('No new requests')
            return
        else:
            print('You have ' + str(len(dic)) + ' new requests to be reviewed')

    # Function to review request. They can either be accepted or rejected.
    # This function overrides the class Mother view_requests()
    def view_requests(self):
        # Fetches the requests from notification class
        dic_1 = self.notification.view_request()
        # Fetches the transferred requests from notification class
        dic_2 = self.notification.get_transfer_request()
        dic = {**dic_1, **dic_2}
        accepted_req = []
        rejected_req = []
        print(dic)
        k = len(dic)

        while k != 0:
            accept = int(input('Enter the request number you approve of, Press 0 for None:'))
            if accept != 0:
                accepted_req.append(accept)
                k -= 1
                if k == 0:
                    break
            reject = int(input('Enter the request number you rejected, Press 0 for None::'))
            if reject != 0:
                rejected_req.append(reject)
                k -= 1
                if k == 0:
                    break
        # Returns the accepted and rejected requests number to the notification class
        self.notification.review_request(accepted_req, rejected_req)
