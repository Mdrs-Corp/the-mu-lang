##converti une liste de tokens créé par le tokenizer.py, en en arbre AST facile a interpreter
##un truc genre  https://www.researchgate.net/profile/Thang-Huynh-Quyet/publication/300802898/figure/fig1/AS:723808830894081@1549580881995/Abstract-syntax-tree-of-Euclide-function.png
import tokenizer
import nodes


def parse(tokens:list):
	document=nodes.newnode(tokenizer.Token("balise",".µ"),None)
	ouverts=[document]
	for index,elem in enumerate(tokens):
		if elem.type=="balise":
			if elem.value[0]=="/":
				ouverts.pop()
			else:
				new=nodes.newnode(elem,ouverts[-1])
				ouverts[-1].enfants.append(new)
				ouverts.append(new)
		else:
			ouverts[-1].enfants.append(nodes.newnode(elem,ouverts[-1]))
	print(document.enfants[0])
	return document.enfants[0]
