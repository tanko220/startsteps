def decimal_to_binary(decimal_num):
    binary_num = ""
    
    # Special case for decimal number 0
    if decimal_num == 0:
        return "0"
    
    while decimal_num > 0:
        # Divide the decimal number by 2 and get the remainder
        remainder = decimal_num % 2
        # Prepend the remainder to the binary number
        binary_num = str(remainder) + binary_num
        # Divide the decimal number by 2 for the next iteration
        decimal_num //= 2
    
    return binary_num

# Example usage
decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print("Binary representation:", binary_number)
