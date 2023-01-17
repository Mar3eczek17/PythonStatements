def animal_crackers(text):
    singiel_word = text.split()
    if singiel_word[0][0] == singiel_word[1][0]:
        print(True)
    else:
        print(False)


# Check
animal_crackers('Levelheaded Llama')
# Check
animal_crackers('Crazy Kangaroo')
