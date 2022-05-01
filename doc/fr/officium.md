# Officium
Déclare une fonction:
```xml
</officium>
	<nom_de_la_fonction/>
	arg1 arg2 arg3

	script
	<red> valeur_à_renvoyer </red>
</officium>
```
Example:
```xml
<officium>
	<Carré/>
	x

	<indo>
		v
		<mul> x x </mul>
	</indo>
	<red> v </red>
</officium>
```
Est une fonction qui renvoie le carré de la valeur donné (x).  
Une fois déclaré, la fonction peut être utilisé n'importe où dans le script:
```xml
<loq>
	<Carré> 5 </Carré>
</loq>
```
va écrire 25.
