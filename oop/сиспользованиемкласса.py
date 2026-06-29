class PaymentMethod:
    def process(self, amount, points_available=0):
        raise NotImplementedError

class CardPayment(PaymentMethod):
    def process(self, amount, points_available=0):
        return amount

class CashPayment(PaymentMethod):
    def process(self, amount, points_available=0):
        return round(amount, 2)

class PointsPayment(PaymentMethod):
    def process(self, amount, points_available=0):
        if points_available >= amount:
            return 0
        return amount - points_available

class Order:
    def __init__(self, order_data, reserv):
        self.sum = order_data["sum"]
        self.reserv = reserv

    def calculate_total(self):
        if self.reserv == 0:
            return "Товар закончился"

        if self.sum >= 5000:
            discount = self.sum / 10
            return self.sum - discount
        return self.sum  # без скидки, но сумма всё равно валидна
    
order = Order({"sum": 6000}, reserv=10)
total = order.calculate_total()
final = CardPayment().process(total)