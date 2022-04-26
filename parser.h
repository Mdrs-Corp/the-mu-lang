
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
    c->size=tok->size;
	strcpy(c->content, tok->value);
	return c;
}

void addSon(node * mom, node * new){
	if(mom->child == 0){ // si il n'y en avait pas
		mom->child = new;// il devient l'ainé
	}else{
		node *c = mom->child;
		while(c->bro) {// Chercher le tout petit
			c=c->bro;
		}
		c->bro=new;// Devenir plus petit que le petit
	};
};

node * parse(token *  tok){
    bloc * pile = (bloc *) blocsize;
	node * root = NodefromToken(tok);
    pile->node = root;
	tok = tok->next;
	node * currentNode;
	token * new;
    while (tok) {
		currentNode = pile->node;
        if (tok->type == 1) { // si c'est une balise
            if(tok->value[0] == '/') { // si elle se ferme
                pile = depiler(pile);
            }else{ // sinon on en ouvre une autre
				node * new = NodefromToken(tok);
				addSon(currentNode,new);
				pile = empiler(pile, new);
            }
        }else{ // sinon c'est une feuille de l'AST
			node * n = NodefromToken(tok);
            addSon(currentNode,n);
        }
        new = tok->next;
		free(tok);
		tok=new;
    }
    return root;
}

void printFamilly(node * root, int niv){
    for (size_t i = 0; i < niv; i++)printf("---|");
    printf("%i: %s\n",root->type, root->content ? root->content : "Empty node wth");
    node * curChild = root->child;
    while (curChild){
        printFamilly(curChild,niv+1);
        curChild = curChild->bro;
    }
}
