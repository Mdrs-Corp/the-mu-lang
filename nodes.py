def get(node):
	if type(node) == Num or type(node) == Fil:
		return node.value
	else:
		return node.action()

class Node():
	REPR = "µ"
	def __init__(self, value = None):
		self.childs = []
		self.value = value

	def __repr__(self):
		t = f"{self.REPR}[{self.value}]("
		for e in self.childs:
			t += "\n\t" + str(e)

		return t + f"){self.REPR[0]}\n"
	def action(self):
		for e in self.childs:
			e.action()

class Loq(Node):
	REPR = "Loqum"
	def __init__(self, v):
		self.value = "%"
		super().__init__()

	def action(self):
		self.value = ""
		for elem in self.childs:
			self.value += str(get(elem))
		print(self.value)
		return self.value

	def __repr__(self):
		return super().__repr__()


class Add(Node):
	REPR = "Addere"
	def __init__(self, v):
		super().__init__(0)

	def action(self):
		for enfant in self.childs:
			self.value += get(enfant)
		return self.value

class Partio(Node):
	REPR = "Partiorum"
	def __init__(self, v):
		super().__init__(1)

	def action(self):
		self.value = get(self.childs[0])
		for enfant in self.childs[1:]:
			self.value /= get(enfant)
		return self.value

class Mul(Node):
	REPR = "multiplicare"
	def __init__(self, v):
		super().__init__(1)
		
	def action(self):
		for enfant in self.childs:
			self.value *= get(enfant)
		return self.value
class Num(Node):
	# C'est un literal je devrai faire autrement je pense
	REPR = "Numerus"
	def __init__(self, value):
		super().__init__(int(value))

class Fil(Node):
	# Aussi un literal mais bon bref
	REPR = "Filum"
	def __init__(self, value):
		super().__init__(value)


bigdic={
	"loq":Loq,
	".µ":Node,
	"µ":Node,
	"add":Add,
	"partio":Partio,
	"mul":Mul
}

def newnode(token):
	print(token.type, token.value)
	if token.type == "balise":
		typ=bigdic[token.value]
		return typ(token.value)
	elif token.type == "number":
		return Num(token.value)
	elif token.type == "string":
		return Fil(token.value)
