# Dum
Executes the script **while** the condition is true :
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
