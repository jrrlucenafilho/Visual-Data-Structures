#include <stdio.h>
#include <stdlib.h>
#include "pilha_seq.h"

int main()
{
    tPilha p1;
    int tam = 0, to = 0, ret;

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

    top(p1, &to);
    printf("Topo da pilha atualmente = %d \n", to);

    pop(&p1, &to);
    printf("Removendo topo da pilha = %d \n", to);

    pop(&p1, &to);
    printf("Removendo topo da pilha = %d \n", to);

    push(&p1, 50);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

    pop(&p1, &to);
    printf("Topo da pilha = %d \n", to);

   tam = tamanho(p1);
    printf("Tamanho final da pilha = %d \n", tam);


    ret= top(p1, &to);
    printf("Topo da pilha atualmente = %d - %d\n", to, ret);

    return 0;
}
