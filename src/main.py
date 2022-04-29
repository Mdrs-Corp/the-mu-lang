"""Programme qui inteprète les fichier donné"""
import tokenizer
import muparser as parser
import sys

if __name__=="__main__":
	if len(sys.argv)==1:
		p=input("Enter file to execute:")
	else:
		p=sys.argv[1]
	f=open(p,"r",encoding="utf-8")
	tokens = tokenizer.tokenize(f.read())
	f.close()
	node=parser.parse(tokens)
	node.action({})
