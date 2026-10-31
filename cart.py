TAX_RATE = 0.21

def average(prices):
    if not prices:
        return 0
    return sum(prices) / len(prices)

def total(prices):
    """Cart total, taxes included."""
    return round(sum(prices) * (1 + TAX_RATE), 2)

def apply_discount(prices, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return [p * (1 - percent / 100) for p in prices]

def count(prices):
    return sum(1 for p in prices if p > 0)

FREE_SHIPPING_FROM = 50
def shipping(prices):
    """Shipping cost: free from 50, before taxes."""
    if sum(prices) >= FREE_SHIPPING_FROM:
       return 0
    return 5
