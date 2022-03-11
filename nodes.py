
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
		data[name] = self.childs[1].action(data)

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


bigdic={
	"loq": Loq,
	".µ": Node,
	"µ": Node,
	"add": Add,
	"partio": Partio,
	"mul": Mul,
	"indo": Indo
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
