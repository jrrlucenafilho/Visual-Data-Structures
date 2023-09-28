#include <stdio.h>
#include <stdlib.h>
#include "listaenc.h"

/**Cria uma Lista vazia */
void cria (tLista *lista) {
    lista->cabeca = NULL;
    lista->tamanho = 0;
}

/** Verifica se a Lista está vazia */
int vazia (tLista lista) {
    if (lista.tamanho == 0)
        return 1;
    else
        return 0;
}

/**Obtém o tamanho da Lista*/
int tamanho (tLista lista) {
    return lista.tamanho;
    /* ou
 	  tNo *p = lista.cabeca;
	  int qtde = 0;
	  while(p != NULL){
		  p = p-> prox;
		  qtde++;
	  }
	  return qtde;
    */
}

/** Obtém o i-ésimo elemento de uma lista
    Retorna 0 se a posição passada for inválida,
    caso contrário 1. O parâmetro dado irá receber
    o elemento encontrado*/
int elemento (tLista lista, int pos, int *dado ) {
    tNo *p;
    int n = 1;

    /* Lista vazia */
    if (lista.cabeca == NULL) {
            return 0;
    }

    /* Percorre a lista do 1o elemento até pos */
    p = lista.cabeca;
    while ((p != NULL) && (n < pos)){
        /* modifica "p" para apontar para o proximo elemento da lista */
        p = p-> prox;
        n++;
    }

    /* Caso chegue-se ao final da lista, pos eh invalida */
	 if (p == NULL) {
            return 0;
     }

    *dado = p->dado;
    return 1;
}

/**Retorna a posição de um elemento pesquisado.
    Retorna 0 caso não seja encontrado */
int posicao (tLista lista, int dado) {
    int n = 1;
    tNo *p;

    /* Lista vazia */
    if ( lista.cabeca == NULL) {
            return 0;
    }

    /* Percorre a lista do inicio ao fim até encontrar o elemento*/
    p = lista.cabeca;
	while (p != NULL) {
        /* Se encontrar o elemento, retorna sua posicao n;*/
        if (p->dado == dado){
            return n;
        }

        /* modifica "p" para apontar para o proximo elemento da lista */
        p = p->prox;
        n++;
    }

    return 0;
}

/** Insere nó em lista vazia */
int insereInicioLista(tLista *lista, int valor) {
    tNo *novoNo;

    /* Aloca memoria para novo no */
    novoNo = malloc(sizeof(tNo));
    if (novoNo == NULL) { /* mem. insuf. */
		 return 0;
    }

    /* Insere novo elemento na cabeca da lista */
    novoNo->dado = valor;
    novoNo->prox = NULL;
    lista->cabeca = novoNo;
    lista->tamanho++;
    return 1;
}

/** Insere nó no meio da lista */
int insereMeioLista(tLista *lista, int pos, int dado){
    tNo *p, *novoNo;

    int n = 1;
    /* Localiza a pos. onde será inserido o novo nó */
    p = lista->cabeca;
    while ((n < pos-1) && (p != NULL)){
          p = p->prox;
          n++;
    }

    if (p == NULL) {  /* pos. inválida */
            return 0;
    }

    /* Aloca memoria para novo no */
    novoNo = malloc(sizeof(tNo));
    if (novoNo == NULL) { /* mem. insuf. */
		 return 0;
    }

    /* Insere novo elemento apos p */
    novoNo->dado = dado;
    novoNo->prox = p->prox;
    p->prox = novoNo;
    lista->tamanho++;

    return 1;
}

/** Insere nó no fim da lista */
int insereFimLista(tLista *lista, int dado){
    tNo *novoNo;

    /* Aloca memoria para novo no */
    novoNo = malloc(sizeof(tNo));
    if (novoNo == NULL) { /* mem. insuf. */
		 return 0;
    }

    novoNo->dado = dado;

    /* Procura o final da lista */
    tNo *ult = lista->cabeca;
    while(ult->prox != NULL){
        ult = ult->prox;
    }

    ult->prox = novoNo;
    novoNo->prox = NULL;
    lista->tamanho++;

    return 1;
}


/**Insere um elemento em uma determinada posição
    Retorna 0 se a lista estiver cheia ou
    a posição for inválida. Caso contrário retorna 1 */
int insere(tLista *lista, int pos, int dado ) {
    tNo *p, *novoNo;
    int  ret, tamanho = lista->tamanho;

 	/* inserção no início da lista (ou lista vazia)*/
    if ((vazia(*lista)) || (pos == 1)){
        ret = insereInicioLista(lista, dado);
        return ret;
    }
    /* inserção no fim da lista */
    else if (pos == tamanho+1){
        ret = insereFimLista(lista, dado);
        return ret;
   }
   /* inserção no meio da lista */
   else{
        ret = insereMeioLista(lista, pos, dado);
        return ret;
   }
}

/** Remove elemento do início da lista */
int removeInicioLista(tLista *lista, int *dado){
    tNo *p = lista->cabeca;

    /* dado recebe o dado removido*/
    *dado = p->dado;

    /* retira o 1o elemento da lista (p)*/
    lista->cabeca = p->prox;
    lista->tamanho--;

    /* libera a memoria da regiao apontada por p*/
    free(p);

    return 1;
}

/** Remove elemento no meio da lista */
int removeNaLista(tLista *lista, int pos, int *dado){
     tNo *aux, *p;
     int n = 1;

     /* Localiza o nó que será removido*/
     p = lista->cabeca;
     while((n < pos) && (p != NULL)){
           aux = p;
           p = p->prox;
           n++;
     }

     if (p == NULL) { /* pos. inválida */
        return (0);
     }

    /* retira o elemento da lista */
    *dado = p->dado;
     aux->prox = p->prox;
     lista->tamanho--;

    /* libera a memoria da regiao apontada por p*/
     free(p);
     return 1;
}

/**Remove um elemento de uma determinada posição
    Retorna 0 se a posição for inválida ou a lista
    estiver vazia. Caso contrário retorna 1 */
int remov (tLista *lista, int pos, int *dado ) {
    int  ret;

    /* Lista vazia */
    if (vazia(*lista)) {
            return 0;
    }

    /*remoção do elemento da cabeça da lista */
    if (pos == 1){
        ret = removeInicioLista(lista, dado);
        return ret;
    }
    /* remoção em outro lugar da lista*/
    else{
        ret = removeNaLista(lista, pos, dado);
        return ret;
    }
}
