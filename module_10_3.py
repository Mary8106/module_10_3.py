from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(1, 101):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            tranc = randint(50, 500)
            self.balance += tranc
            print(f'Пополнение: {tranc}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for j in range(1, 101):
            tranc = randint(50, 500)
            print(f'Запрос на {tranc}')
            if tranc <= self.balance:
                self.balance -= tranc
                print(f'Снятие: {tranc}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')