from cart import average, total, apply_discount
def test_average():
    assert average([10, 20]) == 15
def test_average_empty_cart():
    assert average([]) == 0
def test_total_empty_cart():
    assert total([]) == 0
def test_discount():
    assert apply_discount([100, 50], 10) == [90, 45]