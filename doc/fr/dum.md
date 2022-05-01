# Dum
Exécute le script tant que la condition est vraie:
```XML
<dum>
	condition
	script
</dum>
```
Example:
```XML
<indo> a 0 </indo> 					|| mettre a à 0 ||
<dum> 								|| tant que ... ||
	<inferioris> a 10 </inferioris> || a inférieur à 10 ||
	<indo>
		a
		<add>
			a
			1
		</add>
	</indo> 						|| mettre a à a + 1 ||
</dum>
```
[retour à la liste](./README.md)
