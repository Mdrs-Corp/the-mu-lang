# Ordinata
Permet de créer une liste ordonnée d'objets
```XML
<ord>
	a
	b
	c
	d
</ord>
```
va créer le tableau [a,b,c,d].  
## Consult
Vous pouvez créer une liste et la consulter après avec des {}:
```XML
<indo>
	équipage
	<ord>
		|| Alphonse ||
		|| Albert ||
		|| Eudes ||
		|| Stéphane ||
		|| Jean ||
	</ord>
</indo>
<loq>
	équipage{0}
</loq>
```
renverra ` Alphonse `.  
L'utilisation des {} peut être remplacé par des balises Indicium (ou ind),
qui produisent le même résultat:
```XML
<loq>
	équipage<ind>0</ind>
</loq>
```
[retour à la liste](./README.md)
