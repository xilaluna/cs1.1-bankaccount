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
