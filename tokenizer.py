##converti le programe mu en une liste de tokens, en gros juste pour separer les "mots"

# renvoie vrai si le Character est une lettre
isletter=lambda s:0x61<=ord(s)<=0x7a or 0x41<=ord(s)<=0x7a
# renvoie vrai si le Character est un nombre ou un point ou un signe moins
isnumber=lambda s:0x30<=ord(s)<=0x39 or s=="." or s=="-"

def tokenize(text:str):
	"""Transforme text en une liste de tokens (fongibles)
	Un token est un tuple (type, value)"""
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
			tokens.append(("string", text[start+2:index-2]))

		elif char == "<":
			name = ""
			index += 1
			while index < len(text) and text[index] != ">":
				name += text[index]
				index += 1
			index += 1
			tokens.append(("balise", name))

		elif isnumber(char):
			t = ""
			while index < len(text) and isnumber(text[index]):
				t += text[index]
				index += 1
			tokens.append(("number", t))

		elif isletter(char):
			t = ""
			while index < len(text) and (isletter(text[index]) or isnumber(text[index])):
				t += text[index]
				index += 1
			tokens.append(("identifier", t))

		elif char=="{":
			index+=1
			tokens.append(("balise","indicium"))

		elif char=="}":
			index+=1
			tokens.append(("balise","/indicium"))

		else:
			print("Weird char: ",char,f"utf: ({ord(char)}) at:",index,", doesn't understand it")
			index+=1

	return tokens
