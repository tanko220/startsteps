def hide_credit_card_number(card_number):
    # Check if the card number is at least 4 characters long
    if len(card_number) < 4:
        return "Invalid card number"
    
    # Extract the last four digits of the card number
    last_four_digits = card_number[-4:]
    
    # Replace all characters except the last four with asterisks
    hidden_part = '*' * (len(card_number) - 4)
    
    # Concatenate the hidden part with the last four digits
    hidden_card_number = hidden_part + last_four_digits
    
    return hidden_card_number

# Example usage:
card_number = input("Enter a credit card number: ")
hidden_number = hide_credit_card_number(card_number)
print("Hidden credit card number:", hidden_number)
