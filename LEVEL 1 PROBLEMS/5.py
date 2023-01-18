def paper_doll(text):
    out = []
    for i in text:
        out.append(i*3)
    print("".join(out))


# Check
paper_doll('Hello')
# Check
paper_doll('Mississippi')