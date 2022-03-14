import tokenizer
import muparser as parser
import sys


if __name__=="__main__":
	assert 1!="1"
	if len(sys.argv)==1:
		p=input("Enter file to execute:")
	else:
		p=sys.argv[1]
	f=open(p,"r",encoding='UTF-8')
	tokens = tokenizer.tokenize(f.read())
	node=parser.parse(tokens)
	node.action({})
