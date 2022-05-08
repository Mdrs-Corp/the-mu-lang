
/*
# les types:
0: string
1: balise
2: number
3: identifier

# les nodes:
int type;
char content[MAX_STRING_LEN];
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

/*
0	 name: loq 	 code: 746
1	 name: µ 	 code: -475
2	 name: add 	 code: 0
3	 name: partio 	 code: 936
4	 name: mul 	 code: 984
5	 name: inferioris 	 code: 100
6	 name: aequalis 	 code: 400
7	 name: dum 	 code: 382
8	 name: si 	 code: 250
9	 name: indo 	 code: 321
10	 name: verum 	 code: 668
11	 name: falsum 	 code: 227
12	 name: et 	 code: 500
13	 name: ubi 	 code: 695
14	 name: ord 	 code: 200
15	 name: indicium 	 code: 747
16	 name: officium 	 code: 147
17	 name: red 	 code: 900
18	 name: aeq 	 code: 887
19	 name: qua 	 code: 119
*/
mess action(node * nod,int doBro){
    mess m={.type=0,.ival=0}; // le message à renvoyer
	int s;// lorsqu'on fait des sommes, ou l'equivalent
	int good=1; // lorsqu'on fait du Verum/Falsum
	node * c = nod->child; // le premier enfant amen
	switch (nod->type){
		case 0: // String
            m.type=2;
            strcpy(m.cval,nod->content);
			break;
		case 1://Balise
			switch (baliseEncoder(nod->content)) {
				case 746://loq
					while(c){
						mess a = action(c,0);
						if(a.type==1){
							printf("%i\n", a.ival);
						}else{
							printf("%s\n", a.cval);
						}
						c=c->bro;
	                }
					break;
				case 0://Addere
					m.type=1;
	                s=0;
	                do{
	                    s+=action(c,0).ival;
	                }while((c=c->bro));
	                m.ival=s;
					break;
				case 984://Multiplicare
                	m.type=1;
                	s=1;
                	do{
                    	s*=action(c,0).ival;
                	}while((c=c->bro));
                	m.ival=s;
					break;
				case 936://Partiorum
                	m.type=1;
					s = action(c,0).ival;
                	while((c=c->bro)){
                    	s=s/action(c,0).ival;
                	};
                	m.ival=s;
					break;
				case 100://inferioris
					m.type=1;
					s = action(c,0).ival;
					while((c=c->bro) && good){
						if (s>action(c,0).ival) {
							good=0;
						}
						s=action(c,0).ival;
					};
					m.ival=good;
					break;
				case 400://aequalis
					m.type=1;
					s = action(c,0).ival;
					while((c=c->bro) && good){
						if (s!=action(c,0).ival) {
							good=0;
						}
						s=action(c,0).ival;
					};
					m.ival=good;
					break;
				case 382://dum
					while(action(c,0).ival){
						action(c->bro,1);
					}
					break;
				case 250://si
					if(action(c,0).ival){
						action(c->bro,1);
					}
					break;
				case 321://indo
					setVar(c->content,action(c->bro,0));
				default:// Balise inconnue ou inutile (µ par exemple)
					if(c){action(c,1);}
			}
			break;
        case 2://Numerus
            m.type=1;
            m.ival=parseInt(nod->content,nod->size);
            strcpy(m.cval,nod->content);
            break;
		case 3:
			m=getVar(nod->content);
		default:
			break;
	}
	if(nod->bro && doBro){action(nod->bro,1);}
    return m;
}
