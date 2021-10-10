OPERATORS="%*/-+"
def calc(s:str):
	parts=sep(s)
	# Bon, y'a l'idée mais j'arrive pas à me concentrer
	for op in OPERATORS:
		print(op,parts)
		nextparts=[]
		pos=0
		while pos<len(parts):
			part=parts[pos]
			if part==op:
				nextparts+=[parts[pos-1]+part+parts[pos+1]]
				#calculate here
				pos+=1
			elif part in OPERATORS:
				nextparts+=[part]
			pos+=1
			
		nextparts+=[parts[-1]]
			
		parts=nextparts[:]
		
	return parts
def sep(st):
	#seprate each calculation 
	oldop=0
	ls=[]
	for pos,char in enumerate(st):
		if char in OPERATORS:
			ls+=[st[oldop:(pos)],char]
			oldop=pos+1
	return ls+[st[oldop:]]
			
if __name__=="__main__":
	print(calc("11%222*333/44-55"))
