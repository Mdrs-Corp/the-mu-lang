##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"


isletter=lambda s:0x61<=ord(s)<=0x7a or 0x41<=ord(s)<=0x7a
isnumber=lambda s:0x30<=ord(s)<=0x39 or s=="."

def tokenize(fil):
    tokens = []
    index = 0
    while index < len(fil):
        car = fil[index]
        if car == " " or car=="\n" or car=="\t":
            index += 1

        elif car=="|" and index+1<len(fil):
        	debut=index
        	if fil[index+1]=="|":
        		index+=1
        		while not fil[index]==fil[index+1]=="|":
        			index+=1
        		index+=2
        	tokens.append(Token("string", fil[debut+2:index-2]))
        elif car == "<":
            name = ""
            index += 1
            while index < len(fil) and fil[index] != ">":
                name += fil[index]
                index += 1
            index += 1
            tokens.append(Token("balise", name))

        elif isnumber(car):
            text = ""
            while index < len(fil) and isnumber(fil[index]):
                text += fil[index]
                index += 1
            tokens.append(Token("number", text))
        elif isletter(car):
            text = ""
            while index < len(fil) and (isletter(fil[index]) or isnumber(fil[index])):
                text += fil[index]
                index += 1
            tokens.append(Token("identifier", text))
        else:
        	print("Weird char:",car,ord(car))
    return tokens

class Token:
    def __init__(self, t, value):
        self.type = t
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"
