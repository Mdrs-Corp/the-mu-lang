# Math operations
Balises pour faire quelques opérations mathématiques
## Adderre
Ajoute toutes les valeurs données :
```XML
<add>
	a
	b
	c
	d
</add>
```
va calculer a+b+c+d.  
Il est même possible d'ajouter des filum à des numerus ou des Boolean
```XML
<add>
	|| Je sais compter jusqu’à ||
	42
	|| et c'est fabuleux ||
</add>
```
va créer le filum : `Je sais compter jusqu'à 42 et c'est fabuleux`
## Multiplicare
Multiplie toutes les valeurs entre elles
```XML
<mul>
	a
	b
	c
</mul>
```
va calculer a\*b\*c.  
Les filum peuvent aussi être multipliés:
```XML
<mul> ||tato|| 5 </mul>
```
va renvoyer `tatotatotatotatotato`
## Partiorum
Fais la division de tous les nombres
```XML
<partio>
	a
	b
	c
</partio>
```
va calculer (a/b)/c.
[retour à la liste](./README.md)
