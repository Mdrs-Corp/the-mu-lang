
/*
# les types:
0: string
1: balise
2: number
3: identifier

# les nodes:
int type;
char content[100];
struct node * child;
struct node * bro;
*/

int parseInt(const char *num,int len){
  int result=0;
  int current;
  int puis=1;
  for(int i = len;i>0;i--){
    current=69;
    for (int n = 48; n < 58; n++) {
      if (n==num[i-1]) {
        current=n-48;
        n=69; // On a trouvé qui c'était, on sort
      }
    }
    if (current==69) {
      //printf("Not a Number (on fait pas du JS non plus)\n");
      //i=-1; // On a pas trouvé, ce n'est pas un chiffre, on sort :(
    }else{
      result+=current*puis;
      puis*=10;
    }
  }
  return result;
}

int charCompartion(char * a, char * b, int len){
	for (int i = 0; i < len; i++) {
		if(a[i]!=b[i]){
			return 0;
		}
	}
	return 1;
}

char * action(node * node){
	switch (node->type){
		case 0:
			return node->content;
			break;
		case 1:
			if(node->content=="loq"){
				printf("%s\n", action(node));
				return "";
			}else{
				printf("pas un loq : %s\n", node->content );
				if(node->child){action(node->child);}
				if(node->bro){action(node->bro);}
				return "";
			}
			break;
		default:
			return "";
			break;

	}
}
