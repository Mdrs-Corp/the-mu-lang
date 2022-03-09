##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"


isletter=lambda s:0x61<=ord(s)<=0x7a or 0x41<=ord(s)<=0x7a
isnumber=lambda s:0x30<=ord(s)<=0x39 or s=="."

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
        elif isnumber(chr):
            text = ""
            while index < len(str) and isnumber(str[index]):
                text += str[index]
                index += 1
            tokens.append(Token("literal", text))
        elif isletter(chr):
            text = ""
            while index < len(str) and (isletter(str[index]) or isnumber(str[index])):
                text += str[index]
                index += 1
            tokens.append(Token("identifier", text))
        else:
        	index+=1
    return tokens

class Token:
    def __init__(self, t, value):
        self.type = t
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"

if __name__=="__main__":
	print(tokenize("""
<oh>
</br>
3
5
<add>
3 a
</add>
</oh>"""))
