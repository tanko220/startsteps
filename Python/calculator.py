def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        # Check if dividing by zero
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    elif operator == '.':
        return num1 * num2
    else:
        return "Error: Invalid operator"

# Example usage:
num1 = 6
operator = '.'
num2 = 4

result = calculate(num1, operator, num2)
print("Result:", result)
