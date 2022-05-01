# Indo
Met une valeur dans une variable :
```xml
<indo>
	variable
	valeur
</indo>
```
Example:
```xml
<indo>
	a
	10
</indo>
<loq>
	a
</loq>
```
va écrire `10`.  
Il est même possible d'assigner plusieurs variables depuis une même balise:
```xml
<indo>
	var1
	valeur_pour_var1
	var2
	valeur_pour_var3
	var3
	valeur_pour_var3
</indo>
```
Example:
```xml
<indo>
	a
	10
	b
	<add>
		a
		1
	</add>
	c
	|| fromage de chèvre ||
</indo>
```
Après l'éxécution de cette balise:
| varibale |type|valeur|
|:-:|:-|:-:|
|a|Numerus| 10|
|b|Numerus| 11|
|c|Filum| fromage de chèvre |
---
[retour à la liste](./README.md)
