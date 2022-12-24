# Documentation du langage µ
Des exemples de programmes en µ sont disponibles dans le dossier
[muPrograms](../../muPrograms)
## Les types de données
### Filum
Une chaîne de caractères, plus de détails [ici](./filum.md)
### Numerus
Un entier relatif
### Boolean
Une valeur qui peut être vraie (Verum) ou fausse (Falsum)  
C'est un boolean qui est renvoyé à l'exécution d'un [test](./tests.md)
## Keywords table
| Mot clef       |traduction JavaScript | Bref Résumé |  
|:-------------|:--------:|:----------------------------------------------|  
|[µ](./mu.md)                       |mu        |Définit les limites du script mu |  
|[loq](./loq.md)                    |print     |Renvoie son contenu dans le shell|
|[qua](./quastio.md)                |input     |demande à l'utilisateur un contenu|
|[\|\| \|\|](./filum.md)            |" "       |Permet de déclarer un filum|
|[add, partio, mul](./math.md)      |+,/,x     |Opérations mathématiques simples|  
|[indo](./indo.md)                  |=         |Sauve une valeur dans une variable|
|[si](./conditions.md)              |if        |Execute son contenu si sa condition est vraie|
|[dum](./dum.md)                    |while     |Execute son contenu tant que la condition est vraie|
|[inferioris](./tests.md##inferioris)|<         |Renvoie vrai si les arguments sont dans l'ordre croissant|
|[aequalis](./tests.md##aequalis)    |==        |Renvoie vrai si tous les blocs sont égaux|
|[et, ubi](./tests.md##conjectives)   |and,or    |Renvoie vrai si tout/un argument(s) vrai|
|[officium](./officium.md)          |function  |Permet de créer des fonctions|
|[ord](./ordinata.md)               |array     |Permet de créer des tableaux|
|[{}](./ordinata.md##consult)        |[ ]       |Permet de consulter le tableau à un certain index|
