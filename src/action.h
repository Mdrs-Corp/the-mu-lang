
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
#define msgcpy(a, b) strcpy(a.cval,b.cval);a.type=b.type;a.ival=b.ival
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
19	 name: qua 	 code: 119
*/
void action(node * nod, int doBro, var*vars, mess * m){
	int s;// lorsqu'on fait des sommes, ou l'equivalent
	node * c = nod->child; // le premier enfant amen
	// On fait le ménage quand même:
	m->type=0;
	m->ival=0;
	mess * a = (mess*) calloc(1,sizeof(mess));// va se faire charcuter par les gosses

	switch (nod->type){
		case 0: // String
            m->type=2;
			m->ival=nod->size;
            strcpy(m->cval,nod->content);
			break;
		case 1://Balise
			switch (baliseEncoder(nod->content)) {
				case -475://µ
					if(c){action(c,1,vars,m);}
					break;

				case 0://Addere
					m->type=1;
	                m->ival=0;
	                do{
						action(c,0,vars,a);
	                    m->ival+=a->ival;
	                }while((c=c->bro));
					break;
				case 984://Multiplicare
                	m->type=1;
                	m->ival=1;
                	do{
						action(c,0,vars,a);
                    	m->ival*=a->ival;
                	}while((c=c->bro));

					break;
				case 936://Partiorum
                	m->type=1;
					action(c,0,vars,m);
                	while((c=c->bro)){
						action(c,0,vars,a);
                    	m->ival/=a->ival;
                	};

					break;
				case 100://inferioris
					m->type=1;
					m->ival=1;
					action(c,0,vars,a);
					s=a->ival;
					while((c=c->bro) && m->ival){
						action(c,0,vars,a);
						if (s>a->ival) {
							m->ival=0;
						}
						action(c,0,vars,a);
						s=a->ival;
					};
					break;
				case 400://aequalis
					m->type=1;
					action(c,0,vars,a);
					s = a->ival;
					m->ival=0;
					while((c=c->bro) && m->ival){
						action(c,0,vars,a);
						if (s!=a->ival) {
							m->ival=0;
						}
						action(c,0,vars,a);
						s=a->ival;
					};
					break;
				case 382://dum
					action(c,0,vars,m);
					while(m->ival){
						action(c->bro,1,vars,a);
						action(c,0,vars,m);
					}
					break;
				case 250://si
					action(c,0,vars,m);
					if(m->ival){
						action(c->bro,1,vars,a);
					}
					break;
				case 321://indo
					while(c){
						char * variablename=c->content;
						action(c->bro,0,vars,m);
						setVar(variablename,m,vars);
						c=c->bro->bro;
					}
					break;
				case 500://et
					m->type=1;
					m->ival=1;
					do{
						action(c,0,vars,a);
						m->ival=a->ival && m->ival;
					}while((c=c->bro));
					break;
				case 695://ubi
					m->type=1;
					m->ival=0;
					do{
						action(c,0,vars,a);
						m->ival=a->ival || m->ival;
					}while((c=c->bro));
					break;
				case 227: //verum
					m->type=1;
					m->ival=1;
					break;
				case 668: //falusm
					m->type=1;
					m->ival=1;
					break;
				case 746://loq
					while(c){
						action(c,0,vars,m);
						if(m->type==1){
							printf("%g", m->ival);
						}else{
							printf("%s", m->cval);
						}
						c=c->bro;
					}
					printf("\n");
					break;
				case 119:
					m->type=2;
					while(c){
						action(c,0,vars,a);
						if(a->type==1){
							printf("%g", a->ival);
						}else{
							printf("%s", a->cval);
						}
						c=c->bro;
					}
					scanf("%[^\n]", m->cval);
					char k;
					s=1;
					m->ival=0;
					while((k=m->cval[(int)m->ival])){
						s=isnumber(k) && s;
						m->ival++;
					}
					if(s){
						m->type=1;
						m->ival=parseInt(m->cval,m->ival);
					}
					break;

				default:// Balise inconnue ou inutile (µ par exemple)
					printf("Unknnow hashed: %i (%s)\n",baliseEncoder(nod->content),nod->content);
					if(c){action(c,1,vars,m);}
			}
			break;
        case 2://Numerus
            m->type=1;
            m->ival=parseInt(nod->content,nod->size);
            strcpy(m->cval,nod->content);
            break;
		case 3://identifier
			getVar(nod->content,vars,m);
		default:
			break;
	}
	if(nod->bro && doBro){action(nod->bro,1,vars,a);}
}
