# converti une liste de tokens créé par le tokenizer.py, en en arbre AST facile a interpreter
# un truc genre  https://www.researchgate.net/profile/Thang-Huynh-Quyet/publication/300802898/figure/fig1/AS:723808830894081@1549580881995/Abstract-syntax-tree-of-Euclide-function.png
# https://fr.wikipedia.org/wiki/Arbre_de_la_syntaxe_abstraite

from nodes import newnode,Ind
import sys

class Brick:
	def __init__(self,v):
		self.v=v
		self.down=None

	def history(self):
		if self.down==None:
			return [self]
		else:
			return [self]+self.down.history()

class Pile:
	def __init__(self,t='FIRST'):
		self.tete=Brick(t)

	@property
	def top(self):
		return self.tete.v

	def add(self,zarma):
		new=Brick(zarma)
		new.down=self.tete
		self.tete=new

	def pop(self):
		self.tete=self.tete.down

	def __repr__(self):
		return ','.join(str(s) for s in self.tete.history())


def parse(tokens:list):
	"""Transforme la liste des tokens en un arbre d'instructions ou de valeurs"""
	ouverts=Pile(newnode(tokens[0]))
	for token in tokens:
		if token[0]=="balise":
			if token[1][0]=="/":
				if ouverts.top.REPR.lower()[:len(token[1])-1]!=token[1][1:]:
					print(f"A tag has been opened({ouverts.top.REPR}) but not well closed(found {token[1][1:]})")
					sys.exit()
				else:
					ouverts.pop()
			else:
				if token[1][-1]=="/":
					# Balise autofermante
					token=token[0],token[1][:-1]
					new=newnode(token)
					ouverts.top.childs.append(new)
				else:
					new=newnode(token)
					if new.REPR=="Indicium":
						new.childs.append(ouverts.top.childs.pop())
					ouverts.top.childs.append(new)
					ouverts.add(new)
		else:
			ouverts.top.childs.append(newnode(token))
	return ouverts.top
