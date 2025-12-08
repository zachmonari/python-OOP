from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import datetime
import uuid


def generate_receipt(transaction_message, amount, currency, method_name):
    receipt_id = str(uuid.uuid4())[:8]
    filename = f"receipt_{receipt_id}.pdf"

    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, 800, "PAYMENT RECEIPT")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Receipt ID: {receipt_id}")
    c.drawString(50, 740, f"Payment Method: {method_name}")
    c.drawString(50, 720, f"Amount: {currency} {amount}")
    c.drawString(50, 700, f"Status: SUCCESS")
    c.drawString(50, 680, f"Message: {transaction_message}")
    c.drawString(50, 660, f"Date: {datetime.datetime.now()}")

    c.save()
    return filename
