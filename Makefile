all: main.c
	gcc -g -Wall -o dicke main.c
	./dicke
clean:
	$(RM) dicke
