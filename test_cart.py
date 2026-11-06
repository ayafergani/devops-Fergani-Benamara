import pytest

from cart import apply_discount, average, shipping, total
from stats import most_expensive


def test_average():
    assert average([10, 20]) == 15
def test_average_empty_cart():
    assert average([]) == 0
def test_total_empty_cart():
    assert total([]) == 0
def test_discount():
    assert apply_discount([100, 50], 10) == [90, 45]
def test_shipping_small_cart():
    assert shipping([20]) == 5
def test_shipping_big_cart():
    assert shipping([100]) == 0
def test_shipping_free_from_50():
    assert shipping([50]) == 0
def test_discount_over_100_is_refused():
    with pytest.raises(ValueError):
        apply_discount([100], 150)

def test_most_expensive():
    assert most_expensive([10, 50, 20]) == 50
def test_most_expensive_empty_cart():
    assert most_expensive([]) is None