from enum import Enum
from errors import alert

class MuTypes(Enum):
	FILUM = 0
	NUMERUS = 1
	BOOLEAN = 2
	ORDINATA = 3
	OFFICIUM = 4

class MuValue:
	REPR="Default"
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def toPrint(self):
		return self.value

	"all properties"

	def add(self, muvalue):
		"when <add>self muvalue</add>"

	def mul(self, muvalue):
		"when <mul>self muvalue</mul>"

	def equal(self, muvalue):
		"when <aequalis>self muvalue</aequalis>"

	def div(self, muvalue):
		"when <partio>self muvalue</partio>"

	def inf(self, muvalue):
		"when <inferioris>self muvalue</inferioris>"

	def at(self, muvalue):
		"when self {muvalue}"

class Filum(MuValue):
	REPR="FILUM"
	def __init__(self, value):
		super().__init__(MuTypes.FILUM, value)

	def getValue(self):
		return self.value

	def add(self, muvalue):
		if muvalue.type == MuTypes.FILUM:
			return Filum(self.getValue() + muvalue.getValue())
		elif muvalue.type == MuTypes.FILUM or muvalue.type==MuTypes.BOOLEAN:
			return Filum(self.getValue()+ muvalue.toPrint())
		else:
			alert(self,muvalue,'add')

	def mul(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Filum(self.getValue() * int(muvalue.getValue()))
		else:
			alert(self,muvalue,'multiply')

	def equal(self, muvalue):
		if muvalue.type == MuTypes.FILUM:
			if self.getValue() == muvalue.getValue():
				return Boolean("verum")
			else:
				return Boolean("falsum")
		else:
			alert(self,muvalue,'compare')

	def at(self, muvalue):
		return Filum(self.getValue()[int(muvalue.getValue())])

class Numerus(MuValue):
	REPR="NUMERUS"
	def __init__(self, value):
		super().__init__(MuTypes.NUMERUS, value)
		self.number=None

	def toPrint(self):
		return "%g" % self.getValue()

	def getValue(self):
		if self.number!=None:
			return self.number
		self.number=float(self.value)
		return self.number

	def add(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Numerus(str(self.getValue() + muvalue.getValue()))
		else:
			alert(self,muvalue,'add')

	def mul(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Numerus(str(self.getValue() * muvalue.getValue()))
		else:
			alert(self,muvalue,'multiply')

	def div(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Numerus(str(self.getValue() / muvalue.getValue()))
		else:
			alert(self,muvalue,'divide')

	def inf(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			if self.getValue() < muvalue.getValue():
				return Boolean("verum")
			else:
				return Boolean("falsum")

	def equal(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			if self.getValue() == muvalue.getValue():
				return Boolean("verum")
		return Boolean("falsum")

class Boolean(MuValue):
	REPR="BOOLEAN"
	def __init__(self, value):
		super().__init__(MuTypes.BOOLEAN, value)

	def toPrint(self):
		return str(self.value)

	def getValue(self):
		if self.value == "verum":
			return 1
		elif self.value == "falsum":
			return 0
		print('Unknown Boolean:'+str(self.value))

	@property
	def isTrue(self):
		value = self.getValue()
		if value == 1:
			return True
		else:
			return False

	def anti(self):
		if self.getValue() == 0:
			return Boolean("verum")
		else:
			return Boolean("falsum")

	def equal(self, muvalue):
		if muvalue.type == MuTypes.BOOLEAN:
			if self.getValue() == muvalue.getValue():
				return Boolean("verum")
		return Boolean("falsum")

class Ordinata(MuValue):
	REPR="ORDINATA"
	def __init__(self, childs):
		super().__init__(MuTypes.ORDINATA, childs)

	def getValue(self):
		return self.value

	def toPrint(self):
		return '['+', '.join(c.toPrint() for c in self.value)+']'

	def at(self, muvalue):
		return self.value[int(muvalue.getValue())]

class Officium(MuValue):
	REPR="OFFICIUM"
	def __init__(self, parameters, code):
		self.parameters=parameters
		super().__init__(MuTypes.OFFICIUM, code)
