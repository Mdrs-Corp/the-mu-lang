# Dum
Execute le script tant que la condition est vraie:
```xml
<dum>
	condition
	script
</dum>
```
Example:
```xml
<indo> a 0 </indo>|| set a to 0 ||
<dum> || while ... ||
	<inferioris> a 10 </inferioris> || a < 10 ||
	<indo>
		a
		<add>
			a
			1
		</add>
	</indo> || set a to a + 1 ||
</dum>
```

[retour à la liste](./README.md)
