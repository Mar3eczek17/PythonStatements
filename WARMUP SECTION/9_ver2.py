def animal_crackers(text):
    singiel_word = text.upper().split()
    print(singiel_word)

    return singiel_word[0][0] == singiel_word[1][0]


# Check
animal_crackers('Levelheaded Llama')
# Check
animal_crackers('Crazy Kangaroo')
# Check
animal_crackers('Crazy cat')
