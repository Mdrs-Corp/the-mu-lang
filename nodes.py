import values

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
			result += elem.action(data).toPrint()
		print(result)
		return result

class Add(Node):
	REPR = "Addere"

	def action(self, data):
		result = self.childs[0].action(data)
		for child in self.childs[1:]:
			result = result.add(child.action(data))
		return result

class Partio(Node):
	REPR = "Partiorum"

	def action(self, data):
		result = self.childs[0].action(data)
		for child in self.childs[1:]:
			result = result.div(child.action(data))
		return result

class Mul(Node):
	REPR = "multiplicare"

	def action(self, data):
		result = self.childs[0].action(data)
		for child in self.childs[1:]:
			result = result.mul(child.action(data))
		return result

class Indo(Node):
	REPR = "Indo"

	def action(self, data):
		for i in range(0,len(self.childs), 2):
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
	REPR = "Numerus"

	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return values.MuNumber(self.value)

class Fil(Node):
	REPR = "Filum"

	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return values.MuString(self.value)

class Inf(Node):
	REPR = "Inferioris"

	def action(self, data):
		previous = self.childs[0].action(data)

		for child in self.childs[1:]:
			next = child.action(data)
			if next.compare(previous).isTrue():
				return values.MuBoolean("false")
			previous = next

		return values.MuBoolean("true")

class Dum(Node):
	REPR="Dom"

	def action(self, data):
		last = None
		while self.childs[0].action(data).isTrue():
			for child in self.childs[1:]:
				last = child.action(data)
		return last

class Si(Node):
	REPR="Si"

	def action(self, data):
		last = None
		if self.childs[0].action(data).isTrue():
			for child in self.childs[1:]:
				last = child.action(data)
		return last

class Ver(Node):
	REPR="Verum"
	def action(self, data):
		return values.MuBoolean("true")

class Fal(Node):
	REPR="Falsum"
	def action(self, data):
		return values.MuBoolean("false")

class Et(Node):
	REPR="Et"
	def action(self, data):
		if all(child.action(data).isTrue() for child in self.childs):
			return values.MuBoolean("true")
		else:
			return values.MuBoolean("false")

class Ubi(Node):
	REPR="Ubi"
	def action(self, data):
		if any(child.action(data).isTrue() for child in self.childs):
			return values.MuBoolean("true")
		else:
			return values.MuBoolean("false")

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
	"falsum":Fal,
	"et": Et,
	"ubi": Ubi
}

def newnode(token):
	if token.type == "balise":
		typ=bigdic[token.value]
		return typ()
	elif token.type == "number":
		return Num(token.value)
	elif token.type == "string":
		return Fil(token.value)
	elif token.type == "identifier":
		return Identifier(token.value)
