/*
Fichier qui contient toutes les structures utilisées
*/

#define toknsize malloc(sizeof(token))
#define blocsize malloc(sizeof(bloc))
#define nodesize calloc(1,sizeof(node))

/* les types:
0: string
1: balise
2: number
3: identifier
*/

//Les tokens
typedef struct token {
  int type;
  char value[MAX_STRING_LEN]; // Les valeurs des tokens
  unsigned int size;
  struct token * next;
}token;

//Les noeds de l'AST
typedef struct node{
    unsigned int type;
    char content[MAX_STRING_LEN];
    unsigned int size;
    struct node * child;
    struct node * bro;
	int getElement; // si la node est consulté
}node;

//Les blocs pour la pile lors de la fabrication de l'AST
typedef struct bloc{
    node * node;
    struct bloc * prev;
}bloc;

//La communication entre balise
typedef struct mess {
    int type;// 1 pour int 2 pour char*
    float ival;// La valeur en int si c'est un int sinon la longeur de la chaine
    char cval[MAX_STRING_LEN];// Le stockage de la chaine de char
}mess;

typedef struct var{
	char name[MAX_STRING_LEN];
	unsigned int isFull:1;
	mess content;
}var;
