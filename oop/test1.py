class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    @property
    def owner(self):
        return self.__owner
    
    @property
    def balance(self):
        return self.__balance
    
    @owner.setter
    def owner(self, new_owner):
        if new_owner == '':
            print('Имя владельца не должно быть пустым')
        else:
            self.__owner = new_owner

    def deposit(self, amount):
        if amount <= 0:
            return 'Пополнение не должно быть отрицательным'
        else:
            self.__balance += amount
            return f'Успешное пополнение на {amount} рублей'
        
    def withdraw(self, amount):
        if amount > self.__balance:
            return 'Нечего снимать'
        else:
            self.__balance -= amount
            return f'Успешное снятие на {amount} рублей\nБаланс: {self.__balance} рублей'
        
    def get_balance(self):
        return f'На балансе {self.__balance} рублей'
    
        

acc = BankAccount('Александр', 1000)
print(acc.deposit(500))
print(acc.balance)

acc.owner = 'Дима'
print(acc.owner)

acc.owner = ''
print(acc.owner)