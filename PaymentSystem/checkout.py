from payment_methods import Mpesa, Card, PayPal
from receipt_generator import generate_receipt

def checkout(payment_method, amount,currency):
    message = payment_method.pay(amount, currency)

    # Log transaction
    with open("transactions.txt", "a") as f:
        f.write(message + "\n")

    # PDF Receipt
    receipt_path = generate_receipt(
        transaction_message=message,
        amount=amount,
        currency=currency,
        method_name=payment_method.__class__.__name__
    )
    return message, receipt_path
