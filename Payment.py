class Payment:
    def pay(self, amount):
        pass

class Mpesa(Payment):
    def pay(self, amount):
        return f"Paid {amount} via M-Pesa."

class Card(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."

def checkout(payment_method: Payment):
    print(payment_method.pay(500))

checkout(Mpesa())
checkout(Card())