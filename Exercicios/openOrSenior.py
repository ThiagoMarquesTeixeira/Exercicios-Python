def openOrSenior(data):
    retorno = []
    for status in data:
        idade = status[0]
        handicap = status[1]
        if (idade >= 55) and (handicap >= 7):
            retorno.append("Senior")
        else:
            retorno.append("Open")

    return retorno


print(openOrSenior([[54, 25], [68, 8], [61, 7], [54, 5], [35, 8], [52, 21], [53, 27]]))
