#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STRING_LEN 100
#define VARS_LEN 10             // Nombre de variables
#define FUNS_LEN 10             // Nombre de fonctions

// paramètres d'execution
#define DEVMODE 1
#define PRINTRETURN 2

/* Ordre important, le compileur va vraiment yank les contenus à la suite
   Et les mettres dans ce fichier afin d'executer un gros */

#include "structs.c"
#include "tokenizer.c"
#include "parser.c"
#include "alerts.c"
#include "hash.c"
#include "action.c"

int main(int argc, char const *argv[])
{
  struct memory mem;
  mem.vars = (var *) calloc(VARS_LEN, sizeof(var));
  mem.funs = (fun *) calloc(FUNS_LEN, sizeof(fun));
  token *T;

  if (argc >= 2 && argv[1][0] != '-') {
    T = tokenizeFromFile(argv[1]);
  } else {
    printf("Interpreting from built-in exemple : \n");
    T = tokenizeFromFile("./src/exemple.µ");
  }

  int params = 0;
  for (size_t i = 0; i < argc; i++) {
    if (strcmp(argv[i], "-dev") == 0) {
      params |= DEVMODE;
    } else if (strcmp(argv[i], "-µ") == 0) {
      params |= PRINTRETURN;
    }
  }

  mess *resultat = (mess *) malloc(sizeof(mess));

  strcpy(resultat->cval, "µ\0");
  resultat->type = Filum;
  if (params & DEVMODE) {
    printf("\033[1;1m-->\033[0m Lexing : \n");
    printf("type\ttaille\tvaleur\n");
    char *types[] = { "string", "balise", "number", "identif" };
    token *t = T;
    while (t) {
      printf("\033[0;3%im", t->type);
      printf("%s\t%i\t%s\n", types[t->type - 1], t->size, t->value);
      t = t->next;
    }

    printf("\033[1;37m-->\033[0m Parsing : \n");
    node *R = parse(T);
    printFamilly(R, 0);

    printf("\033[1;1m-->\033[0m Interpreting : \n");
    action(R, 0, mem, resultat);

    printf("\n\033[1;1m-->\033[0m Variables :\n");
    see_mmry(mem);

    printf("\033[0m");          //Reset the text to default color
  } else
    action(parse(T), 0, mem, resultat);

  if (params & PRINTRETURN) {
    print(resultat);
    printf("\n");
  }

  return 0;
}                               // nice number of lines ;)
