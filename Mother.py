from BankAccount import BankAccount
from Notification import Notification
from Wallet import Wallet


class Mother:

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.account = BankAccount('Mother', 1000)
        self.notification = Notification()
        self.wallet = Wallet()

    # Function will fetch transaction list from the Notification class method
    def view_transactions(self):
        # Fetches the transaction list from Notification class
        view_trans = self.notification.view_transactions()
        print(view_trans)

    # Function is used to block the user form accessing the wallet
    def block_user(self):

        name = str(input('Enter the name to be blocked'))
        if name == 'Adam':
            print('Sorry, you do not have permission to block this user')
            return
        else:
            # Updates the blocked user name through block function of the wallet class
            self.wallet.block(name)

    # Function shows the total requests count
    def request_count(self):
        # Fetches the requests from notification class
        dic = self.notification.view_request()
        if len(dic) == 0:
            print('No new requests')
            return
        else:
            print('You have ' + str(len(dic)) + ' new requests to be reviewed')

    # Function shows the total permission requests count
    def permission_count(self):
        # Fetches the permission requests from notification class
        dic = self.notification.view_permission()
        if len(dic) == 0:
            print('No new permissions')
            return
        else:
            print('You have ' + str(len(dic)) + ' new permission to be reviewed')

    # Function shows messages sent to parents when balance is 0
    def view_message(self):
        # Fetches the messages from notification class
        message = self.notification.return_messages()
        if len(message) == 0:
            print('No new messages')
            return
        print('You have new messages')
        for i in message:
            print(i)

    # Function shows notification to parents when balance is less than 100
    def view_notification(self):
        # Fetches the notifications list from notification class
        notify = self.notification.return_notifications()
        if len(notify) == 0:
            print('No new Notifications')
            return
        print('You have new Notifications')
        print(notify)

    # Function to add money to the wallet from the users bank account
    def deposit_wallet(self, amount):

        self.account.view_bank_account_balance()
        # Subtracts the amount from bank account balance of the Mothers account
        self.account.withdraw_bank_account(amount)
        # Adds the amount to the wallet balance
        result_amount = Wallet.add_balance(amount)
        print("Your new wallet balance is:", result_amount)

    # Function to add money to the users bank account from the wallet
    def withdraw_wallet(self, amount):
        # Subtracts the amount from the wallet balance
        result_amount = Wallet.subtract_balance(amount)
        # Adds the amount to the bank account balance
        self.account.deposit_bank_account(amount)
        print("Your new wallet balance is:", result_amount)

    # Function to review request. They can either be rejected, accepted or transferred to father.
    def view_requests(self):
        # Fetches the requests made by children
        dic = self.notification.view_request()
        accepted_requests = []
        rejected_requests = []
        transfer_requests = []
        print(dic)
        k = len(dic)

        while k != 0:
            accept = str(input('Enter the request number you approve of,Press 0 for None or T for transfer request:'))
            if accept != 0 and accept != 'T':
                accepted_requests.append(int(accept))
                k -= 1
                if k == 0:
                    break
            if accept == 'T':
                transfer_request_number = int(input('Enter request number to be transferred to dad'))
                transfer_requests.append(transfer_request_number)
                k -= 1
                if k == 0:
                    break
            reject = str(input('Enter the request number you rejected,Press 0 for None or T for transfer request:'))
            if reject != 0 and reject != 'T':
                rejected_requests.append(int(reject))
                k -= 1
                if k == 0:
                    break
            if reject == 'T':
                transfer_request_number = int(input('Enter request number to be transferred to dad'))
                transfer_requests.append(transfer_request_number)
                k -= 1
                if k == 0:
                    break
        # Returns the accepted and rejected requests number to the notification class
        self.notification.review_request(accepted_requests, rejected_requests)
        # Returns the transferred requests number to the notification class
        self.notification.transfer_request(transfer_requests)

    # Function to view permission request made by children. They can either be rejected or accepted
    def view_permission(self):
        # Fetches the permission requests made by children
        dic = self.notification.view_permission()
        accepted_requests = []
        rejected_requests = []
        print('These children have requested permission to use wallet for an extra transaction')
        print(dic)
        k = len(dic)

        while k != 0:
            accept = str(input('Enter name whose permission has been granted, Press 0 for None:'))
            if accept != 0:
                accepted_requests.append(accept)
                k -= 1
                if k == 0:
                    break
            reject = str(input('Enter name whose permission has been rejected, Press 0 for None:'))
            if reject != 0:
                rejected_requests.append(reject)
                k -= 1
                if k == 0:
                    break
        # Returns the name of the children whose permission requests either got accepted or rejected
        self.notification.review_permission(accepted_requests, rejected_requests)
