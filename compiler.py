from sys import argv
import values

vars = {}

def comp(line):
    line = line.split(sep = " ")

    if line[0] == "make":
        type = line[1]
        name = line[2]
        var = values.create(type)
        if var != None:
            vars[name] = var
            print(f"Created {name} of type {type}")
        else:
            print("Invalid type")

    elif line[0] == "set":
        var = line[1]
        value = " ".join(line[2:])
        if var in vars:
            #gonna have to do things like a+b
            #https://en.wikipedia.org/wiki/Lexical_analysis#Tokenization
            success = vars[var].set(value)
            if success:
                print(f"{var} set to {value}")
            else:
                print("Invalid value")
        else:
            print(f"{var} not found")

    elif line[0] == "yield":
        var = line[1]
        if var in vars:
            print(f"{var} is {vars[var].toPrint()}")
        else:
            print(f"{var} not found")

    elif line[0] == "do":
        for i in range(int(line[1])):
            comp(" ".join(line[2:]))

    elif line[0] == "§":
        pass

    elif line[0] == "?":
        for name in vars:
                print(name, ":", vars[name].toPrint())

    else:
        print('Not executed : ' + " ".join(line))

if __name__=="__main__":
	# Condition vraie ssi on utilise pas le programme dans un import
	if len(argv)>=2:
		script=open(argv[1],"r").read() # ~/$ python3 compiler.py programme.µ
	else:
		script = open("exemple.µ","r").read()

	lines = script.split(sep = "\n")
	for line in lines:
		comp(line)
	while True:comp(input(">µ>"))
