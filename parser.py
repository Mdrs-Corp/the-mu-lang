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
				if ouverts[-1].childs[-1].REPR=="Indicium":
					ouverts[-1].childs.pop()
				
			else:
				if elem.value[-1]=="/":
					elem.value=elem.value[:-1]
				new=nodes.newnode(elem)
				if new.REPR=="Indicium":
					ouverts[-1].childs[-1].consult=new
					
				ouverts[-1].childs.append(new)
				ouverts.append(new)
		else:
			ouverts[-1].childs.append(nodes.newnode(elem))
	return document.childs[0]
