def most_expensive(prices):
    """Price of the most expensive item, None for an empty cart."""
    if not prices:
        return None
    return max(prices)