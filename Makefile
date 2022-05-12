all: src/main.c
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/helloworld.µ
dev:
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/helloworld.µ -dev
clean:
	$(RM) dicke
