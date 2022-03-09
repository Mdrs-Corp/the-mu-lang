##converti une liste de tokens créé par le tokenizer.py, en en arbre AST facile a interpreter
##un truc genre  https://www.researchgate.net/profile/Thang-Huynh-Quyet/publication/300802898/figure/fig1/AS:723808830894081@1549580881995/Abstract-syntax-tree-of-Euclide-function.png

class Node():
	def __init__(self,obj, parent):
		self.parent=parent
		self.enfants=[]
		self.obj=obj
	def __repr__(self):
		
		if self.enfants:
			return f"{self.obj.type}[{self.obj.value}](\n\t{','.join(str(e) for e in self.enfants)})\n"
		else:
			return self.obj.__repr__()

def parse(tokens:str):
	document=Node(Token("DOCUMENT",".µ"),None)
	ouverts=[document]
	for index,elem in enumerate(tokens):
		if elem.type=="balise":
			if elem.value[0]=="/":
				ouverts.pop()
			else:
				new=Node(elem,ouverts[-1])
				ouverts[-1].enfants.append(new)
				ouverts.append(new)
		else:
			ouverts[-1].enfants.append(Node(elem,ouverts[-1]))
	print(document)
	return document
