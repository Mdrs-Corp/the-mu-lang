
	
class Node():
	REPR="µ"
	def __init__(self, parent,document=None):
		self.parent=parent
		self.enfants=[]
		self.val=""
		
	def __repr__(self):
		t=f"{self.REPR}[{self.val}](\n"
		for e in self.enfants:
			t+="\t"+str(e)+","
				
		return t+")\n"
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
			self.val+=elem.val
		return self.val
class Add(Node):
	REPR="Addere"
	def __init__(self,parent,v):
		self.val=0
		super().__init__(parent)
	def action(self):
		for enfant in self.enfants:
			self.val+=enfant.val
		return self.val
		
		
bigdic={"loq":Loq,"fil":Fil,".µ":Node,"µ":Node,"add":Add}
			
def newnode(token,parent):
	print(token.type,token.value)
	if token.type=="balise":
		typ=bigdic[token.value]	
		return typ(parent,token.value)
	elif token.type=="literal":
		truc=Node(parent)
		truc.val=token.value
		return truc
		

