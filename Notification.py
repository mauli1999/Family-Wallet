class Notification:
    messages = []
    notify = []
    transaction = []
    requests = []
    list_transfer_request = []
    accept = []
    reject = []
    request_count = 0
    dict_requests = {}
    dict_transfer_requests = {}
    dict_permissions = {}
    accepted_permissions = []
    rejected_permissions = []

    # Method to receive message when wallet balance is 0
    @classmethod
    def receive_messages(cls, message):
        cls.messages.append(message)

    # Method to return the messages to the parents
    @classmethod
    def return_messages(cls):
        return cls.messages

    # Method to receive notification when wallet balance is less than 100
    @classmethod
    def receive_notifications(cls, notify):
        cls.notify.append(notify)

    # Method to return the notifications to the parents
    @classmethod
    def return_notifications(cls):
        return cls.notify

    # Method to append the transaction list
    @classmethod
    def add_transactions(cls, Name, amount, purpose, timestamp):
        cls.transaction.append(Name)
        cls.transaction.append(amount)
        cls.transaction.append(purpose)
        cls.transaction.append(timestamp)

    # Method to return the transaction list to the parents
    @classmethod
    def view_transactions(cls):
        return cls.transaction

    # Method to receive the overpayment requests from the children and return them the request number
    @classmethod
    def receive_request(cls, request):
        cls.request_count += 1
        cls.dict_requests[cls.request_count] = request
        
        return cls.request_count

    # Method to return the requests to the parents
    @classmethod
    def view_request(cls):
        return cls.dict_requests

    # Method to receive the accepted and rejected requests from the parents
    @classmethod
    def review_request(cls, accepted_req, rejected_req):
        cls.accept = accepted_req
        cls.reject = rejected_req

        # Removes the reviewed requests from dictionary so that parents don't get any pending request notification
        for i in cls.accept:
            cls.dict_requests.pop(int(i))
            cls.request_count -= 1
            
        for j in cls.reject:
            cls.dict_requests.pop(int(j))
            cls.request_count -= 1

    # Method to return the accepted and rejected requests to the children
    @classmethod
    def get_req_status(cls):
        return cls.accept, cls.reject

    # Method to receive the transfer requests from the mother
    @classmethod
    def transfer_request(cls, req):
        cls.list_transfer_request = req

    # Method to return the transferred requests to the father
    @classmethod
    def get_transfer_request(cls):
        for i in cls.list_transfer_request:
            req_num = i
            
            cls.dict_transfer_requests[req_num] = cls.dict_requests[req_num]
            cls.dict_transfer_requests.pop(int(i))
        return cls.dict_transfer_requests

    # Method to receive the extra transaction permission requests from the children
    @classmethod
    def permit_request(cls, permit, name):
        cls.dict_permissions[name] = permit

    # Method to return the permission requests to the parents
    @classmethod
    def view_permission(cls):
        return cls.dict_permissions

    # Method to receive the accepted and rejected permission requests from the parents
    @classmethod
    def review_permission(cls, accepted_req, rejected_req):
        cls.accepted_permissions = accepted_req
        cls.rejected_permissions = rejected_req
        
        for i in cls.accepted_permissions:
            cls.dict_permissions.pop(i)
            
        for j in cls.rejected_permissions:
            cls.dict_permissions.pop(j)

    # Method to return the accepted and rejected permission requests to the children
    @classmethod
    def get_per_status(cls):
        return cls.accepted_permissions, cls.rejected_permissions
