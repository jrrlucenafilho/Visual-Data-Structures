#include <stdio.h>
#include <stdlib.h>
#include "abp.h"

/**Cria uma árvore vazia */
void cria (tAbp *T) {
	*T = NULL;
}

/**Verifica se a árvore está vazia*/
int vazia (tAbp T) {
    if (T == NULL)
        return 1;
    else
        return 0;
}

/**Buscar um elemento na ABP
    Retorna o endereço se o elemento for
    encontrado, caso contrário retorna NULL*/
/*** busca(T, 5); */
/** T originalmente eh a raiz da arvore*/
tNo *busca(tNo *T, int dado) {

	if (T == NULL)
		return NULL;  /* Arvore Vazia*/

	if(T->conteudo == dado){
		return T; /*Elem. encontrado na raiz*/
	}

	if (dado < T->conteudo){
		return busca(T->esq, dado);
    }
    else{
		return busca(T->dir, dado);
    }
}

/**Exibe o conteúdo de uma árvore no formato in-ordem
    (preserva a ordenação)*/
void exibe (tAbp T){
	if (T != NULL) {
		exibe(T->esq);
		printf("%d   ", T->conteudo);
		exibe(T->dir);
	}
}

/**Insere um nó em uma árvore ABP
    Retorna 1 se a inserção for com sucesso.
    Caso contrário retorna 0*/
int insere(tAbp *T, int dado){
	tNo *novoNo, *aux, *p;

	novoNo = malloc(sizeof(tNo));
	if (novoNo == NULL)
        return 0;

	novoNo->conteudo = dado;
	novoNo->esq = NULL;
	novoNo->dir = NULL;

	if (*T == NULL){ /* Arvore vazia*/
 		*T = novoNo;
		return 1;
	}

    /** Procura a posicao correta pra inserir o novo no */
    aux = *T;
    while (aux != NULL) {
        p = aux;
		if (dado < aux->conteudo)
			aux = aux->esq;
		else
			aux = aux->dir;
	}

	/* Encontrou um nó folha para inserir*/
	if (dado < p->conteudo){
		p->esq = novoNo;
	}else{
		p->dir = novoNo;
	}

	return 1;


}

int insere2(tAbp *T, int dado){
	tNo *novoNo, *aux;
	aux = *T;
	if (vazia(*T)){
		novoNo = malloc(sizeof(tNo));
		if (novoNo == NULL)
			return 0;

		novoNo->conteudo = dado;
		novoNo->esq = NULL;
		novoNo->dir = NULL;
		*T = novoNo;
		return 1;
	}
	else if (dado == aux->conteudo){
		return 0;
	}
	else if (dado > aux->conteudo){
		return insere(&aux->dir, dado);
	}
	else /*if (dado < aux->conteudo)*/{
		return insere(&aux->esq, dado);
	}
}

