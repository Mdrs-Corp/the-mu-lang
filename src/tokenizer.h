/* Transforme le texte en suite d'instructions */

int isletter(char s){return ('a'<=s && s<='z') || ('A'<=s && s<='Z');}
int isnumber(char s){return ('0'<=s && s<='9') || s=='.' || s=='-';}

token * tokenize(char text[],int len){
	token * tokens = (token*) toknsize;
	tokens -> next = (token*) toknsize;
	token * using = tokens -> next;
	int index=0;
	char c;
	while(index < len-1){
		c=text[index];
		if(c==' ' || c=='\n' || c=='\t'){
			index++;
        }else if(c=='<'){
			char name[MAX_STRING_LEN];
			int e=0;
            index++;
			while(index<len && text[index] !='>'){
				name[e++]=text[index++];
			}
            index++;
			using->next=(token *) toknsize;
			using=using->next;
			using->type=1;
			using->size=e;
			name[e]='\0';
			strcpy(using->value,name);
        }else if(isnumber(c)){
			char name[MAX_STRING_LEN];
			int e=0;
			while(index<len && isnumber(text[index])){
				name[e++]=text[index++];
			}
			using->next = (token *) toknsize;
			using = using->next;
			using->type=2;
			using->size=e;
			name[e]='\0';
			strcpy(using->value,name);
		}else if(isletter(c)){
			char name[MAX_STRING_LEN];
			index++;
			int e=0;
			while(index<len && isletter(text[index])){
				name[e]=text[index];
				e++;
				index++;
			}
			using->next=(token*) toknsize;
			using=using->next;
			using->type=3;
			using->size=e;
			name[e+1]='\0';
			strcpy(using->value,name);
        }else if(c=='|'){
			int lenOfStr=0;
            char name[MAX_STRING_LEN];
            index+=2;
			while(!(text[index]=='|' && text[index+1]== '|')){
				name[lenOfStr++]=text[index++];
			}
            index+=2;
			using->next=(token*) toknsize;
			using=using->next;
			using->type=0;
			using->size=lenOfStr;
			name[lenOfStr]='\0';
			strcpy(using->value,name);
		}else{
			printf("Pas compris : %c ( place dans utf : %i)\n",c,c );
			index++;
		}
	}
	return tokens->next->next;
}


token * tokenizeFromFile(const char *path){
	char c=0;//Current char
	char nc=0;//Next char
	FILE *filePointer;
	char move(){ // Oui, c'est mal...
		c = nc;
		nc = fgetc(filePointer);
		return c;
	}
    filePointer = fopen(path, "r");
	if (filePointer == NULL){
        printf("File is not available \n");
    }

	token * tokens = (token*) toknsize;
	tokens -> next = (token*) toknsize;
	token * using = tokens -> next;
	move();
	while(c!= EOF){
		if(c==' ' || c=='\n' || c=='\t'){
			move();
        }else if(c=='<'){
			char name[MAX_STRING_LEN];
			int e=0;
			while(nc!=EOF && nc !='>'){
				name[e++]=move();
			}
            move();
			move();
			using->next=(token *) toknsize;
			using=using->next;
			using->type=1;
			using->size=e;
			name[e]='\0';
			strcpy(using->value,name);

        }else if(isnumber(c)){
			char name[MAX_STRING_LEN];
			int e=0;
			while(nc!=EOF && isnumber(c)){
				name[e]=c;
				e++;
				move();
			}
			using->next = (token *) toknsize;
			using = using->next;
			using->type = 2;
			using->size = e;
			name[e] = '\0';
			strcpy(using->value, name);

		}else if(isletter(c)){
			char name[MAX_STRING_LEN];
			int e=0;
			while(nc!=EOF && isletter(c)){
				name[e]=c;
				e++;
				move();
			}
			using->next = (token *) toknsize;
			using = using->next;
			using->type = 3;
			using->size = e;
			name[e] = '\0';
			strcpy(using->value, name);

        }else if(c=='|'){
			int lenOfStr=0;
            char name[MAX_STRING_LEN];
			move();
			move();
			do{
				name[lenOfStr++]=c;
				move();
			}while(!(c=='|' && nc=='|'));
            move();
			move();
			using->next=(token*) toknsize;
			using=using->next;
			using->type=0;
			using->size=lenOfStr;
			name[lenOfStr]='\0';
			strcpy(using->value,name);
		}else{
			printf("Pas compris : %c ( place dans utf : %i)\n",c,c );
			move();
		}
	}
	fclose(filePointer);
	return tokens->next->next;
}
