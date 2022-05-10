all: src/main.c
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/ordiniat.µ
dev:
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/ordiniat.µ -dev
clean:
	$(RM) dicke
