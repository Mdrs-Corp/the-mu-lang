/*
Fichier qui contient toutes les structures utilisées
*/

#define toknsize malloc(sizeof(token))
#define blocsize malloc(sizeof(bloc))
#define nodesize malloc(sizeof(node))

/* les types:
0: string
1: balise
2: number
3: identifier
*/

//Les tokens
typedef struct token {
  int type;
  char value[100]; // Les valeurs des tokens sont ainsi limités à 100 caractères
  int size;
  struct token * next;
}token;

//Les noeds de l'AST
typedef struct node{
    int type;
    char content[100];
    int size;
    struct node * child;
    struct node * bro;
}node;

//Les blocs pour la pile lors de l'AST
typedef struct bloc{
    node * node;
    struct bloc * prev;
}bloc;

//La communication entre balise
typedef struct mess{
    int type;// 1 pour int 2 pour char*
    int ival;// La valeur en int si c'est un int sinon la longeur de la chaine
    char cval[100];// Le stockage de la chaine de char
}mess;
