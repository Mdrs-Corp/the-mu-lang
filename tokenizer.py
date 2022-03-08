##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"
def tokenize(str):
    tokens = []
    index = 0
    while index < len(str):
        chr = str[index]
        if chr == "<":
            name = ""
            index += 1
            while index < len(str) and str[index] != ">":
                name += str[index]
                index += 1
            index += 1
            tokens.append(Token("balise", name))
    return tokens



class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return self.type + ": " +self.value

print(tokenize("<oh></br></oh>"))
