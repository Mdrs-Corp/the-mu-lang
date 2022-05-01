# Tests
Tag to compare values:
## Inferioris
Returns Verum (True) if all the values are in ascending order:
```xml
<inferioris>
	a
	b
	c
	d
</inferioris>
```
Would return true if and only if a < b < c < d

## aequalis
Returns Verum if all the values are equal:
```xml
<aequalis>
	a
	b
	c
	d
</aequalis>
```
would return true if and only if a = b = c = d  
## Conjectives
You can even do some logical interpretation:
### Et
Returns Verum if and only if all keys are Verum:
```xml
<et>
	A
	B
	C
</et>
```
Would return verum if and only if A, B and C compute to Verum

### Ubi
Returns Verum if one or more key is/are Verum:
```xml
<ubi>
	A
	B
	C
</ubi>
```
Would return verum if A, B or C computes to Verum
