import values
import errors
from tokenizer import isnumber
class Node():
	"""Classe principale:
	Un noeud est un élément dans un arbre qui execute l'action de ses enfants
	puis renvoie le resultat à son parent"""
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
	"""Loqum, équivalent au python "print", écrit le résultat de ses enfants dans
	le terminal"""
	REPR = "Loqum"

	def action(self, data,end="\n"):
		result = ''.join(c.action(data).toPrint() for c in self.childs)
		print(result,end=end)
		return result

class Qua(Loq):
	"""Demande à l'utilisateur d'entrer une valeur"""
	REPR="Quaestio"
	def action(self,data):
		super().action(data,end='')
		res=input()
		for elem in res:
			if not isnumber(elem):
				return values.Filum(res)
		return values.Numerus(res)



class Add(Node):
	"""Fait la somme de l'ensemble de ses termes"""
	REPR = "Addere"

	def action(self, data):
		result = self.childs[0].action(data)
		for child in self.childs[1:]:
			result = result.add(child.action(data))
		return result

class Partio(Node):
	"""Divise le premier terme par l'ensemble des suivants:
	<partio> 1 2 3 4 </partio> --> ((1/2)/3)/4
	"""
	REPR = "Partiorum"

	def action(self, data):
		result = self.childs[0].action(data)
		for child in self.childs[1:]:
			result = result.div(child.action(data))
		return result

class Mul(Node):
	"""Multiplie les termes entre eux
	<mul> 1 2 3 4 </mul> --> 1 x 2 x 3 x 4"""
	REPR = "Multiplicare"

	def action(self, data):
		result = self.childs[0].action(data)
		for child in self.childs[1:]:
			result = result.mul(child.action(data))
		return result

class Indo(Node):
	"""Assigne une variable à une valeur:
	<indo> a 5 </indo> --> a = 5
	<indo>
		a 5
		b 10
		a b
	</indo>
	--> a prend la valeur 5;
		b prend la valeur 10;
		a prend la valeur b;
	"""
	REPR = "Indo"

	def action(self, data):
		for i in range(0,len(self.childs), 2):
			name = self.childs[i].value
			result = self.childs[i+1].action(data)
			data[name] = result
		return result

class Identifier(Node):
	""" Noeud représentant une Variable,
	c'est une feuille de l'AST du programme"""

	REPR = "Variabilis"
	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return data[self.value]

class Num(Node):
	""" Noeud représentant un Nombre,
	c'est une feuille de l'AST du programme"""
	REPR = "Numerus"
	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return values.Numerus(self.value)

class Fil(Node):
	""" Noeud représentant une Chaine de Caractères,
	c'est une feuille de l'AST du programme"""
	REPR = "Filum"

	def __init__(self, value):
		super().__init__()
		self.value = value

	def action(self, data):
		return values.Filum(self.value)

class Ord(Node):
	""" Noeud représentant un tableau (liste ordonnée),
	c'est une feuille de l'AST du programme"""
	REPR="Ordinata"
	def __init__(self):
		super().__init__()

	def action(self,data):
		self.value = values.Ordinata([child.action(data) for child in self.childs])
		return self.value

class Inf(Node):
	"""Renvoie Verum si les nombres sont rangés dans l'ordre croissant:
	<inferioris> a b </inferioris> --> a inférieur à b
	<inferioris> a b c </inferioris> --> a inférieur à b ET b inférieur à c
	"""
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
	"""Renvoie vrai si toutes les entitées sont égales:
	<aequalis> a b </aequalis> --> a et b ont la même valeur
	<aequalis> a b c </aequalis> --> a et b et c ont la même valeur
	"""
	REPR = "Aequalis"

	def action(self, data):
		first = self.childs[0].action(data)

		for child in self.childs[1:]:
			if not first.equal(child.action(data)).isTrue:
				return values.Boolean("falsum")

		return values.Boolean("verum")

class Dum(Node):
	"""Boucle tant que:
	<dum>
		'condition'
		'script'
	</dum> --> while(condition){script}
	Tant que la condition est vraie, éxécuter le script
	"""
	REPR="Dum"
	def action(self, data):
		last = None
		while self.childs[0].action(data).isTrue:
			for child in self.childs[1:]:
				last = child.action(data)
		return last

class Si(Node):
	"""Instruction conditionelle:
	<si>
		'condition'
		'script'
	</si> --> if(condition){script}
	"""
	REPR="Si"

	def action(self, data):
		last = None
		if self.childs[0].action(data).isTrue:
			for child in self.childs[1:]:
				last = child.action(data)
		return last

class Ver(Node):
	""" Noeud représentant une valeur toujours Vraie, c'est une feuille de l'arbe du programme"""
	REPR="Verum"
	def action(self, data):return values.Boolean("verum")

class Fal(Node):
	""" Noeud représentant une valeur toujours Fausse, c'est une feuille de l'arbe du programme"""
	REPR="Falsum"
	def action(self, data):return values.Boolean("falsum")

class Et(Node):
	"""Renvoie vrai si toutes les valeurs sont vraies:
	<et> a b c </et> --> a and b and c
	"""
	REPR="Et"
	def action(self, data):return values.Boolean("verum" if all(child.action(data).isTrue for child in self.childs) else "falsum")

class Ubi(Node):
	"""Renvoie vrai si il'y a une condition vraie parmi l'ensemble des enfants:
	<ubi> a b c </ubi> --> a or b or c
	"""
	REPR="Ubi"
	def action(self, data):return values.Boolean("verum" if any(child.action(data).isTrue for child in self.childs) else "falsum")

class Ind(Node):
	"""Lorsque l'utilisateur consulte une liste à un certain indice"""
	REPR="Indicium"
	def action(self, data):
		return self.childs[0].action(data).at(self.childs[1].action(data))

class Officium(Node):
	"""Pour déclarer une fonction:
	<officium>
		<name/>
		arg1 arg2
		script
	</officium>
	-->
	def name(arg1, arg2):
		script"""
	REPR = "Officium"

	def action(self, data):
		name = self.childs[0].name
		parameters=[]
		i=1
		while self.childs[i].REPR=="Variabilis":
			parameters.append(self.childs[i])
			i+=1
		data[name] = values.Officium(parameters, self.childs[i:])

class Call(Node):
	"""Quand une fonction inconne est appellée"""
	REPR = "Allô"
	def __init__(self, name):
		super().__init__()
		self.name = name
		self.REPR=name

	def action(self, data):
		scopedata={}
		try:
			fun=data[self.name]
		except:
			errors.unknown(self.name)
		for variab,child in zip(fun.parameters,self.childs):
			scopedata[variab.value]=child.action(data)
		scopedata.update(data)
		for child in fun.value:
			if child.REPR=="Reducite":
				return child.action(scopedata)
			child.action(scopedata)
		return values.Filum("None")

class Red(Node):
	"""Pour renvoyer une valeur lors de l'appel d'une fonction custom"""
	REPR="Reducite"
	def action(self,data):
		return self.childs[0].action(data)

bigdic={
	"µ": Node,
	"loq": Loq,
	"qua": Qua,
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
	"ord": Ord,
	"indicium": Ind,
	"officium": Officium,
	"red":Red
}


def balise(token):
	"""Crée une balise à partir d'un token"""
	if token[1] in bigdic:
		return bigdic[token[1]]()
	return Call(token[1])

def newnode(token):
	"""Transforme un token en noeud"""
	if token[0] == "balise":return balise(token)
	elif token[0] == "number":return Num(token[1])
	elif token[0] == "string":return Fil(token[1])
	elif token[0] == "identifier":return Identifier(token[1])
	else:print('Node not fode',token)
