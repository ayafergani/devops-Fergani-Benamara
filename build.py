
"""Build the shop's web page into site/index.html."""

import os

from cart import shipping, total

ITEMS = {"Notebook": 4, "Pen": 2, "Backpack": 45}
VERSION = os.environ.get("GITHUB_SHA", "dev")[:7]


def page(items, version):
    prices = list(items.values())
    rows = "".join(
        f"<li>{name}: {price}</li>" for name, price in items.items()
    )

    return f"""<!doctype html>
<html>
<head><meta charset="utf-8"><title>Shop</title></head>
<body>
<h1>Shop</h1>
<ul>{rows}</ul>
<p>Total, taxes included: {total(prices)}</p>
<p>Shipping: {shipping(prices)}</p>
<p><small>Version {version}</small></p>
</body>
</html>
"""


if __name__ == "__main__":
    os.makedirs("site", exist_ok=True)

    with open("site/index.html", "w") as f:
        f.write(page(ITEMS, VERSION))

    print("Built site/index.html, version", VERSION)
