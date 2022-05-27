#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LEN 100
#define VARS_LEN 10
#define FUNS_LEN 10
/* Ordre importants, le compileur va vraiment yank les contenus à la suite
Et les mettres dans ce fichier afin d'executer un gros */
#include "structs.h"
#include "tokenizer.h"
#include "parser.h"
#include "hash.h"
#include "alerts.h"
#include "action.h"

int main(int argc, char const *argv[]){
	struct memory mem;
	mem.vars = (var*) calloc(VARS_LEN,sizeof(var));
	mem.funs = (fun*) calloc(FUNS_LEN,sizeof(fun));
	token * T;

	if(argc>=2 && argv[1][0]!='-'){
		T = tokenizeFromFile(argv[1]);
	}else{
		printf("Interpreting from built-in exemple : \n");
		T = tokenizeFromFile("./src/exemple.µ");
	}

	int devmode = 0;
	for (unsigned int i = 0; i < argc; i++) {
		if (strcmp(argv[i],"-dev")==0) {
			devmode=1;
		}
	}

	if(devmode){
		printf("\033[1;1m-->\033[0m Lexing : \n");
		printf("type\ttaille\tvaleur\n");
		char * types[] = {"string","balise","number","identifier"};
		token * t = T;
		while(t){
			printf("\033[0;3%im", t->type+1);
			printf("%s\t%i\t%s\n", types[t->type], t->size, t->value);
			t = t->next;
		}

		printf("\033[1;37m-->\033[0m Parsing : \n");
		node * R = parse(T);
		printFamilly(R,0);

		printf("\033[1;1m-->\033[0m Interpreting : \n");
		mess * resultat = (mess*) malloc(sizeof(mess));
		action(R, 0, mem, resultat);

		printf("\n\033[1;1m-->\033[0m Variables :\n");
		see_mmry(mem);

		printf("\033[0m"); //Reset the text to default color
	}else{
		mess * resultat = (mess*) malloc(sizeof(mess));
		strcpy(resultat->cval,"µ\0");
		resultat->type=Filum;
		action(parse(T),0,mem,resultat);
	}
	
	return 0;
} // nice number of lines ;)