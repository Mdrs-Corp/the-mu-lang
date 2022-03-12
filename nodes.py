
class Node():
	REPR = "µ"
	def __init__(self):
		self.childs = []

	def __repr__(self):
		t = f"{self.REPR}("
		for e in self.childs:
			t += "\n\t" + str(e)
		return t + f"){self.REPR[0]}"

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
			e=elem.action(data)
			if e==True :
				e="Verum"
			elif e==False :
				e="Falsum"
			result += str(e)
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
	REPR = "Indo"

	def action(self, data):
		for i in range(0,len(self.childs),2):
			name = self.childs[i].value
			result = self.childs[i+1].action(data)
			data[name] = result
		return result

class Identifier(Node):
	REPR = "Variabilis"
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

	def action(self, data):
		prece=self.childs[0].action(data)
		for elem in self.childs[1:]:
			suiv = elem.action(data)
			if suiv<prece:
				return False
			prece=suiv
		return True

class Dum(Node):
	REPR="Dom"

	def action(self, data):
		condi = self.childs[0]
		last = None
		while condi.action(data):
			for child in self.childs[1:]:
				last = child.action(data)
		return last


class Si(Node):
	REPR="Si"

	def action(self, data):
		last = None
		if self.childs[0].action(data):
			for child in self.childs[1:]:
				last = child.action(data)
		return last
class Ver(Node):
	REPR="Verum"
	def action(self,d):
		return True
class Fal(Node):
	REPR="Falsum"
	def action(self,d):
		return False
bigdic={
	"loq": Loq,
	".µ": Node,
	"µ": Node,
	"add": Add,
	"partio": Partio,
	"mul": Mul,
	"inferioris": Inf,
	"dum": Dum,
	"si": Si,
	"indo": Indo,
	"verum": Ver,
	"falsum":Fal
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
