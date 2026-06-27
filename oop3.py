class Discount:
    def __init__(self,amount):
        self.amount = amount
    
    def return_amount(self):
        raise NotADirectoryError
    
class PercentDiscount(Discount):
    def __init__(self, amount, skidka):
        super().__init__(amount)
        self.skidka = skidka

    def apply(self):
        total = self.amount - (self.amount * self.skidka / 100)
        return total
    
    def __str__(self):
        return f'Скидка {self.skidka}%'
    


    
class FixedDiscount(Discount):
    def __init__(self, amount, fixed_sum):
        super().__init__(amount)
        self.fixed_sum = fixed_sum

    def apply(self):
        total = self.amount - self.fixed_sum
        return max(total, 0)
    
    def __str__(self):
        return f'Фиксированная скидка {self.fixed_sum}P'


class NoDiscount(Discount):
    def __init__(self, amount):
        super().__init__(amount)

    def apply(self):
        return self.amount
    
    def __str__(self):
        return 'Без скидки'
    
discounts = [PercentDiscount(6000, 15), FixedDiscount(6000, 500), NoDiscount(6000)]
for d in discounts:
    print(d, "->", d.apply())
