#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define size malloc(sizeof(token))
/* les types:
0: string
1: balise
2: number
3: identifier
*/

const char exemple[]="<µ><a></a> 12 ||allah est grand||   58 <a> ||squid game||</µ>";

int isletter(char s){return ('a'<=s && s<='z') || ('A'<=s && s<='Z');}
int isnumber(char s){return ('0'<=s && s<='9') || s=='.' || s=='-';}

typedef struct token {
  int type;
  char value[100]; // Les valeurs des tokens sont ainsi limités à 100 caractères
  struct token * next;
}token ;

token * tokenize(const char text[],int len){
	token * tokens = (token*) size;
	tokens -> next = (token*) size;
	token * using = tokens -> next;
	int index=0;
	char c;
	while(index < len-1 ){
		c=text[index];
		if(c==' ' || c=='\n' || c=='\t'){
			index++;
        }else if(c=='<'){
			char name[100];
			int e=0;
            index++;
			while(index<len && text[index] !='>'){
				name[e++]=text[index++];
			}
            index++;
			using->next=(token *) size;
			using=using->next;
			using->type=1;
			name[e]='\0';
			strcpy(using->value,name);
        }else if(isnumber(c)){
			char name[100];
			int e=0;
			while(index<len && isnumber(text[index])){
				name[e++]=text[index++];
			}
			using->next=(token *) size;
			using=using->next;
			using->type=2;
			name[e]='\0';
			strcpy(using->value,name);
		}else if(isletter(c)){
			char name[100];
			index++;
			int e=0;
			while(index<len && isletter(text[index])){
				name[e]=text[index];
				e++;
				index++;
			}
			using->next=(token*) size;
			using=using->next;
			using->type=3;
			name[e+1]='\0';
			strcpy(using->value,name);
        }else if(c=='|'){
			int lenOfStr=0;
            char name[100];
            index+=2;
			while(!(text[index]=='|' && text[index+1]== '|')){
				name[lenOfStr++]=text[index++];
			}
            index+=2;
			using->next=(token*)size;
			using=using->next;
			using->type=0;
			name[lenOfStr]='\0';
			strcpy(using->value,name);
		}else{
			printf("Pas compris : %c ( place dans utf : %i)\n",c,c );
			index++;
		}
	}
	return tokens->next->next;
}

int main(int argc, char const *argv[]) {
	token * t = tokenize(exemple,sizeof(exemple)/sizeof(exemple[0]));
	while(t){
		printf("Type : %i Valeur : %s\n",t->type, t->value);
		t=t->next;
	}
	return 0;
}
