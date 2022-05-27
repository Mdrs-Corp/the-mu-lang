all: src/main.c
	@gcc -g -Wall -o dicke src/main.c
	./dicke muPrograms/numberus.µ 
clean:
	$(RM) dicke
	$(RM) */a.out
