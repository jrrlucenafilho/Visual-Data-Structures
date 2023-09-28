#ifndef FILAENC_H_INCLUDED
#define FILAENC_H_INCLUDED

/* Definição da ED Fila Encadeada com Duas Cabeças */
typedef struct no {
	int dado;
	struct  no *prox;
} tNo;

typedef struct fila {
	tNo  *inicio;  /* aponta para o inicio da fila */
	tNo  *fim;   /* aponta para o fim da fila  */
	int tam;
} tFila;       /* tipo fila */

void cria (tFila *F);
int vazia (tFila F);
int tamanho(tFila F);
int primeiro (tFila F, int *dado);
int insere(tFila *F, int dado);
int retira(tFila *F, int *dado);

#endif // FILAENC_H_INCLUDED
