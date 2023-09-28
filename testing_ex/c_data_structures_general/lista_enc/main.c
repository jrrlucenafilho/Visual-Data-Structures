#include <stdio.h>
#include <stdlib.h>
#include "listaenc.h"

#define TRUE 1
#define FALSE 0

int main()
{
    tLista minhaLista;
    int i, dado;

    cria(&minhaLista);

    if (vazia(minhaLista) == FALSE){
        printf("Lista criada nao estava vazia!\n");
    }

    insere(&minhaLista, 1, 10);
    insere(&minhaLista, 2, 20);
    insere(&minhaLista, 3, 30);
    insere(&minhaLista, 4, 40);

    insere(&minhaLista, 3, 25);
    insere(&minhaLista, 5, 35);

    printf("Pos do elemento 10 = %d \n", posicao(minhaLista, 10));
    printf("Pos do elemento 30 = %d \n", posicao(minhaLista, 30));
    printf("Pos do elemento 40 = %d \n", posicao(minhaLista, 40));

    printf("\nLista antes da remocao \n");
    for (i = 0; i < tamanho(minhaLista); i++){
        elemento(minhaLista, i+1, &dado);
        printf("%d-esimo elemento da lista = %d\n",
               i+1, dado);
    }

    remov(&minhaLista, 3, &dado);
    printf("\nDado removido = %d \n\n", dado);

    printf("Lista depois da remocao \n");
    for (i = 0; i < tamanho(minhaLista); i++){
        elemento(minhaLista, i+1, &dado);
        printf("%d-esimo elemento da lista = %d\n",
               i+1, dado);
    }
    return 0;
}

