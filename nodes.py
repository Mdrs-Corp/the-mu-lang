import values

class Node():
	REPR = "µ"

	def __init__(self):
		self.childs = []

	def __repr__(self):
		t = f"{self.REPR}("
		for e in self.childs:
			t += str(e)
		return t + f")"

	def action(self, data):
		last = None
		for e in self.childs:
			last = e.action(data)
		return last

class Loq(Node):
	REPR = "Loqum"

	def action(self, data):
		result = self.childs[0].action(data).toPrint()
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
		return values.Numerus(self.value)

class Fil(Node):
	REPR = "Filum"

	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return values.Filum(self.value)
		

class Ord(Node):
	REPR="Ordinata"
	def __init__(self):
		super().__init__()

	def action(self,data):
		#je sais pas sqe c, jte fé confianse
		self.muvalue=values.Ordinata([c.action(data) for c in self.childs])
		return self.muvalue

class Inf(Node):
	REPR = "Inferioris"

	def action(self, data):
		previous = self.childs[0].action(data)

		for child in self.childs[1:]:
			next = child.action(data)
			if next.inf(previous).isTrue:
				return values.Boolean("falsum")
			previous = next

		return values.Boolean("verum")

class Aeq(Node):
	REPR = "Aequalis"

	def action(self, data):
		first = self.childs[0].action(data)

		for child in self.childs[1:]:
			if not first.equal(child.action(data)).isTrue:
				return values.Boolean("falsum")

		return values.Boolean("verum")

class Dum(Node):
	REPR="Dom"

	def action(self, data):
		last = None
		while self.childs[0].action(data).isTrue:
			for child in self.childs[1:]:
				last = child.action(data)
		return last

class Si(Node):
	REPR="Si"

	def action(self, data):
		last = None
		if self.childs[0].action(data).isTrue:
			for child in self.childs[1:]:
				last = child.action(data)
		return last

class Ver(Node):
	REPR="Verum"
	def action(self, data):return values.Boolean("verum")

class Fal(Node):
	REPR="Falsum"
	def action(self, data):return values.Boolean("falsum")

class Et(Node):
	REPR="Et"
	def action(self, data):return values.Boolean("verum" if all(child.action(data).isTrue for child in self.childs) else "falsum")

class Ubi(Node):
	REPR="Ubi"
	def action(self, data):return values.Boolean("verum" if any(child.action(data).isTrue for child in self.childs) else "falsum")
class Ind(Node):
	REPR="Indicium"

	def action(self, data):
		return self.childs[0].action(data).at(self.childs[1].action(data))

bigdic={
	"loq": Loq,
	".µ": Node,
	"µ": Node,
	"add": Add,
	"partio": Partio,
	"mul": Mul,
	"inferioris": Inf,
	"aequalis": Aeq,
	"dum": Dum,
	"si": Si,
	"indo": Indo,
	"verum": Ver,
	"falsum": Fal,
	"et": Et,
	"ubi": Ubi,
	"ord":Ord,
	"indicium":Ind
}

def newnode(token):
	if token.type == "balise":return bigdic[token.value]()
	elif token.type == "number":return Num(token.value)
	elif token.type == "string":return Fil(token.value)
	elif token.type == "identifier":return Identifier(token.value)
	else:print('Node not fode',token)
