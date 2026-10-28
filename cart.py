TAX_RATE = 0.21

def average(prices):
    if not prices:
        return None
    return sum(prices) / len(prices)

def total(prices):
    """Cart total, taxes included."""
    return round(sum(prices) * (1 + TAX_RATE), 2)

def apply_discount(prices, percent):
    return [p * (1 - percent / 100) for p in prices]