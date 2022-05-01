# Tests
Tag to compare values :
## Inferioris
Return Verum (True) if all the values are in ascending order :
```xml
<inferioris>
	a
	b
	c
	d
</inferioris>
```
Will return true if and only if a < b < c < d

## aequalis
Return Verum if all the values are equals :
```xml
<aequalis>
	a
	b
	c
	d
</aequalis>
```
will return true if and only if a = b = c = d  
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
