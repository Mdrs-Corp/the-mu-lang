from sys import argv
import values
import tokens
import muparser
import interpreter

vars = {}

if __name__=="__main__":
    # Condition vraie ssi on utilise pas le programme dans un import
    if len(argv)>=2:
        script=open(argv[1],"r").read() # ~/$ python3 compiler.py programme.µ
    else:
        script = open("exemple.µ","r").read()

    tok = tokens.lex(script.replace("\n", ""))
    parse = muparser.parse(tok)
    interpreter.interpret(vars, parse)
    while True:
        s = input(">µ>")
        tok = tokens.lex(s)
        parse = muparser.parse(tok)
        print(interpreter.interpret(vars, parse))
