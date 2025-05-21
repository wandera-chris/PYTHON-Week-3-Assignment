Args:
    price: The original price of the item.
    discount_percent: The discount percentage.

Returns:
    The final price after applying the discount, or the original price if no discount is applied.
"""
if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount
    return final_price
else:
    return price
    