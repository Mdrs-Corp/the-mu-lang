// Transforme le texte en une suite de jetons

int isletter(char s)
{
  return ('a' <= s && s <= 'z') || ('A' <= s && s <= 'Z');
}

int isnumber(char s)
{
  return ('0' <= s && s <= '9') || s == '.' || s == '-';
}

char move(char *c, char *nc, FILE * file)
{
  *c = *nc;
  *nc = fgetc(file);
  return *c;
}

token *tokenizeFromFile(const char *path)
{
  char c;                       //Current char
  char nc;                      //Next char
  int line = 1;
  FILE *f;                      //file pointeur
  f = fopen(path, "r");
  if (f == NULL) {
    printf("File is not available :,( \n");
  }

  token *tokens = (token *) toknsize;
  token *using = tokens;
  move(&c, &nc, f);
  move(&c, &nc, f);
  int e;                        //longeur du jeton
  int t;                        //type du jeton
  char name[MAX_STRING_LEN];    // Contenu du jeton
  while (nc != EOF && c) {
    e = 0;
    t = 0;
    if (c == '<') {
      while (nc != EOF && nc != '>')
        name[e++] = move(&c, &nc, f);
      move(&c, &nc, f);
      move(&c, &nc, f);
      t = BALISE;
    } else if (isnumber(c)) {
      while (nc != EOF && isnumber(c)) {
        name[e] = c;
        e++;
        move(&c, &nc, f);
      }
      t = CONSTT;
    } else if (isletter(c)) {
      while (nc != EOF && isletter(c)) {
        name[e] = c;
        e++;
        move(&c, &nc, f);
      }
      t = IDENTIFIER;
    } else if (c == '|') {
      move(&c, &nc, f);
      move(&c, &nc, f);
      do {
        name[e++] = c;
        move(&c, &nc, f);
      } while (!(c == '|' && nc == '|'));
      move(&c, &nc, f);
      move(&c, &nc, f);
      t = STRING;
    }
    if (t) {
      using->next = (token *) toknsize;
      using = using->next;
      using->type = t;
      using->size = e;
      using->line = line;
      name[e] = '\0';
      strcpy(using->value, name);
    } else if (c == '{') {      //enft { et } c'est des ***macro***
      move(&c, &nc, f);
      using->next = (token *) toknsize;
      using = using->next;
      using->type = BALISE;
      using->size = 8;          //parce que "indicium" fait 8 caractères
      using->line = line;
      strcpy(using->value, "indicium");
    } else if (c == '}') {
      move(&c, &nc, f);
      using->next = (token *) toknsize;
      using = using->next;
      using->type = BALISE;
      using->size = 9;
      using->line = line;
      strcpy(using->value, "/indicium");
    } else {
      if (c == ' ' || c == '\n' || c == '\t') {
        line += (c == '\n');
        move(&c, &nc, f);
      } else {
        printf("Pas compris : '%c' ( place dans utf : %i)\n", c, c);
        move(&c, &nc, f);
      }
    }
  }
  fclose(f);
  return tokens->next;
}
