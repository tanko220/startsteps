def extract_integers(input_list):
    result = []
    for item in input_list:
        if isinstance(item, int) and item >= 0:
            result.append(item)
    return result

# Example usage:
mixed_list = [5, 'apple', 10, 'banana', 20, 'cherry', 0]
integers_only = extract_integers(mixed_list)
print("Integers only:", integers_only)
