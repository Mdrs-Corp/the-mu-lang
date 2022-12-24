// Construction de l'AST
bloc * empiler(bloc * head, node * new) {
    bloc * n = (bloc*) blocsize;
    n->node = new;
    n->prev = head;
    return n;
}

bloc * depiler(bloc * head){
    bloc * new = head->prev;
    free(head);
    return new;
}

node * NodefromToken(token * tok){
    node * c = (node*) nodesize;
    c->type = tok->type;
    c->size = tok->size;
    c->line = tok->line;
    c->bro = NULL;
    strcpy(c->content, tok->value);
    return c;
}

node * lastSon(node * mom){
    node * c = mom->child;
    while(c->bro) c = c->bro;
    return c;
}

void addSon(node * mom, node * new){
    if(mom->child == NULL) 
        mom->child = new;
    else
        lastSon(mom)->bro = new;
}

void printFamilly(node * rt, int niv){
    printf("%02d ",rt->line);
    for (int i = 0; i < niv; i++)printf("\033[1;3%im--|",rt->type+1);
    printf("\033[0m");
    printf("%s\n",rt->content);
    node * curChild = rt->child;
    while (curChild){
        printFamilly(curChild,niv+1);
        curChild = curChild->bro;
    }
}

node * parse(token *  tok){
    bloc * pile = (bloc*) blocsize;
    node * root = NodefromToken(tok);
    node * currentNode;
    node * newNod;
    token * newTok;
    pile->node = root;
    tok = tok -> next;
    while (tok)
    {
        currentNode = pile->node;
        if (tok->type == BALISE && tok->value[tok->size-1]!='/') 
        {
            if(tok->value[0] == '/') 
                pile = depiler(pile);
            else
            {
                newNod = NodefromToken(tok);
                if(!strcmp(newNod->content,"indicium"))
                {
                    lastSon(currentNode)->child = newNod;
                    lastSon(currentNode)->getElement = 1;
                }
                else
                    addSon(currentNode, newNod);
                pile = empiler(pile, newNod);
            }
        }else{
            newNod = NodefromToken(tok);
            addSon(currentNode,newNod);
        }
        newTok = tok->next;
        free(tok);
        tok = newTok;
    }
    return root;
}
