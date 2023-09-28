#ifndef PILHA_ENC_H_INCLUDED
#define PILHA_ENC_H_INCLUDED

typedef struct no {
    int   conteudo; /* informa��o */
    struct  no *prox; /* posi��o do topo da pilha */
} tNo;       /* tipo do n� */

typedef struct{
    tNo *topo;
    int tam;
}tPilha;

void cria(tPilha *pilha);
int vazia(tPilha pilha);
int tamanho(tPilha pilha);
int top(tPilha pilha, int *dado);
int push(tPilha *pilha, int valor);
int pop(tPilha *pilha, int *valor );

#endif // PILHA_ENC_H_INCLUDED
