class BankAccountError(Exception):
    """Базовий клас для винятків, пов'язаних з банківським рахунком."""

    def __init__(self, message="Помилка банківського рахунку"):
        self.message = message
        super().__init__(self.message)

'''
class InsufficientFundsError(BankAccountError):
    """Виняток для випадку недостатньої кількості коштів на рахунку."""

    def __init__(self, account_number, balance, amount):
        self.account_number = account_number
        self.balance = balance
        self.amount = amount
        self.message = f"Рахунок {account_number}: Недостатньо коштів ({balance}) для зняття {amount}."
        super().__init__(self.message)
'''

class NegativeDepositError(BankAccountError, ValueError):
    """Виняток для випадку негативного внесення на рахунок."""

    def __init__(self, account_number, amount):
        self.account_number = account_number
        self.amount = amount
        self.message = f"Рахунок {account_number}: Негативне внесення ({amount}). Сума повинна бути додатною."
        
        # BankError.__init__(self, self.message)
        super().__init__(self.message)
        # ValueError.__init__(self, self.message)
        # super(ValueError, self).__init__(self.message)



'''
# Моделюємо помилку під час зняття коштів
try:
    raise InsufficientFundsError(account_number="123456789", balance=100, amount=150)
except InsufficientFundsError as e:
    print(f"Помилка типу InsufficientFundsError: {e}")
    print(f"Баланс: {e.balance}")
except BankError as e:
    print(f"Помилка типу BankError: {e}")
'''


class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0
    def __repr__(self):
        return f"<BankAccount {self.account_number!r}, balence={self.balance}>"
    def deposit(self, amount):
        if amount <= 0:
            raise NegativeDepositError(account_number=self.account_number, amount=amount)
        self.balance += amount    

a = BankAccount('01-001')
# a.deposit(-10)

try:
    a.deposit(-10)
except NegativeDepositError as e:
    print(f"Помилка типу NegativeDepositError: {e}")
    print(f"Сума: {e.amount}")
#except BankError as e:
    #print(f"Помилка типу BankError: {e}")
except ValueError as e:
    print(f"Помилка типу ValueError: {e}")
#except Exception as e:
    #print(f"Інша помилка: {e}")
