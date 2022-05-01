# Conditions

Does an action if the condition ( first argument ) is true :
```xml
<si>
	condition
	script
</si>
```
## Examples :
```xml
<loq> || Is 0 lower than 1? || </loq>
<si>
	<inferioris> 0 1 </inferioris>
	<loq> || 0 is lower than 1! || </loq>
</si>
```
Here, we get:
```
Is 0 lower than 1?
0 is lower than 1!

```
But if the condition is false, the inner script doesn't get executed:
```xml
<loq> || Is 1 equals to 2? || </loq>
<si>
	<aequalis> 1 2 </aequalis>
	<loq> || 1 is 2! || </loq>
</si>
```
Here, we get:
```
Is 1 equals to 2?
```
