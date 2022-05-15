// Pour faire du hashing et stocker les variables dans des hasmap
int baliseEncoder(char * str){
	unsigned int result=8; // la clef qui permet un chiffrage clean pour les mu balises :)
	int i=0;
	char c;
	while((c=str[i++])){
		result += c;
		result = (result*c)%1000;
	}
	if(!result){result=1;}
	return (int)result*result/result;
}

int varshasher(char * str){
	int result=0;
	int i=0;
	char c;
	while((c=str[i++])){
		result += c;
		result = (result*c)%VARS_LEN;
	}
	return result;
}

void see_mmry(struct memory mem){
	printf("\033[0;33mNAME\t\033[0;34mTYPE\t\033[0;35mIVAL\t\033[0;36mCVAL\n\033[0m");
	char types[][4]={"num","fil","ord"};
	for (int i = 0; i < VARS_LEN; i++) {
		if(mem.vars[i].isFull){
			printf("\033[0;33m%s\t\033[0;34m%s\t\033[0;35m%g\t\033[0;36m%s\n\033[0m",
			mem.vars[i].name,
			types[mem.vars[i].content.type-1],
			mem.vars[i].content.ival,
			mem.vars[i].content.cval);
		}else{
			printf("---\t---\t---\t---\n");
		}
	}
	printf("\nAnd declared functions are : ");
	for (int i = 0; i < FUNS_LEN; i++) {
		if(mem.funs[i].isFull){
			printf("%s,",mem.funs[i].name);
		}
	}
	printf("\n");
}

void getVar(char * str, var * vars, mess * m){
	int location = varshasher(str);
	while(strcmp(str,vars[location].name)!=0){
		location = (location+1)%VARS_LEN;
	}
	m->type = vars[location].content.type;
	m->ival = vars[location].content.ival;
	m->next = vars[location].content.next;
	strcpy(m->cval,vars[location].content.cval);
}

void setVar(char * str, mess * micode, var * vars){
	int location = varshasher(str);
	while((strcmp(vars[location].name,str)==0)^vars[location].isFull){
		location = (location+1)%VARS_LEN;
	}
	vars[location].isFull = 1;
	strcpy(vars[location].name,str);

	vars[location].content.type = micode->type;
	vars[location].content.ival = micode->ival;
	vars[location].content.next = micode->next;
	strcpy(vars[location].content.cval,micode->cval);
	//printf("Setted %s to %i\n", str,(int) micode->ival);
}

void setFun(node * c, fun * funs){
	c->content[c->size-1]='\0';
	int location = baliseEncoder(c->content)%FUNS_LEN;
	while((strcmp(funs[location].name,c->content)==0)^funs[location].isFull){
		location = (location+1)%FUNS_LEN;
	}
	funs[location].isFull = 1;
	strcpy(funs[location].name,c->content);
	funs[location].args = c->bro;
}
fun getFun(node * nod, fun * funs){
	int location = baliseEncoder(nod->content)%FUNS_LEN;
	while(strcmp(nod->content,funs[location].name)!=0){
		location = (location+1)%FUNS_LEN;
	}
	return funs[location];
}

/*
int main(){ // pour vérifier si deux balises ont le même hash
	char * name[]={"loq","µ","add","partio","mul",
	"inferioris","aequalis","dum","si","indo","verum/",
	"falsum/","et","ubi","ord","indicium","officium",
	"red","qua/","qua","variabilis/"};
	int lon = sizeof(name)/sizeof(name[0]);
	printf("%i elements to scan\n",lon);
	int * codes = malloc(lon*sizeof(int));
	int i,j;
	for(i = 0; i < lon;i++){
		printf("Encoding %s...\n",name[i]);
		codes[i]=baliseEncoder(name[i]);
		printf("%i\t name: %s \t code: %i\n",i,name[i],codes[i]);
	}
	fprintf (stderr, "Internal error: "
                 "negative string length "
                 "%d at %s, line %d.",
         181, __FILE__, __LINE__);
	printf("nada qaui");
	for (i = 0; i < lon; i++) {
		for (j = 0; j < lon; j++) {
			if (codes[i] == codes[j] && i!=j) {
				printf("same shit %i %i\n",i,j);
			}
		}
	}
	printf("Nothing is the same :)");
	return 0;
}
*/
