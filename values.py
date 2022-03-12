from enum import Enum

class MuTypes(Enum):
	STRING = 0
	NUMBER = 1
	BOOLEAN = 2

class MuValue:
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def toPrint(self):
		return self.value

class MuString(MuValue):
	def __init__(self, value):
		super().__init__(MuTypes.STRING, value)

	def toPrint(self):
		#return "\""+self.value+"\""
		return self.value

	def getValue(self):
		return self.value

	def add(self, muvalue):
		if muvalue.type == MuTypes.STRING:
			return MuString(self.getValue() + muvalue.getValue())

	def mul(self, muvalue):
		if muvalue.type == MuTypes.NUMBER:
			return MuString(self.getValue() * muvalue.getValue())


class MuNumber(MuValue):
	def __init__(self, value):
		super().__init__(MuTypes.NUMBER, value)

	def getValue(self):
		return float(self.value)

	def add(self, muvalue):
		if muvalue.type == MuTypes.NUMBER:
			return MuNumber(str(self.getValue() + muvalue.getValue()))

	def mul(self, muvalue):
		if muvalue.type == MuTypes.NUMBER:
			return MuNumber(str(self.getValue() * muvalue.getValue()))

	def div(self, muvalue):
		if muvalue.type == MuTypes.NUMBER:
			return MuNumber(str(self.getValue() / muvalue.getValue()))

	def compare(self, muvalue):
		if self.getValue() < muvalue.getValue():
			return MuBoolean("true")
		else:
			return MuBoolean("false")

class MuBoolean(MuValue):
	def __init__(self, value):
		super().__init__(MuTypes.BOOLEAN, value)

	def getValue(self):
		if self.value == "true":
			return 0b1
		elif self.value == "false":
			return 0b0
		print("error")

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
			return MuBoolean("true")
		else:
			return MuBoolean("false")
