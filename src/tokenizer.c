// Transforme le texte en une suite de jetons

int isletter(char s){return ('a'<=s && s<='z') || ('A'<=s && s<='Z');}
int isnumber(char s){return ('0'<=s && s<='9') || s=='.' || s=='-';}

#define SET(t) 

token * tokenizeFromFile(const char *path){
    char c;//Current char
    char nc;//Next char
    int line = 1;
    FILE *filePointer;
    filePointer = fopen(path, "r");
    if (filePointer == NULL){printf("File is not available \n");}

    char move(){ // Oui, c'est mal...
        c = nc;
        nc = fgetc(filePointer);
        return c;
    }

    token * tokens = (token*) toknsize;
    token * using = tokens;
    move();
    move();
    int e; //longeur du jeton
    int t; //type du jeton
    char name[MAX_STRING_LEN]; // Contenu du jeton
    while(nc!=EOF && c){
        e=0;
        t=0;
        if(c=='<'){
            while(nc!=EOF && nc !='>'){name[e++]=move();}
            move();
            move();
            t=BALISE;
        }
        else if(isnumber(c)){
            while(nc!=EOF && isnumber(c)){
                name[e]=c;
                e++;
                move();
            }
            t=CONSTT;
        }
        else if(isletter(c)){
            while(nc!=EOF && isletter(c)){
                name[e]=c;
                e++;
                move();
            }
            t=IDENTIFIER;
        }
        else if(c=='|'){
            move();
            move();
            do{
                name[e++]=c;
                move();
            }while(!(c=='|' && nc=='|'));
            move();
            move();
            t=STRING;
        }
        if(t){
            using->next = (token*) toknsize;
            using = using->next;
            using->type=t;
            using->size=e;
            using->line=line;
            name[e]='\0';
            strcpy(using->value,name);
        }
        else if(c=='{'){
            move();
            using->next = (token*) toknsize;
            using = using->next;
            using->type = BALISE;
            using->size = 8; //parce que "indicium" fait 8 caractères
            using->line = line;
            strcpy(using->value,"indicium");
        }
        else if(c=='}'){
            move();
            using->next = (token*) toknsize;
            using = using->next;
            using->type = BALISE;
            using->size = 9;
            using->line = line;
            strcpy(using->value,"/indicium");
        }
        else{
            if(c == ' ' || c == '\n' || c == '\t'){
                line+=(c=='\n');
              move();
            }else{

            printf("Pas compris : '%c' ( place dans utf : %i)\n",c,c);
            move();
            }
        }
    }
    fclose(filePointer);
    return tokens->next;
}
