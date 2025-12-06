class Payment:
    def pay(self, amount):
        pass

class Mpesa(Payment):
    def pay(self, amount):
        return f"Paid {amount} via M-Pesa."

class Card(Payment):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card."