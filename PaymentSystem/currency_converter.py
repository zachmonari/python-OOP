import requests
import time

# Free API base (no key required for basic usage)
API_URL = "https://api.exchangerate-api.com/v4/latest/{}"

# Simple in-memory cache to avoid hitting API repeatedly
_cache = {
    "rates": None,
    "base": None,
    "timestamp": 0
}
CACHE_TTL = 3600  # seconds (1 hour)
def get_rates(base_currency: str = "USD"):
    """
    Fetch exchange rates for a given base currency.
    Uses a simple cache to reduce API calls.
    """
    now = time.time()
    if (
            _cache["rates"] is not None
            and _cache["base"] == base_currency
            and now - _cache["timestamp"] < CACHE_TTL
    ):
        return _cache["rates"]
    response = requests.get(API_URL.format(base_currency))
    response.raise_for_status()
    data = response.json()

    rates = data.get("rates", {})
    _cache.update(
        {
        "rates": rates,
        "base": base_currency,
        "timestamp": now
    })

    return rates

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert amount from one currency to another.
    """
    if from_currency == to_currency:
        return amount

    rates = get_rates(from_currency)

    if to_currency not in rates:
        raise ValueError(f"Unsupported currency: {to_currency}")

    return round(amount * rates[to_currency], 2)