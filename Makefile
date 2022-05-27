all: src/main.c
	@gcc -g -Wall -o dicke src/main.c
dev:
	@gcc -g -Wall -o dicke src/main.c
clean:
	$(RM) dicke
	$(RM) */a.out
