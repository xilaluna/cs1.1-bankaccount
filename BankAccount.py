class BankAccount:
    """
    initializes a users bank account and actions.
    """

    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.__account_number = account_number
        self.__routing_number = routing_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f'Amount Deposited: ${amount}')

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f'Amount Withdrawn: ${amount}')
        else:
            self.__balance -= 10.00
            print(f'Insufficient funds')

    def get_balance(self):
        print(f'You have a balance of {self.__balance}')
        return self.__balance

    def add_interest(self):
        interest = self.__balance * 0.00083
        self.__balance += round(interest, 2)

    def print_receipt(self):
        print(
            f' {self.full_name}\n Account No: ****{str(self.__account_number)[4:]}\n Routing No: {self.__routing_number}\n Balance: {self.__balance}')


xila_luna = BankAccount('Xila Luna', 12345678, 87654321, 100)
xila_luna.deposit(20.50)
xila_luna.withdraw(10)
xila_luna.add_interest()
xila_luna.get_balance()
xila_luna.print_receipt()
