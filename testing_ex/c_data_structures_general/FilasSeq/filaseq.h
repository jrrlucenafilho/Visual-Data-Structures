#ifndef FILASEQ_H_INCLUDED
#define FILASEQ_H_INCLUDED

# define MAX 100

typedef struct {
	int item[MAX];
	int inicio;
	int fim;
	int tam;
} tFila;       /* tipo Fila */

void cria (tFila *F);
int vazia (tFila F);
int cheia (tFila F);
int tamanho(tFila F);
int primeiro (tFila F, int *dado);
int insere(tFila *F, int dado);
int retira(tFila *F, int *dado);

#endif // FILASEQ_H_INCLUDED
