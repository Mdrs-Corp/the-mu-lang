import sys
import json
# Pour prévenir l'utilisateur des erreurs qu'il  peut y avoir

#La liste des µ keywords
keywords=json.load(open("keywords.json","r"))

def alert(one,two,action:str):
	"""Alerter si les types ne sont pas compatibles entre eux avec l'opération"""
	print(f"Erratum: You can't {action} a {one.REPR} with a {two.REPR} sorry :(")
	sys.exit()

def unknown(word:str):
	"""Si l'utilisateur utilise une balise non définie"""
	print(f"Erratum: we don't understand \"{word}\", did you mean {suggest(word)} ?")
	sys.exit()

def getMatchCoefficient(array:list, matchWord:str)->dict:
	"""Renvoie le coefficient de similarité de chaque mot de l'array avec matchWorld"""
	matches = []
	matchWord = matchWord.lower()
	for i in array:
		matchCoef = compare(matchWord, i.lower(), True)
		matches.append({"value": i, "coef": matchCoef})
	matches = sorted(matches, key = lambda i: -i['coef'])
	return matches

def compare(a:str, b:str, ratio:bool):
	"""renvoie la "distance" entre a et b"""
	rows = len(a) + 1
	cols = len(b) + 1
	distance = [[0 for j in range(cols)] for i in range(rows)]
	for row in range(1, rows):
		for col in range(1, cols):
			distance[row][0] = row
			distance[0][col] = col
	for col in range(1, cols):
		for row in range(1, rows):
			cost = 0
			if a[row - 1] == b[col -1]:
				cost = 0
			elif ratio:
				cost = 2
			else:
				cost = 1
			distance[row][col] = min(distance[row - 1][col] + 1, distance[row][col - 1] + 1, distance[row - 1][col - 1] + cost)
	dist = distance[len(distance) - 1][len(distance[0]) - 1]
	return (len(a) + len(b) - dist) / (len(a) + len(b)) if ratio else dist

def suggest(word):
	"""Renvoie le mot le plus proche disponible dans le fichier keywords.json"""
	return getMatchCoefficient(keywords, word)[0]["value"]

if __name__ == '__main__':
	print(suggest("jean"))
