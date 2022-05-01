# Math operations
Balises pour faire quelques opérations mathématiques
## Adderre
Ajoute toutes les valeurs données :
```xml
<add>
	a
	b
	c
	d
</add>
```
va calculer a+b+c+d.  
Il est même possible d'ajouter des filums à des numerus ou des booléans
```xml
<add>
	|| Je sais compter jusqu’à ||
	42
	|| et c'est fabuleux ||
</add>
```
va créer le filum : `Je sais compter jusqu'à 42 et c'est fabuleux`
## Multiplicare
Multiplie toutes les valeurs entre elles
```xml
<mul>
	a
	b
	c
</mul>
```
va calculer a\*b\*c.  
Les filums peuvent aussi être multipliés:
```xml
<mul> ||tato|| 5 </mul>
```
va renvoyer `tatotatotatotatotato`
## Partiorum
Fais la division de tous les nombres
```xml
<partio>
	a
	b
	c
</partio>
```
va calculer (a/b)/c.
