# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the discounted price
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Print the result
if discount_percent >= 20:
    print(f"The final price after applying the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {price:.2f}")
