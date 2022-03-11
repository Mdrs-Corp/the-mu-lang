import values
import tokens
import muparser
import interpreter

def do(s):
    tok = tokens.lex(s)
    #print(tok)
    parse = muparser.parse(tok)
    #print(parse)
    interpreter.interpret(vars, parse)

vars = {}

f = open("exemple.µ")
a = f.read()
#print(a)
do(a)
while True:
    do(input(">"))
