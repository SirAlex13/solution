def capitalize_words(input_string):
    # Capitalize the first letter of each word
    result = input_string.title()
    return result

# Example usage
input_string = input("Enter a string: ")
result = capitalize_words(input_string)
print("Result:", result)
