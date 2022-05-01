# Filums
`||` Defines the boundaries of a string of characters:  
```xml
|| this is a filum ||
```
Each Filum contains the EXACT chain of characters it was written with:
```xml
<loq>
	||i am a
very long filum ||
<loq>
```
Prints as:
```
i am a
very long filum

```
## Operations
We can do concatenation with filums:
```xml
<add> ||hello || ||world|| ||!||</add>
```
returns: `hello world!`  
In this way, we can also multiply filums:
```xml
<mul> ||hey || 5 </mul>
```
Prints `hey hey hey hey hey `  
/!\\ however `<mul> 5 ||hey|| </mul>` doesn't work!
