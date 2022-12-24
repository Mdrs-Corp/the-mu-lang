# Conditions
Execute le script si le premier argument renvoie Verum:
```XML
<si>
	condition
	script
</si>
```
## Examples :
```XML
<loq> || Es ce que 1 est inférieur à 0? || </loq>
<si>
	<inferioris> 0 1 </inferioris>
	<loq> || 0 est plus petit que 1 ! || </loq>
</si>
```
Ici, nous aurons:
```
 Es ce que 1 est inférieur à 0?
 0 est plus petit que 1 !
```
Mais si la condition est fausse, le script à l'intérieur ne va pas être exécuté:
```XML
<loq> ||Es ce que 1 est égal à 2? || </loq>
<si>
	<aequalis> 1 2 </aequalis>
	<loq> || 1 est égal à 2 ! || </loq>
</si>
```
Ici nous aurons:
```
Es ce que 1 est égal à 2?
```
[retour à la liste](./README.md)
