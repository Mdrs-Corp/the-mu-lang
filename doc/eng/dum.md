# Dum
This tag is used to execute the script **while** the condition is true:
```xml
<dum>
	<condition/>
	<code/>
</dum>
```
```xml
<indo> a 0 </indo>|| set a to 0 ||
<dum> || while... ||
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
So, since 0 is always false, this loop never ends :
```xml
<dum>
	1
	<loq> || This will never end !|| </loq>
</dum>
```
