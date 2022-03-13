##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"


isletter=lambda s:0x61<=ord(s)<=0x7a or 0x41<=ord(s)<=0x7a
isnumber=lambda s:0x30<=ord(s)<=0x39 or s=="."

def tokenize(str):
    tokens = []
    index = 0
    while index < len(str):
        char = str[index]
        if char == " " or char=="\n" or char=="\t":
            index += 1

        elif char=="|" and index+1<len(str):
        	start=index
        	if str[index+1]=="|":
        		index+=1
        		while not str[index]==str[index+1]=="|":
        			index+=1
        		index+=2
        	tokens.append(Token("string", str[start+2:index-2]))
        	
        elif char == "<":
            name = ""
            index += 1
            while index < len(str) and str[index] != ">":
                name += str[index]
                index += 1
            index += 1
            tokens.append(Token("balise", name))

        elif isnumber(char):
            text = ""
            while index < len(str) and isnumber(str[index]):
                text += str[index]
                index += 1
            tokens.append(Token("number", text))
            
        elif isletter(char):
            text = ""
            while index < len(str) and (isletter(str[index]) or isnumber(str[index])):
                text += str[index]
                index += 1
            tokens.append(Token("identifier", text))
            
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
