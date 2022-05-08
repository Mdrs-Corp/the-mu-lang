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
mess getVar(char * str){
	int location=varshasher(str);
	while(strcmp(muvars[location].name,str)!=0){
		location=(location+1)%VARS_LEN;
	}
	return muvars[location].content;
}
void setVar(char * str, mess micode){
	int location=varshasher(str);
	while(strcmp(muvars[location].name,"0")){
		location=(location+1)%VARS_LEN;
	}
	muvars[location].content=micode;
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
