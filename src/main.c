#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LEN 100
#define VARS_LEN 10
/* Ordre importants, le compileur va vraiment yank les contenus à la suite
Et les mettres dans ce fichier afin d'executer un gros */
#include "structs.h"
#include "tokenizer.h"
#include "parser.h"
#include "hash.h"
#include "action.h"
char exemple[]="<µ> <loq> ||jean|| </loq><loq><add>1 2</add></loq></µ>";

int main(int argc, char const *argv[]){
	var * vars =(var*) calloc(VARS_LEN,sizeof(var));

	token * T;
	if(argc>=2 && argv[1][0]!='-'){
		T = tokenizeFromFile(argv[1]);
	}else{
		printf("Interpreting from exemple : \n" );
		T = tokenize(exemple,sizeof(exemple)/sizeof(exemple[0]));
	}
	int devmode=0;
	for (size_t i = 0; i < argc; i++) {
		if (strcmp(argv[i],"-dev")==0) {
			devmode=1;
		}
	}
	if(devmode){
		printf("-->Lexing : \n");
		token * t=T;
		printf("type\ttaille\tvaleur\n");
		char * types[]={"string","balise","number","identifier"};
		while(t){
			printf("%s\t%i\t%s\n",types[t->type], t->size, t->value);
			t=t->next;
		}

		printf("-->Parsing : \n");
		node * R = parse(T);
		printFamilly(R,0);

		printf("-->Interpreting : \n");
		mess * resultat =(mess*) malloc(sizeof(mess));
		action(R,0,vars,resultat);

		printf("\n-->Variables :\n");
		see_hash(vars);
	}else{
		mess * resultat =(mess*) malloc(sizeof(mess));
		action(parse(T),0,vars,resultat);

	}


	return 0;
}
