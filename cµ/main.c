#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/* Ordre importants, le compileur va vraiment yank les contenus à la suite
Et les mettres dans ce fichier afin d'executer un gros */
#include "structs.h"
#include "tokenizer.h"
#include "pile.h"


const char exemple[]="<µ><a></a> 12 ||allah est grand||   58 <a> ||squid game||</µ>";

int main(int argc, char const *argv[]) {
	token * T = tokenize(exemple,sizeof(exemple)/sizeof(exemple[0]));
    token * t=T;
	while(t){
		printf("Type : %i Valeur : %s\n",t->type, t->value);
		t=t->next;
	}
    //parse(T);
	return 0;
}
