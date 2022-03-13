from enum import Enum
from errors import alert
class MuTypes(Enum):
	FILUM = 0
	NUMERUS = 1
	BOOLEAN = 2
	ORDINATA = 3

class MuValue:
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def toPrint(self):
		return self.value

class Filum(MuValue):
	def __init__(self, value):
		super().__init__(MuTypes.FILUM, value)
		self.consult=None
		
	@property
	def repr(self,data={}):
		return str(self.getValue(data))

	def getValue(self,data={}):
		if self.consult:
			r=self.value[int(self.consult.action(data).getValue())]
			self.consult=None
			return Filum(r)
		else:
			return self.value

	def add(self, muvalue,data={}):
		if muvalue.type == MuTypes.FILUM:
			return Filum(self.getValue(data) + muvalue.getValue(data))
		else:
			alert('You can only add Filum to another Filum')

	def mul(self, muvalue,data={}):
		if muvalue.type == MuTypes.NUMERUS:
			return Filum(self.getValue(data) * muvalue.getValue())
		else:
			alert('You can only multiply Filum by Numerus')
			
	def equal(self, muvalue,data={}):
		if muvalue.type == MuTypes.FILUM:
			if self.getValue(data) == muvalue.getValue(data):
				return Boolean("verum")
			else:
				return Boolean("falsum")
		else:
			alert("You can only compare Filum to another Filum")
class Ordinata(MuValue):
	def __init__(self,childs):
		super().__init__(MuTypes.ORDINATA,childs)
		self.consult=None

	def getValue(self,data={}):
		if self.consult:
			r=self.value[int(self.consult.action(data).getValue())]
			self.consult=None
			return r.action(data).getValue()	
		else:
			return self.value
			
	@property
	def repr(self,data={}):
		return "/"+", ".join(c.repr(data) for c in self.childs)+"/"
		
class Numerus(MuValue):
	def __init__(self, value):
		super().__init__(MuTypes.NUMERUS, value)
		
	@property
	def repr(self):
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

	def andOp(self, muvalue):
		return self.getValue()&muvalue.getValue()

	def orOp(self, muvalue):
		return self.getValue()|muvalue.getValue()

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


		





