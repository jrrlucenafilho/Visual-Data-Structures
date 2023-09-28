#ifndef PILHA_SEQ_H_INCLUDED
#define PILHA_SEQ_H_INCLUDED

# define MAX 100  /* tamanho Máximo da Pilha */

typedef struct {
    int dados[MAX]; /* vetor que contém a Pilha */
    int topo;  /* posição do topo da Pilha */
} tPilha;      /* tipo Pilha */

void cria(tPilha *p);
int vazia(tPilha p);
int cheia(tPilha p);
int tamanho(tPilha p);
int top(tPilha p, int *d);
int push(tPilha *p, int d);
int pop(tPilha *p, int *d);



#endif // PILHA_SEQ_H_INCLUDED
