# The µ lang
The µ programming langage python based  
You can crerate your magnificents programmes in µ in your atom editor by selecting the "Mu-Lang" grammar
## Execute your maginificient code
Just type in your command line where you downloaded the interpreter :  
```bash
python3 main.py path_of_your_file.µ
```  
No neads for extras modules, should woks for python>=3.6
## Exemple of a code :
```xml
<µ>
 <loq>
   || Hello world ! ||
 </loq>
</µ>
```

## Keywords table
| Keyword             | traduction |  what it does                                      |  
|:-------------------:|:----------:|:---------------------------------------------------|  
|*µ*                  | mu         | define the boundaries of the document              |  
|*loq*                | print      | print the content to the user, logs the expression |
|*\|\|*               | ""         | define the bondaries of a filum                    |
|*add*,*partio*,*mul* | +,/,x      | basic maths                                        |  
|*indo*               | =          | set a value into a variable                        |
|*si*                 | if         | do this part if the condition is true              |
|*alite*              | else       | do this if the precedent condition is false        |
|*dum*                | while      | while the condition is true, do                    |
|*inferioris*         | <          | conditionnal bloc if a < b                         |
|*aequalis*           | ==         | conditionnal bloc if a==b                          |
|*officium*           | fonction   |                                                    |
|*et*,*ubi*           | and,or     | return true if all/one of conditons are true       |
|*ord*                | array      | means ordinata, create an array                    |
|*{}*                 | [ ]        | to consult the ordinata at a certain index a{2}    |

## Some examples
More directly in the repository muExemples

### Sets the value B in the variable A
```xml
<indo>  
	identifier (A)  
	expression (B)  
</indo> 
```
### Do B while A
```xml
<dom>  
	condition (A)  
	expression (B)  
</dom>  
```
