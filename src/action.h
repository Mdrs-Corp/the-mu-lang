// Executer le contenu de l'arbre
void action(node * nod, int doBro, var*vars, mess * m);
float parseInt(const char *num,int len){
  float result = 0;
  int puis = 1;
  int current; // Le caractère actuel
  int n;// Le nombre auquel cela correspond
  for(int i = len; i>0 ;i--){
    current=69;
	if (num[i-1]==46) {// si on tombe sur un point
		result/=puis;
		puis=1;
	}else{//sinon c'est un chiffre
		for (n = 48; n < 58; n++) {
	      if (n == num[i-1]) {
	        current = n-48;
	        n = 420; // On a trouvé qui c'était, on sort
	      }
	    }
	}

	if (current!=69) {
	    result+=current*puis;
	    puis*=10;
    }
  }
  return result;
}
void consulted(mess * m, node * c, mess * a,  var*vars, char * string){
	m->ival=1;
	action(c,0,vars,a);
	m->cval[0] = string[(int)a->ival];
	m->cval[1] = '\0';
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
18	 name: qua/		code: 802
19	 name: qua 	 code: 119
20 	 name: variabilis/ code :9
*/

void action(node * nod, int doBro, var*vars, mess * m){
	// On commence par un petit ménage, on ne sait pas où il a trainé :
	m->type = 0;
	m->ival = 0;
	node * c = nod->child; // le premier enfant amen
	mess * a = (mess*) calloc(1,sizeof(mess));// va se faire charcuter par les gosses
	int s;// lorsqu'on fait des sommes, ou l'equivalent
	mess * first; // Pour se souvenir du premier membre d'une liste

	switch (nod->type){
		case 0: // String
			m->type=2;
			if(nod->getElement){ // si on le prend à un certain index
				consulted(m,c,a,vars,nod->content);
			}else{
				m->ival=nod->size;
				strcpy(m->cval,nod->content);
			}
			break;
		case 1://Balise
			switch (baliseEncoder(nod->content)) {//Quel type ?
				case -475:case 747://µ, indicium
					if(c){action(c,1,vars,m);}
					break;
				case 0://Addere
					m->type = 1;
	                m->ival = 0;
	                do{
						action(c,0,vars,a);
	                    m->ival += a->ival;
	                }while((c=c->bro));
					break;
				case 984://Multiplicare
                	m->type = 1;
                	m->ival = 1;
                	do{
						action(c,0,vars,a);
                    	m->ival *= a->ival;
                	}while((c=c->bro));
					break;
				case 936://Partiorum
					action(c,0,vars,m);
					m->type = 1;
                	while((c=c->bro)){
						action(c,0,vars,a);
                    	m->ival /= a->ival;
                	};
					break;

				case 100://inferioris
					m->type = 1;
					m->ival = 1;
					action(c,0,vars,a);
					s = a->ival;
					while((c=c->bro) && m->ival){
						action(c,0,vars,a);
						if (s > a->ival) {
							m->ival = 0;
						}
						action(c,0,vars,a);
						s = a->ival;
					};
					break;
				case 400://aequalis
					m->type = 1;
					m->ival = 0;
					action(c,0,vars,a);
					s = a->ival;
					while((c=c->bro) && m->ival){
						action(c,0,vars,a);
						if (s != a->ival) {
							m->ival = 0;
						}
						action(c,0,vars,a);
						s = a->ival;
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
						action(c->bro,0,vars,m);
						setVar(c->content,m,vars);
						c = c->bro->bro;
					}
					break;
				case 500://et
					m->type = 1;
					m->ival = 1;
					do{
						action(c,0,vars,a);
						m->ival = a->ival && m->ival;
					}while((c = c->bro));
					break;
				case 695://ubi
					m->type = 1;
					m->ival = 0;
					do{
						action(c,0,vars,a);
						m->ival = a->ival || m->ival;
					}while((c = c->bro));
					break;
				case 227: //verum
					m->type = 1;
					m->ival = 1;
					break;
				case 668: //falusm
					m->type = 1;
					m->ival = 0;
					break;
				case 746://loq
					while(c){
						action(c,0,vars,m);
						if(m->type==1){
							printf("%g", m->ival);
						}else{
							printf("%s", m->cval);
						}
						c = c->bro;
					}
					printf("\n");
					break;
				case 200://ordinata ou "ord"
					first = m;
					do{
						action(c,0,vars,m);
						//a = (mess*) malloc(sizeof(mess));
						m->next = a;
						m = a;
					}while((c=c->bro));
					m = first;
					while(m->next){
						//printf("%i",(int)m->ival);
						m=m->next;
					}
					//printf("Le second vaut : %g\n",m->next->ival);
					break;
				case 119:case 802://qua et qua/
					m->type = 2;
					while(c){
						action(c,0,vars,a);
						if(a->type==1){
							printf("%g", a->ival);
						}else{
							printf("%s", a->cval);
						}
						c = c->bro;
					}
					scanf("%[^\n]", m->cval);
					char k;
					s = 1;// es ce que c'est un Numerus ?
					m->ival = 0;
					while((k=m->cval[(int)m->ival])){
						s=isnumber(k) && s;
						m->ival++;
					}
					if(s){
						m->type = 1;
						m->ival = parseInt(m->cval,m->ival);
					}
					break;
				case 9:// variabilis
					see_hash(vars);
					break;
				default:// Balise inconnue ou mal hashé (par mentié)
					printf("Unknnow hashed: %i (%s)\n",baliseEncoder(nod->content),nod->content);
					if(c){action(c,1,vars,m);}
			}
			break;
        case 2://Numerus
            m->type = 1;
            m->ival = parseInt(nod->content,nod->size);
            strcpy(m->cval,nod->content);
            break;
		case 3://identifier
			getVar(nod->content,vars,m);
			if(nod->getElement){
				consulted(m,c,a,vars,m->cval);
			}
		default:
			break;
	}
	if(nod->bro && doBro){action(nod->bro,1,vars,a);}
}
