def double_characters(input_string):
    doubled_string = ''
    for char in input_string:
        doubled_string += char * 2
    return doubled_string

# Example usage:
input_string = input("Enter a string: ")
doubled_string = double_characters(input_string)
print("Doubled string:", doubled_string)
