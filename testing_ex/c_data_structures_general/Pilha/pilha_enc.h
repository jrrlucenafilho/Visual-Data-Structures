#ifndef PILHA_ENC_H_INCLUDED
#define PILHA_ENC_H_INCLUDED

typedef struct no {
    int   dado;  // informação
    struct  no *prox; // posição do topo da pilha
} tNo;       // tipo do nó

typedef tNo *tPilha; // tipo pilha




#endif // PILHA_ENC_H_INCLUDED
