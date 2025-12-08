from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount,currency):
        pass

class Mpesa(PaymentMethod):
    def pay(self, amount,currency):
        return f"Payment of  {currency}. {amount} completed via M-Pesa."

class Card(PaymentMethod):
    def pay(self, amount,currency):
        return f"Payment of  {currency}. {amount} completed using Credit/Debit Card."


class PayPal(PaymentMethod):
    def pay(self, amount,currency):
        return f"Payment of  {currency}. {amount} completed via PayPal."