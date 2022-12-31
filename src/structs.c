// Fichier qui contient toutes les structures utilisées

// Shortcut, flemme de me répéter
#define toknsize malloc(sizeof(token))
#define blocsize malloc(sizeof(bloc))
#define nodesize calloc(1,sizeof(node))

// Les types de messages/variables
#define Numerus 1
#define Filum 2
#define Ordinata 3

// Les types de tokens/nodes:
#define STRING 1
#define BALISE 2
#define CONSTT  3
#define IDENTIFIER 4

//Les tokens, pour Lexer
typedef struct token {
  struct token *next;
  char value[MAX_STRING_LEN];   // Les valeurs des tokens
  unsigned int size;
  unsigned int type:3;
  unsigned int line;
} token;

//Les noeds de l'Abstract Syntax Tree
typedef struct node {
  struct node *child;
  struct node *bro;
  char content[MAX_STRING_LEN];
  unsigned int size;
  unsigned int type:3;
  unsigned int line;
  unsigned int getElement:1;    // si la node est consulté aka {}
} node;

//Les blocs pour la pile lors de la fabrication de l'AST
typedef struct bloc {
  struct bloc *prev;
  node *node;
} bloc;

//La communication entre balise, "messages"
typedef struct mess {
  struct mess *next;            //pour les ordinata
  unsigned int type:2;
  // attention ! soit Numerus, soit Filum, pas les deux!
  union {
    int ival;
    char cval[MAX_STRING_LEN];
  };
} mess;

//Les variables
typedef struct var {
  unsigned int isFull:1;
  char name[MAX_STRING_LEN];
  mess content;
} var;

//Les fonctions
typedef struct fun {
  unsigned int isFull:1;
  char name[MAX_STRING_LEN];
  node *args;
} fun;

struct memory {
  fun *funs;
  var *vars;
};
