from build import page
from cart import total


def test_page_shows_items_total_and_version():
    html = page({"Pen": 10}, "abc1234")
    assert "<li>Pen: 10</li>" in html
    assert f"Total, taxes included: {total([10])}" in html
    assert "Version abc1234" in html
