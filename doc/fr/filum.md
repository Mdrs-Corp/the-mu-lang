# Filums
`||` and `||` defines the boundaries of a string of characters:  
```xml
|| this is a filum ||
```
each Filums  contains the EXACT chain of characters it  was written with :
```xml
<loq>
	||i am a
very long filum ||
<loq>
```
will be rendered as :
```
i am a
very long filum

```
## Operations
We can do some concatenations with filums:
```xml
<add> ||hello || ||world|| ||!||</add>
```
will be equal to: `hello world!`  
In this way, we can also multiply filums:
```xml
<mul> ||hey || 5 </mul>
```
will render `hey hey hey hey hey `  
/!\\ Be aware that `<mul> 5 ||hey|| </mul>` won't work !
