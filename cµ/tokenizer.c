#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* les types:
0: string
1: balise
2: number
3: identifier
*/
const char exemple[]="<µ>\n<loq> || Hello world ! || </loq>\n</µ>\n";

int isletter(char s){return ('a'<=s && s<='z') || ('A'<=s && s<='Z');}
int isnumber(char s){return ('0'<=s && s<='9') || s=='.' || s=='-';}

typedef struct token {
  int type;
  char value[100];
  struct token * next;
}token ;

token * tokenize(const char text[],int len){
  token * tokens = (token*)malloc(sizeof(token));
  tokens->next=malloc(sizeof(token));
  token * using = tokens->next;
  int index=0;
  char c=text[index];
  while(index<len&&c!='\0'){
    char c=text[index];
    if(c==' ' || c=='\n' || c=='\t'){ index++;}
    else if(c=='|' && index+1<len){
      int start=index;
      if(text[index+1]=='|'){
        index++;
        while(text[index]!='|' && text[index+1]!= '|'){index++;}
        index+=2;
      }
      using->next=malloc(sizeof(token));
      using=using->next;
      using->type=0;
      int e=0;
      char p[index-start-4+1];
      for(int i=start+2;i<index-2;){p[e]=text[i];e++;}
      p[e+1]='\0';
      strcpy(using->value,p);
    }else if(c=='<'){
      char name[100];
      index++;
      int e=0;
      while(index<len && text[index] !='>'){
        name[e]=text[index];
        e++;
        index++;
      }
      index++;
      using->next=malloc(sizeof(token));
      using=using->next;
      using->type=1;
      name[e+1]='\0';
      strcpy(using->value,name);
    }else if(isnumber(c)){
      char name[100];
      index++;
      int e=0;
      while(index<len && isnumber(text[index])){
        name[e]=text[index];
        e++;
        index++;
      }
      using->next=malloc(sizeof(token));
      using=using->next;
      using->type=2;
      name[e+1]='\0';
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
    using->next=malloc(sizeof(token));
    using=using->next;
    using->type=3;
    name[e+1]='\0';
    strcpy(using->value,name);
  }else{
    printf("Pas compris : %c ( place dans utf : %i)\n",c,c );
    index++;
  }

  }
  return tokens;
}

int main(int argc, char const *argv[]) {
  token* t=tokenize(exemple,sizeof(exemple)/sizeof(exemple[0]));
  while(t->next){
    printf("%s\n",t->value);
    t=t->next;
  }
  return 0;
}
