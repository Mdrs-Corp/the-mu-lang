all: src/main.c
	gcc -g -Wall -o dicke src/main.c
	./dicke ./muPrograms/helloworld.µ
clean:
	$(RM) dicke
