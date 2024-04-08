def sort_numbers(numbers, order):
    if order == "asc":
        return sorted(numbers)
    elif order == "desc":
        return sorted(numbers, reverse=True)
    elif order == "none":
        return numbers
    else:
        raise ValueError("Invalid order parameter. It should be 'asc', 'desc', or 'none'.")

# Example usage:
numbers = [5, 2, 8, 1, 3]
order = input("Enter 'asc', 'desc', or 'none': ")

sorted_numbers = sort_numbers(numbers, order)
print("Sorted numbers:", sorted_numbers)
