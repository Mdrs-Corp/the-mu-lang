##converti une liste de tokens créé par le tokenizer.py, en en arbre AST facile a interpreter
##un truc genre  https://www.researchgate.net/profile/Thang-Huynh-Quyet/publication/300802898/figure/fig1/AS:723808830894081@1549580881995/Abstract-syntax-tree-of-Euclide-function.png
import tokenizer
import nodes


def parse(tokens:list):
	document=nodes.newnode(tokenizer.Token("balise",".µ"))
	ouverts=[document]
	for index,elem in enumerate(tokens):
		if elem.type=="balise":
			if elem.value[0]=="/":
				ouverts.pop()
			else:
				new=nodes.newnode(elem)
				ouverts[-1].childs.append(new)
				ouverts.append(new)
		else:
			ouverts[-1].childs.append(nodes.newnode(elem))
	print(document.childs[0])
	return document.childs[0]
