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