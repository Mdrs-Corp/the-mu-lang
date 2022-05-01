# Indo
Sets the value into a variable:
```xml
<indo>
	variable
	value
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
Prints `10`.  
You can even set multiple variables with one indo tag:
```xml
<indo>
	var1
	value_for_var1
	var2
	value_for_var3
	var3
	value_for_var3
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
	|| i am groot ||
</indo>
```
After this:
| var |type|value|
|:-:|:-|:-:|
|a|Numerus| 10|
|b|Numerus| 11|
|c|Filum| i am groot |
