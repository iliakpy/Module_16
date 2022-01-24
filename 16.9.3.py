"""
В проекте «Дом питомца» скоро появится новая услуга:
электронный кошелек. То есть система будет хранить данные
о своих клиентах и об их финансовых операциях.
Вам нужно написать программу, обрабатывающую данные,
и на выходе в консоль получить следующее:
Клиент "Иван Петров". Баланс: 50 руб.
"""

class Wallet:
    def __init__(self, name="", balance=0):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Customer: {self.name}, Balance: {self.balance}"

n = str(input("ВВедите Имя и Фамилию: "))
s = int(input("Введите сумму: "))

Guest_1 = Wallet(n, s)
print(Guest_1)