##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"


isletter=lambda s:0x61<=ord(s)<=0x7a or 0x41<=ord(s)<=0x7a
isnumber=lambda s:0x30<=ord(s)<=0x39 or s=="." or s=="-"

def tokenize(text:str):
    tokens = []
    index = 0
    while index < len(text):
        char = text[index]
        if char == " " or char=="\n" or char=="\t":
            index += 1

        elif char=="|" and index+1<len(text):
        	start=index
        	if text[index+1]=="|":
        		index+=1
        		while not text[index]==text[index+1]=="|":
        			index+=1
        		index+=2
        	tokens.append(Token("string", text[start+2:index-2]))

        elif char == "<":
            name = ""
            index += 1
            while index < len(text) and text[index] != ">":
                name += text[index]
                index += 1
            index += 1
            tokens.append(Token("balise", name))

        elif isnumber(char):
            t = ""
            while index < len(text) and isnumber(text[index]):
                t += text[index]
                index += 1
            tokens.append(Token("number", t))

        elif isletter(char):
            t = ""
            while index < len(text) and (isletter(text[index]) or isnumber(text[index])):
                t += text[index]
                index += 1
            tokens.append(Token("identifier", t))

        elif char=="{":
        	index+=1
        	tokens.append(Token("balise","indicium"))
        elif char=="}":
        	index+=1
        	tokens.append(Token("balise","/indicium"))

        else:
        	print("Weird char: ",char,f"({ord(char)})",index)
        	index+=1
    return tokens

class Token:
    def __init__(self, t, value):
        self.type = t
        self.value = value

    def __repr__(self):
        return f"{self.type}:{self.value}"
