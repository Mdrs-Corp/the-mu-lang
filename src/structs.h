// Fichier qui contient toutes les structures utilisées


#define toknsize malloc(sizeof(token))
#define blocsize malloc(sizeof(bloc))
#define nodesize calloc(1,sizeof(node))

/* les types:
0: string
1: balise
2: number
3: identifier
*/

//Les tokens, pour Lexer
typedef struct token {
	struct token * next;
	char value[MAX_STRING_LEN]; // Les valeurs des tokens
	unsigned int size;
	unsigned int type:2;
}token;

//Les noeds de l'Abstract Syntax Tree
typedef struct node{
    struct node * child;
    struct node * bro;
	char content[MAX_STRING_LEN];
	unsigned int size;
	unsigned int type:2;
	unsigned int getElement:1; // si la node est consulté aka {}
}node;

//Les blocs pour la pile lors de la fabrication de l'AST
typedef struct bloc{
	struct bloc * prev;
    node * node;
}bloc;

//La communication entre balise, "messages"
typedef struct mess {
	struct mess * next;//pour les listes
    float ival;// La valeur en int si c'est un int sinon la longeur de la chaine
	char cval[MAX_STRING_LEN];// Le stockage de la chaine de char
	int type:2;// 1 pour int 2 pour char*
}mess;

//Les variables, contenues dans la liste des variables (hashés)
typedef struct var{
	mess content;
	char name[MAX_STRING_LEN];
	unsigned int isFull:1; //Si la mémoire à cet endroit est vide
}var;
