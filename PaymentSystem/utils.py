def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        if amount <= 0:
            return None
        return amount
    except ValueError:
        return None
