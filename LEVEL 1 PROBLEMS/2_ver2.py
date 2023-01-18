def master_yoda(text):
    words = text.split()
    reverse_word_list = words[::-1]
    print(' '.join(reverse_word_list))


# Check
master_yoda('I am home')
# Check
master_yoda('We are ready')
