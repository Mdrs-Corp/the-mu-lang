char *types[] = { "Numerus", "Filum", "Ordinata" };

void alert(int expeted, int got, int line, char *nod)
{
  printf("⚠ Unexpected type in %s at line %i, wanted %s but got %s!\n", nod,
         line, types[expeted - 1], types[got - 1]);
}

void error(node * nod, char *s)
{
  printf("Error at line %d: %s\n", nod->line, s);
}
