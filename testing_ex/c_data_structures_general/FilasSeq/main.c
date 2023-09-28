#include <stdio.h>
#include <stdlib.h>
#include "filaseq.h"

int main()
{
    int tam;
    int valor;
    tFila f1;
    printf("Inicio do programa!\n");

    cria(&f1);
    tam = tamanho(f1);
    printf("Tamanho inicial da fila = %d \n", tam);

    insere(&f1, 10);
    insere(&f1, 20);
    insere(&f1, 30);
    insere(&f1, 40);

    tam = tamanho(f1);
    printf("\n\nTamanho atual da fila = %d \n", tam);

    retira(&f1, &valor);
    printf("Removido da fila = %d \n", valor);

    retira(&f1, &valor);
    printf("Removido da fila = %d \n", valor);

    insere(&f1, 50);

    retira(&f1, &valor);
    printf("Removido da fila = %d \n", valor);

    retira(&f1, &valor);
    printf("Removido da fila = %d \n", valor);

    retira(&f1, &valor);
    printf("Removido da fila = %d \n", valor);

    return 0;
}
