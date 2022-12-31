make: src/main.c
	@gcc -Wall -o dicke src/main.c
	./dicke muPrograms/quaestio.µ  -dev

compile:
	gcc -Wall -o dicke src/main.c

clean:

	$(RM) dicke
	$(RM) */a.out
	$(RM) .repl.*

indent:
	indent src/*.c -linux -nut -i2
	rm src/*.c~
