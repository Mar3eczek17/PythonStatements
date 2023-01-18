def master_yoda(text):
    words = text.split()
    words.reverse()
    print(" ".join(words))


# Check
master_yoda('I am home')
# Check
master_yoda('We are ready')
