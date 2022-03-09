import tkinter as tk
import values
import tokens
import muparser
import interpreter
g=None
e=None
vars={}
def shell(script:str):
    global e,g,vars
    g=tk.Tk()
    g.config(bg='black')
    g.title('The µ shell')
    g.geometry('500x500')
    lines = script.split(sep = "\n")
    if all(lines):
        for line in lines:
            tok = tokens.lex(line)
            parse = muparser.parse(tok)
            for line in interpreter.interpret(vars, parse):
                tk.Label(g,text=line).pack()
    e=tk.Entry(g,font='Consolas 25',bg='black',fg='white')
    e.pack()
    g.bind('<KeyRelease>',inter)
def inter(touche):
    global vars
    if touche.keysym=="Return":
        
        s = e.get()
        tok = tokens.lex(s)
        parse = muparser.parse(tok)
        for line in interpreter.interpret(vars, parse):
            tk.Label(g,text=line).pack()


if __name__=="__main__":
    shell('')

