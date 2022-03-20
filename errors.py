import sys
def alert(one,two,action):
	print(f"Erratum: You can't {action} a {one.REPR} with a {two.REPR} sorry :(")
	sys.exit()
