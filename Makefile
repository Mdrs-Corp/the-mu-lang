all: src/main.c
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/officium.µ
dev:
	@gcc -g -Wall -o dicke src/main.c
	@./dicke ./muPrograms/officium.µ -dev
clean:
	$(RM) dicke
