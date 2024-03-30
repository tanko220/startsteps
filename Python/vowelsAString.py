def count_vowels(word):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Iterate through each character in the word
    for char in word:
        # Check if the character is a vowel
        if char.lower() in vowels:
            vowel_count += 1
    
    return vowel_count

# Example usage:
word = input("Enter a word: ")
print("Number of vowels:", count_vowels(word))
