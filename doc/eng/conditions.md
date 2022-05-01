# Conditions

Do an action if the condition ( first argument ) is true :
```xml
<si>
	condition
	script
</si>
```
## Examples :
```xml
<loq> || Is 0 lower than 1 ? || </loq>
<si>
	<inferioris> 0 1 </inferioris>
	<loq> || 0 is lower than 1 ! || </loq>
</si>
```
Here, we will get :
```
Is 0 lower than 1 ?
0 is lower than 1 !

```
but if the condition is false, the inner script won't be executed :
```xml
<loq> || Is 1 equals to 2 ? || </loq>
<si>
	<aequalis> 1 2 </aequalis>
	<loq> || 1 is 2 ! || </loq>
</si>
```
Here, we will get :
```
Is 1 equals to 2 ?
```
