# Officium

Declare a function :
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
Is a declaration of a function returning the value given as `x`, squared.  
If you declare this function, you can use it anywhere after on your script:
```xml
<loq> <square> 5 </square> </loq>
```
will print to the terminal 25.
