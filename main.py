import tokenizer
import parser


exemple="""
<µ>
	<loq>
		<add>1 2</add>
	</loq>
	<pam>
		<add>1 2</add>
	</pam>
</µ>
"""
fib=open("./fibonacci.µ","r")
hw=open("./helloworld.µ","r")

tokens = tokenizer.tokenize(fib.read())
parser.parse(tokens)
