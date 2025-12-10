import pandas as pd
from database import SessionLocal
from models import Transaction

def load_transactions():
    db = SessionLocal()
    rows = db.query(Transaction).all()
    db.close()

    data = [{
        "ID": t.id,
        "Method": t.method,
        "Amount": t.amount,
        "Currency": t.currency,
        "Receipt": t.receipt_path,
        "Timestamp": t.timestamp
    } for t in rows]

    return pd.DataFrame(data)
