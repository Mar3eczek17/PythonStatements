def palindrome(s):
    # REMOVE SPACES STRING
    s = s.replace(" ", "")
    # Check is string is == reversed version of the string
    print(s == s[::-1])


palindrome('helleh')
palindrome('madam')
palindrome('kayak')
palindrome('racecar')
palindrome('nurses run')
