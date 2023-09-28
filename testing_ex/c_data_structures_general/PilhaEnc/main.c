#include <stdio.h>
#include <stdlib.h>
#include "pilha_enc.h"

int main()
{
    tPilha p1;
    int tam = 0, to = 0;

    printf("Inicio do programa \n");
    cria(&p1); /* cria a pilha p1 */

    tam = tamanho(p1);
    printf("Tamanho inicial da pilha = %d \n", tam);

    push(&p1, 10);
    push(&p1, 20);
    push(&p1, 30);
    push(&p1, 40);

    tam = tamanho(p1);
    printf("\n\nTamanho atual da pilha = %d \n", tam);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

    push(&p1, 50);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

   tam = tamanho(p1);
    printf("\n\nTamanho final da pilha = %d \n", tam);

    return 0;
}
