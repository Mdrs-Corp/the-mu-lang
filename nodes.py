
	
class Node():
	REPR="µ"
	def __init__(self, parent,val=None):
		self.parent=parent
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
	def __init__(self,parent,v):
		self.val="%"
		super().__init__(parent)
	def action(self):
		result=""
		for enfant in self.enfants:
			result+=str(enfant.action())
		print(result+"\n")
		return 1
		
class Fil(Node):
	REPR="Filum"
	def __init__(self,parent,v):
		self.val=v
		super().__init__(parent)
	def action(self):
		self.val=""
		for elem in self.enfants:
			self.val+=str(elem.val)
		return self.val
	def __repr__(self):
		self.action()
		return super().__repr__()
		
class Math(Node):
	REPR="Operation"
	def __init__(self,p,v):
		super().__init__(p,v)
	def get(self,elem):
		if type(elem)==Num:
			return elem.val
		else:
			return elem.action()
		
class Add(Math):
	REPR="Addere"
	def __init__(self,parent,v):
		super().__init__(parent,0)
		self.get=super().get
	def action(self):
		for enfant in self.enfants:
			self.val+=self.get(enfant)
		return self.val
		
class Partio(Math):
	REPR="Partiorum"
	def __init__(self,parent,v):
		super().__init__(parent,1)
		self.get=super().get
	def action(self):
		self.val=self.get(self.enfants[0])
		for enfant in self.enfants[1:]:
			self.val/=self.get(enfant)
		return self.val
		
class Mul(Math):
	REPR="multiplicare"
	def __init__(self,parent,v):
		super().__init__(parent,1)
		self.get=super().get
	def action(self):
		for enfant in self.enfants:
			self.val*=self.get(enfant)
		return self.val
class Num(Node):
	# C'est un literal je devrai faire autrement je pense
	REPR="Numerus"
	def __init__(self,parent,val):
		super().__init__(parent,int(val))
		
		
bigdic={"loq":Loq,"fil":Fil,".µ":Node,
"µ":Node,"add":Add,"partio":Partio,"mul":Mul}
			
def newnode(token,parent):
	print(token.type,token.value)
	if token.type=="balise":
		typ=bigdic[token.value]	
		return typ(parent,token.value)
	elif token.type=="literal":
		return Num(parent,token.value)
		

