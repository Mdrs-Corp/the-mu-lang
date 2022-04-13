
bloc * empiler(bloc * head, token * new){
    bloc * n =(bloc*) blocsize;
    n->tok=new;
    n->prev=head;
    return n;
}

bloc * depiler(bloc * head){
    return head->prev;
}

node * addSon(node * mom,token * tok){
    node *c = mom->child;
    if(mom->child==0){
        mom->child = (node*) nodesize;
        c = mom->child;
    }
    while(c->bro){
        c = c->bro;
    }
    c->bro = (node*) nodesize;
    c->bro->type = tok->type;
    strcpy(c->bro->content,tok->value);
    return c->bro;
}

node * parse(token *  tok){
    bloc * pile = (bloc *) blocsize;
    node * root = (node *) nodesize;
    node * currentNode = root;
    while (tok->next) {
        if (tok->type==1) {
            if((tok->value)[0]=='/'){
                pile=depiler(pile);
            }else{
                pile = empiler(pile,tok);
                currentNode = addSon(currentNode,pile->tok);
            }
        }else{
            addSon(currentNode,tok);
        }
        tok=tok->next;
    }
    return root;
}
void printFamilly(node * root, int niv){
    for (size_t i = 0; i < niv; i++) {
        printf("---|");
    }
    printf("%s\n",root->content);
    node * curChild=root->child;
    while (curChild) {
        printFamilly(curChild,niv+1);
        curChild=curChild->bro;
    }
    if (root->bro) {
        printFamilly(root->bro,niv);
    }
	for (size_t i = 0; i < niv; i++) {
        printf("---| /");
    }
	printf("\n");
}
