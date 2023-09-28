#ifndef ABP_H_INCLUDED
#define ABP_H_INCLUDED

typedef struct no {
	int conteudo;  	 /* conteudo */
	struct  no *esq; /* ref. para filho da esquerda */
	struct  no *dir; /* ref. para filho da direita  */
} tNo;       /* tipo do nó */

typedef tNo *tAbp; /* tipo árvore binária de pesquisa */

void cria (tAbp *T);
int vazia (tAbp T);
tNo *busca(tNo *T, int dado);
void exibe (tAbp T);
int insere(tAbp *T, int dado);
int insere2(tAbp *T, int dado);

#endif
