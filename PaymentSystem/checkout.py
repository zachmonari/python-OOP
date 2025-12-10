from database import SessionLocal
from models import Transaction
from receipt_generator import generate_receipt

def checkout(payment_method, amount, currency):

    message = payment_method.pay(amount, currency)
    receipt = generate_receipt(
        transaction_message=message,
        amount=amount,
        currency=currency,
        method_name=payment_method.__class__.__name__
    )

    # Save to DB
    db = SessionLocal()
    tx = Transaction(
        method=payment_method.__class__.__name__,
        amount=amount,
        currency=currency,
        receipt_path=receipt
    )
    db.add(tx)
    db.commit()
    db.refresh(tx)
    db.close()

    return message, receipt
