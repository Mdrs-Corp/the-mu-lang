// Fichier qui contient toutes les structures utilisées


#define toknsize malloc(sizeof(token))
#define blocsize malloc(sizeof(bloc))
#define nodesize calloc(1,sizeof(node))
// Les types de messages/variables
#define Numerus 1
#define Filum 2
#define Ordinata 3

// Les types de tokens/nodes:
#define STRING 0
#define BALISE 1
#define CONSTT  2
#define IDENTIFIER 3


//Les tokens, pour Lexer
typedef struct token {
	struct token * next;
	char value[MAX_STRING_LEN]; // Les valeurs des tokens
	unsigned int size;
	unsigned int type:2;
	unsigned int line;
}token;

//Les noeds de l'Abstract Syntax Tree
typedef struct node{
    struct node * child;
    struct node * bro;
	char content[MAX_STRING_LEN];
	unsigned int size;
	unsigned int type:2;
	unsigned int line;
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
	unsigned int type:2;// 1 pour int 2 pour char* 3 pour ordinata
    union{
    	float ival;// La valeur en int si c'est un int sinon la longeur de la chaine
		char cval[MAX_STRING_LEN];// Le stockage de la chaine de char
	};
}mess;

//Les variables, contenues dans la liste des variables (hashés)
typedef struct var{
	unsigned int isFull:1; //Si la mémoire à cet endroit est vide
	char name[MAX_STRING_LEN];
	mess content;
}var;

typedef struct fun{
	unsigned int isFull:1; //Si la mémoire à cet endroit est vide
	node * args;
	char name[MAX_STRING_LEN];
}fun;

struct memory{
	fun * funs;
	var * vars;
};
