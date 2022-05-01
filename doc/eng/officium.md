# Officium

Declares a function:
```xml
</officium>
	<name_of_the_function/>
	arg1 arg2 arg3

	script
	<red> Value_to_return </red>
</officium>
```
Example:
```xml
<officium>
	<square/>
	x

	<indo>
		v
		<mul> x x </mul>
	</indo>
	<red> v </red>
</officium>
```
This is the declaration of a function squaring the argument and returning it.  
If you declare this function, you can use it anywhere in your script:
```xml
<loq> <square> 5 </square> </loq>
```
would print 25 to the terminal.
