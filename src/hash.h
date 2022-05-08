// Pour faire du hashing et stocker les variables dans des hasmap
// Mais pour l'instant il n'y a que du balisage genre
int baliseEncoder(char * str){
	int result=8; // la clef qui permet un chiffrage clean :)
	int i=0;
	char c;
	while((c=str[i++])){
		result += c;
		result = (result*c)%1000;
	}
	return result;
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
void see_hash(var * vars){
	printf("NAME\ttype\tival\tcval\n");
	char types[][4]={"num\0","fil\0"};
	for (int i = 0; i < VARS_LEN; i++) {
		if(vars[i].isFull){
			printf("%s\t%s\t%i\t%s\n", vars[i].name,
			types[vars[i].content.type-1],
			vars[i].content.ival,
			vars[i].content.cval);
		}else{
			printf("---\t---\t---\t---\n");
		}
	}
	printf("\n");
}

void getVar(char * str, var * vars, mess * m){
	int location=varshasher(str);
	while(strcmp(str,vars[location].name)!=0){
		location=(location+1)%VARS_LEN;
	}
	m->type=vars[location].content.type;
	m->ival=vars[location].content.ival;
	strcpy(m->cval,vars[location].content.cval);
}

void setVar(char * str, mess * micode, var * vars){
	int location=varshasher(str);
	while((strcmp(vars[location].name,str)==0)^vars[location].isFull){
		location=(location+1)%VARS_LEN;
	}
	vars[location].isFull=1;
	strcpy(vars[location].name,str);

	vars[location].content.type=micode->type;
	vars[location].content.ival=micode->ival;
	strcpy(vars[location].content.cval,micode->cval);
}
/*int test(){
	char * name[]={"loq",
	"µ",
	"add",
	"partio",
	"mul",
	"inferioris",
	"aequalis",
	"dum",
	"si",
	"indo",
	"verum",
	"falsum",
	"et",
	"ubi",
	"ord",
	"indicium",
	"officium",
	"red",
"aeq","qua"};

	int lon = sizeof(name)/sizeof(name[0]);
	int * codes = calloc(lon,sizeof(int));
	for(int i=0;i<lon;i++){
		printf("%i\t name: %s \t code: %i\n",
				i,
				name[i],
				codes[i]=strtoint(name[i])
				);
	}
	for (size_t i = 0; i < lon; i++) {
		for (size_t j = i; j < lon; j++) {
			if (codes[i]==codes[j] && i!=j) {
				printf("same shit %i %i\n",i,j);
			}
		}
	}
}
*/
