class RdAccount:

    def __init__(self, first_name, last_name, pin, phone_number, initial_deposit):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__pin = pin
        self.__phone_number = phone_number
        self.__balance = initial_deposit
        self.__account_number = "0026101227"
        self.__ZERO = 0

    def deposit(self, deposit_amount):
        self.__validate_amount(deposit_amount)
        self.__balance += deposit_amount

    def withdraw(self, withdrawal_amount, pin):
        self.__validate_pin(pin)
        self.__validate_amount(withdrawal_amount)
        self.__validate_amount_is_less_than_balance(withdrawal_amount)
        self.__balance -= withdrawal_amount

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def check_account_balance(self, pin):
        self.__validate_pin(pin)
        account_details = f"{self.__first_name} {self.__last_name}\n" \
                          f"{self.__account_number}\n" \
                          f"N{self.__balance}"
        return account_details

    def __validate_amount(self, amount):
        is_amount_valid = amount < self.__ZERO
        if is_amount_valid:
            self.__raise_exception("Amount cant be negative value")

    def __validate_pin(self, pin):
        is_pin_invalid = self.__pin != pin
        if is_pin_invalid:
            self.__raise_exception("Incorrect pin")

    def __validate_amount_is_less_than_balance(self, withdrawal_amount):
        is_withdrawal_amount_less_than_balance = self.__balance < withdrawal_amount
        if is_withdrawal_amount_less_than_balance:
            self.__raise_exception("Insufficient balance")

    def __raise_exception(self, prompt):
        raise Exception(prompt)


account = RdAccount("ret", "max", "1111", "0703100567", 5000)

print(account.check_account_balance("1111"))

account.deposit(2000)

account.withdraw(5000, "1111")

print(account.check_account_balance("1111"))
