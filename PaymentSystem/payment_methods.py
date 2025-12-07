from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Mpesa(PaymentMethod):
    def pay(self, amount):
        return f"Payment of KES {amount} completed via M-Pesa."

class Card(PaymentMethod):
    def pay(self, amount):
        return f"Payment of KES {amount} completed using Credit/Debit Card."


class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Payment of KES {amount} completed via PayPal."