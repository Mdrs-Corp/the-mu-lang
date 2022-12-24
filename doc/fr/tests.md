# Tests
Balise pour comparer les valeurs, renvoie un boolean(Verum / Falsum)
## Inferioris
Renvoie Verum (Vrai) si toutes les valeurs sont dans l'ordre croissant :
```XML
<inferioris>
	a
	b
	c
	d
</inferioris>
```
renverra vrai si et seulement si a < b < c < d.  
De cette façon :
```XML
<inferioris> 0 a 10 </inferioris>
```
renverra vrai si et seulement si `a` est compris entre 0 et 10

## aequalis
Renvoie vrai si toutes les valeurs sont égales à la première :
```XML
<aequalis>
	a
	b
	c
	d
</aequalis>
```
Renverra vrai si et seulement si a = b  et a = c et a = d
## Conjonctives
Les conjonctions logiques sont aussi possibles
### Et
Renvoie vrai si tous les arguments sont vrais:
```XML
<et>
	A
	B
	C
</et>
```
renverra Verum si et seulement si le calcul de A, B **et** C renvoie Verum

### Ubi
Renvoie vrai si au moins une des balises est vraie:
```XML
<ubi>
	A
	B
	C
</ubi>
```
renverra Verum si et seulement si le calcul de A, B **ou** C renvoie Verum
[retour à la liste](./README.md)
