
class file:
    jean="J E A N"
    pass

def comp(line):
    if line.startswith("make "):
        name=5+line[5:].find(" ")
        print("Created variable "+line[5:name]+" to "+line[name+1:])
        setattr(file,line[5:name] , line[name+1:])
    elif line.startswith("yield "):
        for var in dir(file):
            if var in line[6:]:
                print(f"{var} is {getattr(file,var)}")
    elif line.startswith("set "):
        line=line.split(sep=" ")
        print(f"{line[1]} is now {calc(line[2])}")
        setattr(file,line[1],line[2])
    elif line.startswith("do "):
        debut_nb=fin_nb=3
        while line[fin_nb] in "0123456789":
            fin_nb+=1
        nb=int(line[debut_nb:fin_nb])
        for i in range(nb):
            comp(line[fin_nb+1:])
    elif line[0]=="§":
        pass
    elif line=="?":
        for elem in dir(file):
            if not (elem.startswith("__") and elem.endswith("__")):
                print(elem,":",getattr(file,elem))
    else:
        print('Not executed : '+line)
def calc(string):
    
        
script=open("exemple.µ","r").read()
lines=script.split(sep="\n")  
for line in lines:
    comp(line)
