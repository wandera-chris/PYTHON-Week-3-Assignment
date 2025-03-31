# PYTHON-Week-3-Assignment
# Description
# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
# Submit a github repo link


# ANSWERS

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

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

try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percentage)

    print(f"Final price: {final_price}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")


    # EXPLANATION
    calculate_discount(price, discount_percent) Function:

Takes the price and discount_percent as input.
Checks if discount_percent is 20 or greater.
If it is, calculates the discount_amount and subtracts it from the price to get the final_price.
If the discount is less than 20%, it returns the original price.
User Input and Function Call:

Prompts the user to enter the original_price and discount_percentage using input().
Converts the input to floating-point numbers using float().
Calls the calculate_discount() function with the user's input.
Prints the returned value.
Error Handling:

A try...except block is used to catch ValueError exceptions, which might occur if the user enters non-numeric input.
If a ValueError occurs, an error message is printed.
