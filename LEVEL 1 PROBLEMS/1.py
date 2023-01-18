def old_macdonald(name):
    out = []
    for i in range(len(name)):
        if i == 3:
            out.append(name[i].upper())
        elif i == 0:
            out.append(name[i].capitalize())
        else:
            out.append(name[i])
    return "".join(out)


# Check
print(old_macdonald('macdonald'))
print(type(old_macdonald('macdonald')))
