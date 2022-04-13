#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* Ordre importants, le compileur va vraiment yank les contenus à la suite
Et les mettres dans ce fichier afin d'executer un gros */
#include "structs.h"
#include "tokenizer.h"
#include "parser.h"


const char exemple[]="<µ> <a> ||SQPQR|| ||kakak|| </a> ||jean||</µ>";

int main(int argc, char const *argv[]) {
	printf("Lexing : \n");
	token * T = tokenize(exemple,sizeof(exemple)/sizeof(exemple[0]));
    token * t=T;
	while(t){
		printf("Type : %i Valeur : %s\n",t->type, t->value);
		t=t->next;
	}
	printf("Parsing : \n");
	node * R = parse(T);
    printFamilly(R,0);
	return 0;
}
