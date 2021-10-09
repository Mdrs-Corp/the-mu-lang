from enum import Enum

class MuTypes(Enum):
	STRING = 0
	NUMBER = 1
	BOOLEAN = 2


class MuValue:
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def set(self, value):
		self.value = value

	def toPrint(self):
		return self.value

class MuString(MuValue):
	def __init__(self):
		super().__init__(self, MuTypes.STRING, "")

	def set(self, value):
		if (value[0] == "\"" and value[-1] == "\"") or (value[0] == "'" and value[-1] == "''"):
			self.value = value[1:-1]
			return True
		else:
			return False

	def toPrint(self):
		return "\""+self.value+"\""


class MuNumber(MuValue):
	def __init__(self):
		super().__init__(self, MuTypes.NUMBER, 0)

	def set(self, value):
		if value.find("-")>0 or value.count(".")>1:
			return False
		for chr in value:
			if not chr in "-.0123456789":
				return False
		self.value = float(value)
		return True

	def toPrint(self):
		return str(self.value)

class MuBoolean(MuValue):
	def __init__(self):
		super().__init__(self, MuTypes.BOOLEAN, True)

	def set(self, value):
		if value == "true":
			self.value = True
			return True
		elif value == "false":
			self.value = False
			return True
		else:
			return False

	def toPrint(self):
		if self.value:
			return "true"
		else:
			return "false"

def create(type):
	if type == "string":
		return MuString()
	elif type == "number":
		return MuNumber()
	elif type == "boolean":
		return MuBoolean()
	return None
