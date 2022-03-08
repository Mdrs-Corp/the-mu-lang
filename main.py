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

tokens = tokenizer.tokenize(exemple)
parse(tokens)
