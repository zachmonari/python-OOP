from payment_methods import Mpesa, Card, PayPal
from receipt_generator import generate_receipt

def checkout(payment_method, amount):
    try:
        result = payment_method.pay(amount)
        print(result)
        log_transaction(result)
    except Exception as e:
        print("Payment failed:", e)

def log_transaction(message):
    with open("transactions.txt", "a") as f:
        f.write(message + "\n")