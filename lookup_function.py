"""Product lookup helper for the math agent."""

import json


def lookup_product(product_name: str) -> str:
    with open("products.json") as f:
        catalog = json.load(f)
    if product_name in catalog:
        return str(catalog[product_name])
    return f"Product not found. Available products: {', '.join(catalog.keys())}"
