#include "filaseq.h"

/** Cria fila vazia */
void cria (tFila *F) {
	F->inicio = 0;
	F->fim = -1;
	F->tam = 0;
}

/** Verifica se a Fila está vazia */
int vazia (tFila F) {
	if (F.tam == 0)
		return 1;
	else
		return 0;
}

/**Verifica se a Fila está cheia */
int cheia (tFila F) {
	if (F.tam == MAX)
		return 1;
	else
		return 0;
}

/** Obtém o tamanho da Fila */
int tamanho(tFila F) {
	return (F.tam);
}

/** Consulta o elemento do início da fila.
    Retorna 0 se a fila estiver vazia, 1 caso contrário.
    O parâmetro dado irá receber o elemento do inicio */
int primeiro (tFila F, int *dado) {
	if (vazia(F))
		return 0; /*Erro: Fila vazia */
	else{
		*dado = F.item[F.inicio];
		return 1;
	}
}

/**Insere um elemento no fim de uma fila
    Retorna 0 se a fila estiver cheia, 1 caso contrário. */
int insere(tFila *F, int dado) {
	if (cheia(*F)){
		return 0;
	}

	F->fim = (F->fim + 1) % MAX; /* circularidade */
    F->item[F->fim] = dado;
	F->tam++;
	return 1;
}

/**Retira o elemento do início da fila
    Retorna 0 se a fila estiver vazia, 1 caso contrário
    O parâmetro dado irá receber o elemento retirado */
int retira(tFila *F, int *dado) {
	int res = 0;
	if (vazia(*F))
		return 0;

	res = primeiro(*F, dado);
	F->inicio = (F->inicio + 1) % MAX ; /*circularidade */
	F->tam--;
	return 1;
}



