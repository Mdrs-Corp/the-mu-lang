
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


const char *Loqum="loq";
const char *Addere="add";
mess action(node * nod,int doBro){
    mess m;
    m.type=0;// Null
    m.ival=0;
	switch (nod->type){
		case 0: // String
            m.type=2;
            strcpy(m.cval,nod->content);
			break;

		case 1://Balise
			if(strcmp(nod->content, Loqum)==0){
                if(nod->child){
                    mess a=action(nod->child,0);
                    if(a.type==1){
                        printf("%i\n", a.ival);
                    }else{
                        printf("%s\n", a.cval);
                    }
                }
            }else if(strcmp(nod->content, Addere)==0){
                m.type=1;
                int s=0;
                node * c = nod->child;
                do{
                    s+=action(c,0).ival;
                }while((c=c->bro));
                m.ival=s;
			}else{// Balise inconnue ou inutile (µ par exemple)
				if(nod->child){action(nod->child,1);}
			}
			break;
        case 2://Numerus
            m.type=1;
            m.ival=parseInt(nod->content,nod->size);
            strcpy(m.cval,nod->content);
            break;
		default:
			break;
	}
	if(nod->bro && doBro){action(nod->bro,1);}
    return m;
}
