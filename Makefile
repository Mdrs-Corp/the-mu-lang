all: src/main.c
	gcc -g -Wall -o dicke src/main.c
	./dicke ./muPrograms/comparator.µ
clean:
	$(RM) dicke
