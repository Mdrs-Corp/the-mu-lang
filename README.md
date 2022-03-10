# the-mu-lang
The µ programming langage python based
## Exemple of a code :
```
<µ>
	<loq>
		<add>1 2</add>
	</loq>
	<loq>
		<add>1 2</add>
	</loq>
</µ>
```
## Keywords table
| Keyword             | traduction |  what it does                                      |  
|:-------------------:|:----------:|:---------------------------------------------------|  
|*µ*                  | mu         | define the boundaries of the document              |  
|*loq*                | print      | print the content to the user, logs the expression |
|*||*                 | ""         | define the bondaries of a filum
|*add*,*partio*,*mul* | +,/,x      | basic maths                                        |  
|*indo*               | =          | set a value into a variable                        |
|*si*                 | if         | do this part if the condition is true              |
|*alite*              | else       | do this if the precedent condition is false        | 
|*dom*                | while      | while the condition is true, do                    |
|*inferioris*         | <          | conditionnal bloc if a < b                         |
|*aequalis*           | ==         | conditionnal bloc if a==b                          |
|*officium*           | fonction   |                                                    |

## Some examples
More directly in the repository

```
\<indo>  
&nbsp;&nbsp;&nbsp;identifier (A)  
&nbsp;&nbsp;&nbsp;expression (B)  
\</indo>  
||sets the value B in the variable A||
\<dom>  
&nbsp;&nbsp;&nbsp;condition (A)  
&nbsp;&nbsp;&nbsp;expression (B)  
\</dom>  
||do B while A||
```

  
