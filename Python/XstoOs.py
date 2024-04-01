def xo_equal(string):
    # Count the occurrences of 'X' and 'O' in the string
    count_x = string.lower().count('x')
    count_o = string.lower().count('o')
    
    # Check if the counts are equal or both are zero
    return count_x == count_o or (count_x == 0 and count_o == 0)

# Example usage:
input_string = input("Enter a string: ")
result = xo_equal(input_string)
print("Are the counts of 'X's and 'O's equal (or both zero)?", result)
