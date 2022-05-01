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
You can even do some logical interpretations:
### Et
Return Verum if and only if all keys are Verum:
```xml
<et>
	A
	B
	C
</et>
```
will return verum if and only if A, B and C computes to Verum

### Ubi
Return Verum if one or more in all keys is/are Verum:
```xml
<ubi>
	A
	B
	C
</ubi>
```
will return verum if A, B or C computes to Verum
