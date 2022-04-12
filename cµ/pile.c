#include <stdio.h>
#include <stdlib.h>
#include "tokenizer.h"
#define blocsize malloc(sizeof(bloc))
#define nodesize malloc(sizeof(node))

typedef struct bloc{
    int type;
    char content[100];
    struct bloc * prev;
}bloc;

typedef struct node{
    int type;
    char content[100];
    struct node * child;
    struct node * bro;
}node;

bloc * empiler(bloc * head, token * new){
    bloc * n =(bloc*) blocsize;
    n->type=new->type;
    strcpy(n->content,new->value);
    n->prev=head;
    return n;
}

bloc * depiler(bloc * head){
    return head->prev;
}

node * addSon(node * mom,token * tok){
    node *c =mom->child;
    while(c->bro){
        c=c->bro;
    }
    c->bro=(node*)nodesize;
    c->bro->type=tok->type;
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
                pile=empiler(pile,tok);
                currentNode=addSon(currentNode,tok);
            }
        }else{
            addSon(currentNode,tok);
        }
        tok=tok->next;
    }
    return root;
}

int main(int argc, char const *argv[]) {
    printf("%s\n", "quidgame");
    return 0;
}
