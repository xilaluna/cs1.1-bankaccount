class BankAccount:
    """
    initializes a users bank account and actions.
    """

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Amount Withdrawn: ${amount}')
        else:
            self.balance -= 10
            print(f'Insufficient funds')

    def get_balance(self):
        print(f'You have a balance of {self.balance}')
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += round(interest, 2)

    def print_receipt(self):
        print(f'{self.full_name}\n Account No: {self.account_number}\n Routing No: {self.routing_number}\n Balance: {self.balance}')
