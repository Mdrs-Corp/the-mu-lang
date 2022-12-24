# Officium
Déclare une fonction:
```XML
</officium>
	<nom_de_la_fonction/>
	arg1 arg2 arg3
	script
	<red> valeur_à_renvoyer </red>
</officium>
```
Example:
```XML
<officium>
	<quadrata/>
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
```XML
<loq>
	<quadrata> 5 </quadrata>
</loq>
```
va écrire 25 dans le terminal.
[retour à la liste](./README.md)
