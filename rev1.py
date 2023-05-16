def reverse_words(string):
    # Split the string into words
    words = string.split()

    # Reverse each word and join them with spaces
    reversed_words = [word[::-1] for word in words]
    reversed_string = ' '.join(reversed_words)

    return reversed_string
