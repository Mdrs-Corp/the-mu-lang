# `i` Lexer, aka mise en tokens
## Qu'es ce qu'un fichier script ?  
Du point de vue d'un ordinateur, un script n'est qu'un fichier contenant du texte  
La première étape de notre interprétation de ce script doit donc passer par une compréhention et un découpage des ordres écrits par le programmeur.  
## Objectif
Le but du lexer est donc de relever les différents mots clefs et expressions,  
afin de transformer ce texte en une succession d'ordres et d'indications compréhensibles par la machine.  
Prenons l'exemple de ce script (hehe)  
Un ordianateur ne peut lire qu'un seul charactère à la fois.  
On va ainsi *scanner* le document afin de trouver un charactère clef à la compréhention du script.  
Ici, on trouve des **<**, qui vont indiquer un début de balise [highlith]  
On va donc consiéder tout ce qui se situe enter "<" et ">" comme une balise d'action, ou **token**, et les stocker dans une liste.  
# `ìi` Parser, mise en arbre
Maintenant que nous avons une liste de tokens, nous devons comprendre ces tokens. 
un peu comme un point marque la fin d'une phrase, chaque balise marque la fin et le début d'une partie.  
Chaque *partie* contient des *sous-parties*, qu'il faut organiser dans la mémoire.  
la plupart des langages de programation peuvent etre transformés en arbre [animation cool]  
Qu-est ce qu'un arbre?[photo d'arbre cool qui tourne]  
en informatique un arbre est une structure composé de noeud, chaque noeud a des enfants.  
De cette manière, le script est transformé en arbre, où chaque balise est un noeud.  

# `iii` Interpreter
