# Tests
Balise pour comparer les valeurs
## Inferioris
Renvoie Verum (Vrai) si toutes les valeurs sont dans l'ordre croissant :
```xml
<inferioris>
	a
	b
	c
	d
</inferioris>
```
renverra vrai si et seulement si a < b < c < d.  
De cette façon :
```xml
<inferioris> 0 a 10 </inferioris>
```
renverra vrai ssi `a` est compris entre 0 et 10

## aequalis
Renvoie vrai si toutes les valeurs sont égales à la première :
```xml
<aequalis>
	a
	b
	c
	d
</aequalis>
```
Renvera vrai ssi a = b  et a = c et a = d
## Conjectives
Les conjonctions logiques sont aussi possibles
### Et
Renvoie vrai si tous les arguments sont vrais:
```xml
<et>
	A
	B
	C
</et>
```
renverra Verum ssi le calcul de A, B **et** C renvoie Verum

### Ubi
Renvoie vrai si au moins une des balises est vraie:
```xml
<ubi>
	A
	B
	C
</ubi>
```
renverra Verum ssi le calcul de A, B **ou** C renvoie Verum
---
[retour à la liste](./README.md)
