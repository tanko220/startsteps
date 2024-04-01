def apply_discount(full_price, discount_percentage):
    # Calculate the discount amount
    discount_amount = full_price * (discount_percentage / 100)
    
    # Calculate the discounted price
    discounted_price = full_price - discount_amount
    
    return discounted_price

# Example usage:
full_price = int(input("Enter the full price of the item: "))
discount_percentage = int(input("Enter the discount percentage: "))

final_price = apply_discount(full_price, discount_percentage)
print("Price after discount:", final_price)
