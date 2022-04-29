"""Programme qui inteprète les fichier donné"""
import tokenizer
import muparser as parser
import sys

def main(text:str):
	tokens = tokenizer.tokenize(text)
	return parser.parse(tokens)

if __name__=="__main__":
	if len(sys.argv)==1:
		p=input("Enter file to execute:")
	else:
		p=sys.argv[1]
	f=open(p,"r",encoding="utf-8")
	node=main(f.read())
	f.close()
	node.action({})
