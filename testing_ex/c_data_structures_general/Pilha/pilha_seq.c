#include "pilha_seq.h"

/**Cria uma Pilha vazia*/
void cria(tPilha *pilha) {
    pilha->topo = -1;
}

/** Verifica se a Pilha está vazia */
int vazia(tPilha pilha) {
    if (pilha.topo == -1){
        return 1;
    }else{
        return 0;
    }
}

/** Verifica se a Pilha está cheia */
int cheia(tPilha pilha) {
    if (pilha.topo == MAX-1){
        return 1;
    }else{
        return 0;
    }
}

/** Obtém o tamanho da Pilha */
int tamanho(tPilha P) {
    return (P.topo + 1);
}

/** Consulta o elemento do topo da Pilha.
    Retorna 0 se a pilha estiver vazia, caso contrário retorna 1. */
int top(tPilha pilha, int *dado) {
    if (vazia(pilha)) {
            return 0; /* pilha vazia */
    }
    *dado = pilha.dados[pilha.topo];
    return 1;
}

/** Insere um elemento no topo da pilha.
    Retorna 0 se a pilha estiver cheia.
    Caso contrário retorna 1 */
int push(tPilha *pilha, int dado) {
    if (cheia(*pilha)){
            return 0;  /* pilha cheia */
    }
    else {
        pilha->topo++;
        pilha->dados[pilha->topo] = dado;
        return 1;
    }
}

/** Retira o elemento do topo da pilha.
    Retorna 0 se a pilha estiver vazia.
    Caso contrário retorna 1 */
int pop(tPilha *pilha, int *dado ) {
    if (vazia(*pilha)){
            return 0; /* Pilha vazia */
    }
    else {
            *dado = pilha->dados[pilha->topo];
            (pilha->topo)--;
            return 1;
    }
}

