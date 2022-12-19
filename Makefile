make: src/main.c
	@gcc -Wall -o dicke src/main.c
	./dicke muPrograms/ord.µ -dev

compile:
	gcc -Wall -o dicke src/main.c
clean:
	$(RM) dicke
	$(RM) */a.out

