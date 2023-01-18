import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    # String as set, ready to intersection
    str1_as_set = set(str1.replace(" ", '').lower())
    # String as set, rady to compare with alphabet
    str1_to_compare = "".join(sorted(set(str1.replace(" ", '').lower())))
    # Intersection of two sets
    intersection_of_the_sets = "".join(sorted(str1_as_set.intersection(alphabet)))

    # Python function to check whether a string is pangram or not
    if str1_to_compare == intersection_of_the_sets:
        print(True)
    else:
        print(False)


# Driver code
ispangram("The quick brown fox jumps over the lazy dog")
