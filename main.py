# Выполненное домашнее задание Свойства хорошего кода. Abstraction, Composition, Coupling, Cohesion
# Также домашнее задание выполнено в PyCharm C:\Users\Admin\PycharmProjects\Abstraction_Composition_Coupling_Cohesion
# Также домашнее задание выполнено в GIt HUB 

import math
from random import random

class Bank:
    def __init__(self):
        self.accounts = {}


#Класс Клиент - только личные данные
class Customer(Bank):
    def __init__(self, name: str, address: str, bank):
        self.name = name
        self.address = address
        self.bank = bank


#Класс Account - личные данные + баланс счета + генерация номер аккаунта + открытие аккаунта
class Account():
    def __init__(self, customer: Customer, name="", address="", account_number=0, bank="", balance=0):
        self.account_number = account_number
        self.name = name
        self.address = address
        self.bank = bank
        self.balance = balance
        pass


    def open_account(self, customer: Customer, bank):
        account_number = self._generate_account_number()
        print(account_number)
        # Надо разделить создание номера акаунта и создание самого аккаунта - но можно не делить!!!!
        self.account_number = account_number
        self.name = customer.name
        self.address = customer.address
        bank.accounts[account_number] = account_number
        return Account


    def _generate_account_number(self) -> int:
        return math.floor(random() * 1000000)

# Класс банковских операций - банковские операции
class Bank_operation():
    def __init__(self, account: Account):
        pass

    def deposit(self, account: Account, amount: float):
        account.balance += amount

    def withdraw(self, account: Account, amount: float):
        if amount <= account.balance:
            account.balance -= amount
        else:
            raise ValueError("Суммы на счете не достаточно для снятия!!!")


    def get_account(self, account_number: int, account: Account, bank) -> Account:
        if account_number in bank.accounts:
            return account
        else:
            raise ValueError("Account not found")

def banking_scenario():
    # Создаем экземпляр класса Bank
    bank = Bank()
    # Создаем два экземпляра обьекта  Customer - Боба и Алису
    customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1", bank)
    customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5", bank)
    # Alice opens an account and deposits some money
    # Создаем два экземпляра обьекта  Customer - Боба и Алису
    alice_account = Account(customer1)
    bob_account = Account(customer2)

    # Проверка
    print(f' customer1 = {customer1.name, customer1.address, customer1.bank}')
    print(f' customer2 = {customer2.name, customer1.address, customer1.bank}')

    # Создаем номер аккаунта клиенту в банке
    alice_account2 = alice_account.open_account(customer1, bank)
    bob_account2 = bob_account.open_account(customer2, bank)

    # Проверка
    # print(f' alice_account = {alice_account}')
    print(f' alice_account_new = {alice_account.account_number, alice_account.name, alice_account.address, alice_account.bank}')
    # print(f' bob_account = {bob_account}')
    print(f' bob_account_new = {bob_account.account_number, bob_account.name, bob_account.address, bob_account.bank}')

    # Проводим банковские операции
    # Операция депозита - не стал делать сразу первый взнос при открытие счета, так как предположил,
    # что счет можно открыть а вот деньги класть при открытие счета не обязательно
    bank_operation = Bank_operation(alice_account)
    bank_operation.deposit(alice_account, amount=150.0)

    bank_operation = Bank_operation(bob_account)
    bank_operation.deposit(bob_account, amount=78953.0)

    # Проверка
    print(f'баланс счета Алисы =  {alice_account.balance}')
    print(f'баланс счета Боба =  {bob_account.balance}')

    # Alice withdraws some money from her account
    # Алиса снимает немного денег со счета
    bank_operation = Bank_operation(alice_account)
    #  При снятие со счета проверяем достаточность средств и обрабатываем ошибоки
    try:
        bank_operation.withdraw(alice_account, amount= 34.0)
    except ValueError as e:
        print(e)  # Суумы на счете не достаточно для снятия!!!
    print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 300.0

    # Bank retrieves Alice's account using the account number
    # Проверка
    print(f' bank.accounts =  {alice_account.account_number}')
    print(f' bank.accounts =  {bank.accounts}')

    try:
        retrieved_account = bank_operation.get_account(alice_account.account_number,alice_account, bank)
        print(f' retrieved_account1 =  {retrieved_account}')
    except ValueError as e:
        print(f' retrieved_account2 =  {retrieved_account}')
        print(e)  # Account not found
    print(f"Account {retrieved_account.account_number} by {retrieved_account.name} ({retrieved_account.address}), balance {retrieved_account.balance}") # Account XXXXXX by Alice (Moscow, Stremyannyi per, 1), balance 300.0


banking_scenario();
