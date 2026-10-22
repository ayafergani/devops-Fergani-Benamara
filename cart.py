TAX_RATE = 0.19
def average(prices):
    return sum(prices) / len(prices)
def total(prices):
    """Cart total, taxes included."""
    return round(sum(prices) * (1 + TAX_RATE), 2)