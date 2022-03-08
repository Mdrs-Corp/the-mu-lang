##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = ",0123456789"


def tokenize(str):
    tokens = []
    index = 0
    while index < len(str):
        chr = str[index]

        if chr == " ":
            index += 1

        elif chr == "<":
            name = ""
            index += 1
            while index < len(str) and str[index] != ">":
                name += str[index]
                index += 1
            index += 1
            tokens.append(Token("balise", name))

        elif chr in numbers:
            text = ""
            while index < len(str) and str[index] in numbers:
                text += str[index]
                index += 1
            tokens.append(Token("literal", text))

    return tokens



class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return self.type + ": " +self.value

print(tokenize("<oh></br> 3    5    <add>3 5</add></oh>"))
