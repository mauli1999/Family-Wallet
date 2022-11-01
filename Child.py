from Notification import Notification
from Wallet import Wallet


class Child:
    req_num_amt = {}
    per_num_amt = {}

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.count = 0
        self.amount = 0
        self.notification = Notification()
        self.wallet = Wallet()

    # Counts the child's transaction number
    def set_count(self):
        self.count += 1

    # Returns the child's transaction number
    def get_count(self):
        return self.count

    # Adds up the child's transaction amount
    def set_amount(self, amt):
        self.amount += amt

    # Returns the child's transaction amount
    def get_amount(self):
        return self.amount

    # Appends the amount and purpose to dictionary when request is sent to the parents
    @classmethod
    def append_req_num_amt(cls, req_num, req_amt, purpose):
        cls.req_num_amt[req_num] = req_amt, purpose

    # Returns the appended amount and purpose from the dictionary when request is accepted
    @classmethod
    def return_req_num_amt(cls):
        return cls.req_num_amt

    # Sends request to parents when total amount associated with child's profile or requested amount exceeds $50
    def send_request(self, name, purpose, req_amount):

        request = 'Overpayment request from ' + name + ' for $' + str(req_amount) + ' to purchase ' + purpose

        # Sends the overpayment request to the notification class and gets back the request number
        request_number = self.notification.receive_request(request)

        # Calls the class method to append the request number, amount and purpose to the dictionary
        Child.append_req_num_amt(request_number, req_amount, purpose)
        msg = 'Your request has successfully sent. Your request number is:' + str(request_number)

        return msg

    # Function which lets the child know whether their overpayment request has been accepted or rejected
    def request_status(self, obj, name):

        # Gets the accepted or rejected request number from the notification class
        accepted_req, rejected_req = self.notification.get_req_status()
        req_num = int(input('Please enter your request number'))
        if req_num in accepted_req:
            print('your request has been accepted')

            # Returns requested amount and purpose of the transaction
            return_value = Child.return_req_num_amt()
            override_amt, purpose = return_value[req_num]

            print('Do you want to proceed with your transaction of $' + str(override_amt) + 'to purchase' + purpose)
            ans = str(input('Enter Y for Yes or N for No'))

            if ans == 'Y':
                # Calls the pay function of class Wallet to proceed with the transaction
                obj.wallet.pay('Child', override_amt, name, purpose)

        elif req_num in rejected_req:

            print('sorry, your request has been accepted')

        else:

            print('No response yet,please wait for it')

    # Appends the amount to dictionary when permission request is sent to the parents
    @classmethod
    def append_permit_amt(cls, name, per_amt, purpose):
        cls.per_num_amt[name] = per_amt, purpose

    # Returns the appended amount from the dictionary when permission request is accepted
    @classmethod
    def return_permit_amt(cls):
        return cls.per_num_amt

    # Sends permission request to parents when total count of transactions associated with child's profile exceeds 1
    def ask_permission(self, name, purpose, per_amount):

        per_req = 'Transaction permission request ' + name + ' for $' + str(per_amount) + ' to purchase ' + purpose

        # Sends the extra transaction permission request to the notification class
        self.notification.permit_request(per_req, name)

        # Calls the class method to append the requested amount and purpose to the dictionary
        Child.append_permit_amt(name, per_amount, purpose)
        msg = 'Your permission request has been sent'

        return msg

    # Function to let the child know whether the permission request for extra transaction has been accepted or rejected
    def permission_status(self, obj, name):

        # Gets the accepted or rejected request number from the notification class
        accepted_req, rejected_req = self.notification.get_per_status()

        if name in accepted_req:
            print('your request has been accepted')

            # Returns requested amount of the transaction
            return_value = Child.return_permit_amt()
            override_amt, purpose = return_value[name]

            print('Do you want to proceed with your transaction of $' + str(override_amt) + 'to purchase' + purpose)
            ans = str(input('Enter Y for Yes or N for No'))

            if ans == 'Y':
                # Calls the pay function of class Wallet to proceed with the transaction
                obj.wallet.pay('Child', override_amt, name, obj)

        elif name in rejected_req:

            print('sorry, your request has been rejected')

        else:

            print('No response yet,please wait for it')

    # Function to check child's eligibility for the transaction
    def check_eligibility(self, name, purpose, requested_amount):

        # Gets the total number of transaction count associated with child's object
        transaction_count = self.get_count()

        # Gets the total amount associated with child's object
        amount = self.get_amount()

        # Prohibits the blocked users from proceeding with the transaction
        if name in Wallet.block_list:
            msg = 'your access to wallet has been blocked!'

            return msg

        if transaction_count <= 1 and amount <= 50:

            return 'eligible'

        elif transaction_count <= 1 and amount > 50:
            print('amount limit exceeding, request for overpayment')
            print('Do you want to proceed with overpayment request?')

            ans = str(input('Enter Y for Yes Or R to return'))

            if ans == 'Y':
                # Sends overpayment request to the parents
                msg = self.send_request(name, purpose, requested_amount)

                return msg

            else:
                return

        elif transaction_count == 2:
            print('transaction limit exceeding, need to ask parents for permission')
            print('Do you want to proceed with permission request?')

            ans = str(input('Enter Y for Yes Or R to return'))

            if ans == 'Y':
                # Sends permission request to the parents
                msg = self.ask_permission(name, purpose, requested_amount)

                return msg

            else:
                return

        else:
            msg = 'transaction limit exceeded, cannot use the wallet'

            return msg
