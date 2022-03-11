
class Node():
	REPR = "µ"
	def __init__(self):
		self.childs = []

	def __repr__(self):
		t = f"{self.REPR}("
		for e in self.childs:
			t += "\n\t" + str(e)
		return t + f"){self.REPR[0]}\n"

	def action(self, data):
		last = None
		for e in self.childs:
			last = e.action(data)
		return last

class Loq(Node):
	REPR = "Loqum"
	def action(self, data):
		result = ""
		for elem in self.childs:
			result += str(elem.action(data))
		print(result)
		return result



class Add(Node):
	REPR = "Addere"

	def action(self, data):
		result = 0
		for child in self.childs:
			result += child.action(data)
		return result
		

class Partio(Node):
	REPR = "Partiorum"

	def action(self, data):
		result = self.childs[0].action(data)
		for child in self.childs[1:]:
			result /= child.action(data)
		return result

class Mul(Node):
	REPR = "multiplicare"

	def action(self, data):
		result = 1
		for child in self.childs:
			result *= child.action(data)
		return result

class Indo(Node):
	REPR = "<RYAN C A TOI>"

	def action(self, data):
		name = self.childs[0].value
		result = self.childs[1].action(data)
		data[name] = result
		return result

class Identifier(Node):
	REPR = "IDENTIFIER"
	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return data[self.value]

class Num(Node):
	# C'est un literal je devrai faire autrement je pense
	REPR = "Numerus"
	def __init__(self, value):
		super().__init__()
		self.value = int(value)

	def action(self, data):
		return self.value

class Fil(Node):
	# Aussi un literal mais bon bref
	REPR = "Filum"
	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return self.value

class Inf(Node):
	REPR = "Inferioris"
	def __init__(self, v):
		super().__init__(0)

	def action(self):
		precedent=self.childs[0].action()
		for child in self.childs[1:]:
			suivant=child.action()
			if precedent>suivant:
				return 0
		return 1
		
class Dum(Node):
	REPR="Dom"
	def __init__(self,v):
		super().__init__(0)
	def action(self):
		condi=self.childs[0]
		while condi.action():
			for child in self.childs[1:]:
				child.action()
		return 1
class Si(Node):
	REPR="Si"
	def __init__(self,v):
		super().__init__(0)
	def action(self):
		if self.childs[0].action:
			for child in self.childs[1:]:
				child.action()
		return 1
class Indo(Node):
	REPR="Indo"
	def __init__(self,v):
		super().__init__(0)
	def action(self):
		dic={}
		for i in range(0,len(self.childs),2):
			dic[self.childs[i]]=self.childs[i+1].action()
class Var(Node):
	REPR="Variabilis"
	def __init__(self,v):
		super.__init__(v)
	def action(self):
		return self.v

bigdic={
	"loq":Loq,
	".µ":Node,
	"µ":Node,
	"add":Add,
	"partio":Partio,
	"mul":Mul,
	"inferioris":Inf,
	"dum":Dum,
	"si":Si,
	"indo":Indo
}

def newnode(token):
	print(token.type, token.value)
	if token.type == "balise":
		typ=bigdic[token.value]
		return typ()
	elif token.type == "number":
		return Num(token.value)
	elif token.type == "string":
		return Fil(token.value)
	elif token.type == "identifier":
		return Identifier(token.value)
