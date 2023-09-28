#include <stdlib.h>
#include "filaenc.h"

/** Cria uma Fila  */
void cria (tFila *F) {
	F->inicio = NULL;
	F->fim = NULL;
	F->tam = 0;
}

/**Verifica se a Fila est� vazia */
int vazia (tFila F) {
	if (F.tam == 0)
		return 1;
	else
		return 0;
}

/** Obt�m o tamanho da Fila */
int tamanho (tFila F) {
	return F.tam;
}

/** Consulta o elemento do in�cio da fila
    Retorna 0 se a fila estiver vazia, 1 caso contr�rio
    O par�metro elem recebe o elemento in�cio */
int primeiro (tFila F, int *elem) {
	if (vazia(F))
		return 0; /*Erro: Fila vazia */

	*elem = (F.inicio)->dado;
	return 1;
}

/** Insere um elemento no fim de uma fila
    Retorna 0 se a mem. for insuficiente, 1 caso contr�rio*/
int insere (tFila *F, int valor) {
	tNo *novoNo;
	novoNo = malloc(sizeof(tNo));
	if (novoNo == NULL){
		return 0;  /* erro: mem. insuficiente */
	}

	novoNo->dado = valor;
	novoNo->prox = NULL;

    if (vazia(*F)){    /*Inser��o em fila vazia */
        F->inicio = novoNo;
        F->fim = novoNo;
    }
    else {
		(F->fim)->prox = novoNo; /* liga com a fila */
		F->fim = novoNo; /* atualiza o novo fim */
    }
    F->tam++;
    return 1;
}

/**Retira o elemento do in�cio da fila
    Retorna 0 se a fila estiver vazia, 1 caso contr�rio
    O par�metro valor ir� receber o elemento retirado */
int retira (tFila *F, int *valor) {
	tNo *p;
 	int res;

	if (vazia(*F)) {
        return 0; /*Erro: Fila vazia */
    }

	res = primeiro(*F, valor);
 	if (F->inicio == F->fim){ /* Fila com 1 elemento */
		F->fim = NULL;
    }

	p = F->inicio;
	F->inicio = p->prox;
	F->tam--;
	free(p);

	return (1);
}
