def decimal_to_binary(decimal_num):
    if decimal_num < 0 or decimal_num >= 1024:
        raise ValueError("Decimal number must be between 0 and 1023.")

    binary_num = ""
    while decimal_num > 0:
        # Multiply the decimal number by 2
        decimal_num *= 2
        # If the result is greater than or equal to 1, add '1' to the binary representation
        if decimal_num >= 1:
            binary_num += '1'
            # Subtract 1 to keep the result less than 1
            decimal_num -= 1
        else:
            binary_num += '0'
    
    return binary_num

# Example usage:
decimal_number = float(input("Enter a decimal number (less than 1024): "))
binary_number = decimal_to_binary(decimal_number)
print("Binary representation:", binary_number)
