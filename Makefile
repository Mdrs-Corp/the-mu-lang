all: src/main.c
	gcc -g -Wall -o dicke src/main.c
	./dicke ./muPrograms/autoclosing.µ
clean:
	$(RM) dicke
