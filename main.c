#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* Ordre importants, le compileur va vraiment yank les contenus à la suite
Et les mettres dans ce fichier afin d'executer un gros */
#include "structs.h"
#include "tokenizer.h"
#include "parser.h"
#include "action.h"

char exemple[]="<µ> <loq> ||jean|| </loq><loq><add>1 2</add></loq></µ>";









int main(int argc, char const *argv[]){
	printf("Lexing : ");
	token * T;
	if(argc==2){
		printf("From \"%s\" : \n", argv[1]);
		T = tokenizeFromFile(argv[1]);
	}else{
		printf("From exemple : \n" );
		T = tokenize(exemple,sizeof(exemple)/sizeof(exemple[0]));
	}

    token * t=T;
	while(t){
		printf("Type : %i Valeur : %s\n",t->type, t->value);
		t=t->next;
	}

	printf("Parsing : \n");
	node * R = parse(T);
    printFamilly(R,0);

	printf("Interpreting : \n");
	action(R);
	return 0;
}
