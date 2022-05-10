all: src/main.c
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/numberus.µ
dev:
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/numberus.µ -dev
clean:
	$(RM) dicke
