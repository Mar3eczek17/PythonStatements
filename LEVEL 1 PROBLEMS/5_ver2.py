def paper_doll(text):
    result = ''

    for char in text:
        result += char * 3
    return result


# Check
paper_doll('Hello')
# Check
paper_doll('Mississippi')
