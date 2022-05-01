# Ordinata

Declare an ordered array of items
```xml
<ord>
	a
	b
	c
	d
</ord>
```
will return the array [a,b,c,d].  
## Consult
You can put this array into a variable and consult the values later with {}:
```xml
<indo>
	crew
	<ord>
		|| john ||
		|| mac ||
		|| kinsey ||
		|| borris ||
		|| edward ||
	</ord>
</indo>
<loq>
	crew{0}
</loq>
```
will print ` john `
