
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
mess action(node * nod){
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
                    mess a=action(nod->child);
                    if(a.type==1){
                        printf("%i\n", a.ival);
                    }else{
                        printf("%s\n", a.cval);
                    }
                }
            }else if(strcmp(nod->content, Addere)==0){
                int s=0;
                node * c;
                c = nod->child;
                while(c){
                    s+=action(c).ival;
                    c=c->bro;
                }
                m.ival=s;
                m.type=1;
			}else{
				if(nod->child){action(nod->child);}
			}
            if(nod->bro){action(nod->bro);}
			break;
        case 2://Numerus
            m.type=1;
            m.ival=parseInt(nod->content,nod->size);
            strcpy(m.cval,nod->content);
            break;
		default:
			break;
	}
    return m;
}
