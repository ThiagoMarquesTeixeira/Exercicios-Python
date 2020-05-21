from re import split
"""
Desafio:
PT-BR
Conclua o método / função para converter palavras delimitadas por traço / sublinhado em revestimento de camelo. A primeira palavra na saída deve ser maiúscula apenas se a palavra original estiver em maiúscula (conhecida como Upper Camel Case, também conhecida como caso Pascal).
En
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
"""


def to_camel_case(text):
    group_words = split(r'[^a-zA-Z0-9]', text)
    x = []
    for i in range(len(group_words)):
        if i == 0:
            x.append(group_words[i])
        else:
            x.append(group_words[i].capitalize())
    return "".join(x)
