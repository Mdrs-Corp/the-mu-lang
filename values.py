from enum import Enum
from errors import alert

class MuTypes(Enum):
	FILUM = 0
	NUMERUS = 1
	BOOLEAN = 2
	ORDINATA = 3
	OFFICIUM = 4

class MuValue:
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
	def __init__(self, value):
		super().__init__(MuTypes.FILUM, value)

	def getValue(self):
		return self.value

	def add(self, muvalue):
		if muvalue.type == MuTypes.FILUM:
			return Filum(self.getValue() + muvalue.getValue())
		else:
			alert('You can only add Filum to another Filum')

	def mul(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Filum(self.getValue() * int(muvalue.getValue()))
		else:
			alert('You can only multiply Filum by Numerus')

	def equal(self, muvalue):
		if muvalue.type == MuTypes.FILUM:
			if self.getValue() == muvalue.getValue():
				return Boolean("verum")
			else:
				return Boolean("falsum")
		else:
			alert("You can only compare Filum to another Filum")

	def at(self, muvalue):
		return self.getValue()[int(muvalue.getValue())]

class Numerus(MuValue):
	def __init__(self, value):
		super().__init__(MuTypes.NUMERUS, value)

	def toPrint(self):
		return str(self.value)

	def getValue(self):
		return float(self.value)

	def add(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Numerus(str(self.getValue() + muvalue.getValue()))
		else:
			alert("You can only add Numerus to another Numerus")

	def mul(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Numerus(str(self.getValue() * muvalue.getValue()))
		else:
			alert('You can only multiply Numerus by another Numerus')

	def div(self, muvalue):
		if muvalue.type == MuTypes.NUMERUS:
			return Numerus(str(self.getValue() / muvalue.getValue()))
		else:
			alert('You can only partio Numerus by another Numerus')

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
	def __init__(self, value):
		super().__init__(MuTypes.BOOLEAN, value)

	def toPrint(self):
		return self.value

	def getValue(self):
		if self.value == "verum":
			return 0b1
		elif self.value == "falsum":
			return 0b0
		alert('Unknown Boolean:'+str(self.value))

	@property
	def isTrue(self):
		value = self.getValue()
		if value == 0b1:
			return True
		else:
			return False

	def anti(self):
		if self.getValue() == 0b0:
			return Boolean("verum")
		else:
			return Boolean("falsum")

	def equal(self, muvalue):
		if muvalue.type == MuTypes.BOOLEAN:
			if self.getValue() == muvalue.getValue():
				return Boolean("verum")
		return Boolean("falsum")

class Ordinata(MuValue):
	def __init__(self, childs):
		super().__init__(MuTypes.ORDINATA, childs)

	def getValue(self):
		return self.value

	def toPrint(self):
		#flem dle faire mtn
		return str(self.value)

	def at(self, muvalue):
		return self.value[int(muvalue.getValue())]

class Officium(MuValue):
	def __init__(self, parameters, code):
		self.parameters=parameters
		super().__init__(MuTypes.OFFICIUM, code)
