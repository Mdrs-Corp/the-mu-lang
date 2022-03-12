import tokenizer
import parser
import sys

if __name__=="__main__":
	if len(sys.argv)==1:
		p=input("Enter file to execute:")
	else:
		p=sys.argv[1]
	f=open(p,"r")
	tokens = tokenizer.tokenize(f.read())
	node=parser.parse(tokens)
	node.action({})
