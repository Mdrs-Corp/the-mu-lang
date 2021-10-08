from sys import argv
import types
vars = {}

def comp(line):
    line = line.split(sep = " ")
    if line[0] == "make":
        name = line[1]
        value = line[2]
        vars[name] = types.Var(value)
        print("Created variable " + name + " to " + value)
    elif line[0] == "yield":
        var = line[1]
        if var in vars:
            print(f"{var} is {vars[var]}")
        else:
            print(f"{var} not found")
    elif line[0] == "set":
        var = line[1]
        if var in vars:
            vars[var] = calc(line[2])
            print(f"{var} set to {vars[var]}")
        else:
            print(f"{var} not found")
    elif line[0] == "do":
        for i in range(int(line[1])):
            comp(" ".join(line[2:]))
    elif line[0] == "§":
        pass
    elif line[0] == "?":
        for name in vars:
                print(name, ":", vars[name])
    else:
        print('Not executed : ' + " ".join(line))

if __name__==__main__: 
	# Condition vraie ssi on utilise pas le programme dans un import
	if len(argv)>=2:
		script=open(argv[1],"r").read() # ~/$ python3 compiler.py programme.µ
	else:
		script = open("exemple.µ","r").read()

	lines = script.split(sep = "\n")
	for line in lines:
		comp(line)
	while True:comp(input(">µ>"))
	
