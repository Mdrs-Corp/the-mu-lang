# Quastio

Permet de demander à l'utilisateur une valeur :
```XML
<qua>
	texte_d_interrogation
</qua>
```
renverra ce qu'a rentré l'utilisateur.  
Le retour peut être un Filum ou un Numerus, selon ce qu'a écrit l'utilisateur.  
Example:
```XML
<indo>
	age
	<qua>
		|| Quel est ton age ? ||
	</qua>
	nom
	<qua>
		|| Quel est ton nom ? ||
	</qua>
</indo>
<loq>
	|| Bonjour || nom
	||, tu as déjà vécu ||
	<mul>
		age
		365
	</mul> || jours!||
</loq>
```
