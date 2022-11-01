from Child import Child
from Father import Father
from Mother import Mother


class User:
    @staticmethod
    def user_role():
        """
        Validates the user's identification using the name he enters in the system with respect to object available
        in the system.

        :return: user's role which is associated with the object
        """
        user_role = ' '
        obj = ' '
        user_name = str(input("Enter your login credentials:"))
        if user_name == getattr(Maia, 'name'):
            obj = Maia
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Adam, 'name'):
            obj = Adam
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Max, 'name'):
            obj = Max
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Eve, 'name'):
            obj = Eve
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Sam, 'name'):
            obj = Sam
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Pam, 'name'):
            obj = Pam
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Jim, 'name'):
            obj = Jim
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Amy, 'name'):
            obj = Amy
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Cam, 'name'):
            obj = Cam
            user_role = getattr(obj, 'role')
        elif user_name == getattr(Ivy, 'name'):
            obj = Ivy
            user_role = getattr(obj, 'role')
        else:
            print('Access Denied')
            exit()
        return user_role, obj, user_name

    @staticmethod
    def purpose(user_role):
        """
        Returns the task selected by the user.
        The task menu is shown according to the user's role.

        :param user_role: Role assigned to the user
        :return: task selected by the user
        """
        if user_role == 'Father' or user_role == 'Mother':
            print("What would you like to do?")
            print("[V] View Wallet Balance")
            print("[D] Deposit Money")
            print("[W] Withdraw Money")
            print("[P] Pay using Wallet")
            print("[T] View Transactions")
            print("[O] View Request")
            print("[CP] Check Permissions")
            print("[U] Block User")
            print("[0] Exit the program ")
            task = str(input())

        else:
            print("What would you like to do?")
            print("[P] Pay using Wallet")
            print("[R] Review your Request")
            print("[C] Check permission status")
            print("[0] Exit the program ")
            task = str(input())

        return task


def main():
    # Start of the program
    print("Welcome!!")

    user = 1
    while user != 0:
        # returns user's_role and name
        user_role, obj, user_name = U1.user_role()
        check = 1
        while check != 0:
            if user_role == 'Mother' or user_role == 'Father':
                obj.wallet.check_balance()
                obj.view_notification()
                obj.view_message()
                obj.request_count()
                obj.permission_count()

            # returns the task that user selects
            intent = U1.purpose(user_role)
            if intent == '0':
                exit()
            elif intent == 'V':
                obj.wallet.view()
            elif intent == 'O':
                obj.view_requests()
            elif intent == 'D':
                amt = float(input('Enter the amount to be deposited:'))
                obj.deposit_wallet(amt)
            elif intent == 'W':
                amt = float(input('Enter the amount to be withdrawn:'))
                obj.wallet.view()
                obj.withdraw_wallet(amt)
            elif intent == 'T':
                obj.view_transactions()
            elif intent == 'U':
                obj.block_user()
            elif intent == 'R':
                obj.request_status(obj, user_name)
            elif intent == 'C':
                obj.permission_status(obj, user_name)
            elif intent == 'CP':
                obj.view_permission()
            elif intent == 'P':
                purpose = str(input('Please enter purpose for this transaction'))
                requested_amount = int(input('Please enter the amount needed for this transaction'))
                if user_role == 'Child':
                    obj.set_count()
                    obj.set_amount(requested_amount)
                    msg = obj.check_eligibility(user_name, purpose, requested_amount)
                    if msg == 'eligible':
                        obj.wallet.pay(user_role, requested_amount, user_name, purpose)
                        print('transaction completed')
                    else:
                        print(msg)

                else:
                    obj.wallet.pay(user_role, requested_amount, user_name, purpose)

            # user can exit the program or continue onto the next task
            check = int(input("Enter [0] to Exit or [1] to move on to next action"))
        # switch user or exit the program
        user = int(input("Enter [0] to Logout or [1] to continue as different user"))


if __name__ == '__main__':
    Maia = Mother('Maia', 'Mother')
    Adam = Father('Adam', 'Father')

    Max = Child('Max', 'Child')
    Eve = Child('Eve', 'Child')
    Sam = Child('Sam', 'Child')
    Pam = Child('Pam', 'Child')
    Jim = Child('Jim', 'Child')
    Amy = Child('Amy', 'Child')
    Cam = Child('Cam', 'Child')
    Ivy = Child('Ivy', 'Child')

    U1 = User()
    main()
