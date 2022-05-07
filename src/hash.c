// Pour faire du hashing et stocker les variables dans des hasmap

#include <stdio.h>
#include <stdlib.h>
int mupow(int a, int b){
	int r=1;
	for(int i=0; i<b; i++){
		r*=a;
	}
	return r;
}

int strtoint(char * str){
	int result=0;
	int i=0;
	char c;
	while(c=str[i++]){
		//printf("%i %c\n",str[i]-96,str[i]);
		result += c-96;
		result ^= c-96;
		result = (result*result)%1000;
	}
	return result;
}
int main(){
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
	"red"};
	for(int i=0;i<sizeof(name)/sizeof(name[0]);i++){
		printf("name: %s \t code: %i\n",
				name[i],
				strtoint(name[i])
				);
	}
}
