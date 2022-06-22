all: src/main.c
	@gcc -g -Wall -o dicke src/main.c
	./dicke muPrograms/numberus.µ 

compile:
	gcc -g -Wall -o dicke src/main.c
clean:
	$(RM) dicke
	$(RM) */a.out
