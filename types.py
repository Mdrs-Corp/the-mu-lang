class Nb:
	def __init__(self,val):
		self.v=v
	def add(self,other):
		if type(other)==Nb:
			return Nb(self.val+other.val)
		elif type(other)==Str:
			try:
				return other.tonumber() 
			except TypeError:
				print("Can't convert to float")
	def __repr__(self):
		return str(self.v)
class Str:
	chiffres="-.0123456789"
	def __init__(self,chn):
		self.chn=chn
	def tonumber(self):
		for char in self.chn:
			if not char in self.chiffres:
				raise TypeError
		return Nb(float(self.chn))
	def __repr__(self):
		return '"'+self.chn+'"'
def Var(s):
	if s[0]=='"' and s[-1]=='"':
		return Str(s[1:-2])
	# insérer ici de quoi détecter les Enumérables ( list,tuple,dict)
	elif s[0]=="{" and s[-1]=="}":
		...
	else:# SI ça n'a aucun indice de type, c'est un nombre
		truc=Str(s)
		try:
			return truc.tonumber()
		except:
			print(f"can't decode {truc}")
		
