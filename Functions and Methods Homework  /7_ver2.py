import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphabet = set(alphabet)
    # Remove any spaces from the input string
    str1 = str1.replace(" ", '')
    # Concert into all lowercase
    str1 = str1.lower()
    # Grab all unique letters from the string set()
    str1 = set(str1)
    # alpabhet set == string set input
    return str1 == alphabet


# Driver code
ispangram("The quick brown fox jumps over the lazy dog")
