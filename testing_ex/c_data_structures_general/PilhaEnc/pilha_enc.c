#include <stdlib.h>
#include "pilha_enc.h"

/** Cria uma Pilha vazia */
void cria (tPilha *pilha) {
    pilha->topo = NULL;
    pilha->tam = 0;
}

/** Verifica se a Pilha está vazia*/
int vazia (tPilha pilha) {
    if (pilha.tam == 0){
        return 1;
    }
    else{
        return 0;
    }
}

/** Obtém o tamanho da Pilha*/
int tamanho (tPilha pilha) {
    return pilha.tam;

/*    tPilha *p = pilha.topo;
    int i = 0;
    while(p != NULL){
            p = p->prox;
            i++;
    }
    return i;
*/
}

/** Consulta o elemento do topo da Pilha
    A função retorna 0 se a pilha estiver vazia.
    Caso contrário, retorna 1.*/
int top (tPilha pilha, int *dado) {
    if (vazia(pilha)){
        return 0; /* Pilha vazia */
    }

    *dado = (pilha.topo)->conteudo;
    return 1;

}

/** Insere um elemento no topo da pilha.
    Retorna 0 se a memória for insuficiente.
    Caso contrário retorna 1 */
int push(tPilha *pilha, int valor) {
    tNo *novoNo; /* variavel que vai armazenar novo no*/

    /* Aloca memoria para novo no */
    novoNo = (tNo *) malloc(sizeof(tNo));
    if (novoNo == NULL){
            return 0; /* mem. insufic. */
    }

    /* Preenche o campo dado do novo no com o valor que deseja empilhar */
    novoNo->dado = valor;

    /* Faz o novo no apontar pro atual topo da pilha */
    novoNo->prox = pilha->topo;

    /* Atualiza o topo da pilha que agora sera o novo nó */
    pilha->topo = novoNo;

    /* Atualiza o tamanho da pilha */
    pilha->tam++;

    return 1;
}

/** Retira o elemento do topo da pilha.
    Retorna 0 se a pilha estiver vazia.
    Caso contrário retorna 1 */
int pop (tPilha *pilha, int *valor ) {
    tNo *p;
    if (vazia(*pilha)) {
            return 0; /* pilha vazia */
    }
    /* Guarda o no que é o atual topo da pilha */
    p = pilha->topo;
    /* Guarda o valor do topo da pilha */
    *valor = p->dado;

    /* Modifica o topo da pilha para ser o proximo elemento (2o elemento da pilha) */
    /* Isso equivale a retirar o 1o elemento (topo) da pilha */
    pilha->topo = p->prox;

    /* Decrementa o tamanho da pilha */
    pilha->tam--;

    /* Libera a memoria do elemento desempilhado (p) */
    free(p);

    return 1;
}
