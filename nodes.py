def get(node):
	if type(node)==Num or type(node)==Fil:
		return node.val
	else:
		return node.action()

class Node():
	REPR="µ"
	def __init__(self,val=None):
		self.enfants=[]
		self.val=val

	def __repr__(self):
		t=f"{self.REPR}[{self.val}]("
		for e in self.enfants:
			t+="\n\t"+str(e)

		return t+f"){self.REPR[0]}\n"
	def action(self):
		for e in self.enfants:
			e.action()

class Loq(Node):
	REPR="Loqum"
	def __init__(self,v):
		self.val="%"
		super().__init__()

	def action(self):
		self.val=""
		for elem in self.enfants:
			self.val+=str(get(elem))
		print(self.val)
		return self.val

	def __repr__(self):
		return super().__repr__()


class Add(Node):
	REPR="Addere"
	def __init__(self,v):
		super().__init__(0)
	def action(self):
		for enfant in self.enfants:
			self.val+=get(enfant)
		return self.val

class Partio(Node):
	REPR="Partiorum"
	def __init__(self,v):
		super().__init__(1)
	def action(self):
		self.val=get(self.enfants[0])
		for enfant in self.enfants[1:]:
			self.val/=get(enfant)
		return self.val

class Mul(Node):
	REPR="multiplicare"
	def __init__(self,v):
		super().__init__(1)
	def action(self):
		for enfant in self.enfants:
			self.val*=get(enfant)
		return self.val
class Num(Node):
	# C'est un literal je devrai faire autrement je pense
	REPR="Numerus"
	def __init__(self,val):
		super().__init__(int(val))

class Fil(Node):
	# Aussi un literal mais bon bref
	REPR="Filum"
	def __init__(self,val):
		super().__init__(val)


bigdic={"loq":Loq,".µ":Node,
"µ":Node,"add":Add,"partio":Partio,"mul":Mul}

def newnode(token):
	print(token.type,token.value)
	if token.type=="balise":
		typ=bigdic[token.value]
		return typ(token.value)
	elif token.type=="number":
		return Num(token.value)
	elif token.type=="string":
		return Fil(token.value)
