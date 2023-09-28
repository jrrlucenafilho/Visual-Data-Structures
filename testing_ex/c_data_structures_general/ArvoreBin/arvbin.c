#include <stdio.h>
#include <stdlib.h>
#include "arvbin.h"

/**Cria uma árvore vazia */
void cria (tArvBin *T) {
	*T = NULL;
}

/**Verifica se a árvore está vazia*/
int vazia (tArvBin T) {
    if (T == NULL)
        return 1;
    else
        return 0;
}

/**Buscar um elemento na árvore
    Retorna o endereço se o elemento for
    encontrado, caso contrário retorna NULL*/
tArvBin busca(tArvBin T, int dado) {
	tArvBin achou;
	if (T == NULL)
		return NULL;  /* Arvore Vazia*/

	if(T->conteudo == dado)
		return T; /*Elem. encontrado na raiz*/

	achou = busca(T->esq, dado); /* Tenta na sub-arv da esq */
	if (achou == NULL)
		achou = busca(T->dir, dado); /* Tenta na sub-arv da dir */

	return achou;
}

/** Insere um nó raiz em uma árvore vazia
    Retorna 1 se a inserção for com sucesso.
    Caso contrário 0 */
int insereRaiz(tArvBin *T, int dado ) {
	tNo *novoNo;
	if (*T != NULL)
		return 0;  /*Erro: árvore não está vazia*/

	novoNo = malloc(sizeof(tNo));
	if (novoNo == NULL)
        return 0;  /*Err: mem.  Insuf. */

	novoNo->conteudo = dado;
	novoNo->esq = NULL;
	novoNo->dir = NULL;
	*T = novoNo;
	return 1;
}

/** Insere um filho à direita de um dado nó
    Retorna 1 se a inserção for com sucesso,
    Caso contrário 0  */
int insereDireita(tArvBin T, int vPai, int vFilho ) {
	tNo *f, *p, *novoNo;
	/*Verifica se o elemento já existe*/
	f = busca(T, vFilho);
	if (f != NULL)
        return 0;  /*Err: dado já existe*/

	/*Busca o pai e verifica se possui filho direito*/
	p = busca(T, vPai);
  	if (p == NULL)
		return 0; /*Err: pai não encontrado*/
	if (p->dir != NULL)
		return 0; /*Err: filho dir já existe*/

	novoNo = malloc(sizeof(tNo));
	if (novoNo == NULL)
		return (0);  /*Err: mem. insuf.*/

	novoNo->conteudo = vFilho;
	novoNo->esq = NULL;
	novoNo->dir = NULL;
	p->dir = novoNo;
	return 1;
}

/**Insere um filho à esquerda de um dado nó
    Retorna 1 se a inserção for com sucesso, caso contrário 0*/
int insereEsq(tArvBin T, int vPai, int vFilho ) {
	tNo *f, *p, *novoNo;
	/*Verifica se o elemento já existe*/
	f = busca(T, vFilho);
	if (f != NULL)
        return 0;  /*Err: dado já existe*/

	/*Busca o pai e verifica se possui filho da esq*/
	p = busca(T, vPai);
  	if (p == NULL)
		return 0; /*Err: pai não encontrado*/
	if (p->esq != NULL)
		return 0; /*Err: filho esq já existe*/

	novoNo = malloc(sizeof(tNo));
	if (novoNo == NULL)
		return 0;  /*Err: mem. insuf.*/

	novoNo->conteudo = vFilho;
	novoNo->esq = NULL;
	novoNo->dir = NULL;
	p->esq = novoNo;
	return 1;
}

/**Exibe o conteúdo de uma árvore em pré-ordem*/
void exibePreOrdem(tArvBin T) {
	if (T == NULL)
		return ;

	printf("%d   ", T->conteudo);
	if (T->esq != NULL)
		exibePreOrdem(T->esq);

 	if (T->dir != NULL)
		exibePreOrdem(T->dir);
}

/**Exibe o conteúdo de uma árvore em pré-ordem*/
void exibeInOrdem(tArvBin T) {
	if (T == NULL)
		return ;

	if (T->esq != NULL)
		exibeInOrdem(T->esq);

    printf("%d   ", T->conteudo);

 	if (T->dir != NULL)
		exibeInOrdem(T->dir);

}

/**Exibe o conteúdo de uma árvore em pré-ordem*/
void exibePosOrdem(tArvBin T) {
	if (T == NULL)
		return ;

	if (T->esq != NULL)
		exibePosOrdem(T->esq);
	if (T->dir != NULL)
		exibePosOrdem(T->dir);

	printf("%d   ", T->conteudo);
}


