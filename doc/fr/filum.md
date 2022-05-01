# Filums
`||` et `||` précisent les limites d'une chaîne de caractères:  
```xml
|| Ceci est un filum ||
```
Chaque filum contient *exactement* les charctères avec lesquels il a été écrit.
```xml
<loq>
	||je suis un
très long filum ||
<loq>
```
va renvoyer :
```
je suis un
très long filum
```

## Operations
Il est possible de concacténer des filums:
```xml
<add> ||hello || ||world|| ||!||</add>
```
va créer: `hello world!`  
De la même manière, on peut multiplier des filums:
```xml
<mul> ||hey || 5 </mul>
```
va créer `hey hey hey hey hey `  
:warn: Attention, la multiplication ne fonctionne que si le nombre est après
le filum : `<mul> 5 ||hey|| </mul>` ne va pas fonctionner !
---
[retour à la liste](./README.md)
