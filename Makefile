all: main.c
	gcc -g -Wall -o dicke main.c
	./dicke ./muPrograms/helloworld.µ
clean:
	$(RM) dicke
