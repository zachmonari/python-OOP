import pandas as pd
from database import SessionLocal
from models import Transaction

def fetch_transactions():
    db = SessionLocal()
    data = db.query(Transaction).all()
    db.close()
    return pd.DataFrame([{
        "ID": d.id,
        "Method": d.method,
        "Amount": d.amount,
        "Currency": d.currency,
        "Receipt": d.receipt_path,
        "Time": d.timestamp
    } for d in data])
