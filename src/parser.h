
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
	c->bro=0;
	strcpy(c->content, tok->value);
	return c;
}
node * lastSon(node * mom){
	node * c = mom->child;
	while(c->bro) {// Chercher le tout petit
		c=c->bro;
	}
	return c;
}
void addSon(node * mom, node * new){
	if(mom->child == 0){ // si il n'y en avait pas
		mom->child = new;// il devient l'ainé

	}else{
		node * c = mom->child;
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
	node * currentNode = pile->node;
	token * newTok;
	node * newNod;
    while (tok) {
		currentNode = pile->node;
        if (tok->type == 1 && tok->value[tok->size-1]!='/') {
			// si c'est une balise, et qu'elle n'est pas autofermante
            if(tok->value[0] == '/') { // si elle se ferme
                pile = depiler(pile);
            }else{ // sinon on en ouvre une autre
				newNod = NodefromToken(tok);
				if(!strcmp(newNod->content,"indicium")){
					lastSon(currentNode)->child=newNod;
					lastSon(currentNode)->getElement=1;
				}else{
					addSon(currentNode, newNod);
				}
				pile = empiler(pile, newNod);

            }
        }else{ // sinon c'est une feuille de l'AST
			newNod = NodefromToken(tok);
            addSon(currentNode,newNod);
        }
        newTok = tok->next;
		free(tok);
		tok=newTok;
    }
    return root;
}

void printFamilly(node * root, int niv){
    for (int i = 0; i < niv; i++)printf("\033[1;3%im--|",root->type+1);
	printf("\033[0m");
    printf("%s\n",root->content ? root->content : "Empty node wth");
    node * curChild = root->child;
    while (curChild){
        printFamilly(curChild,niv+1);
        curChild = curChild->bro;
    }
}
