#include <stdio.h>
#include <stdlib.h>
#include "abp.h"

int main()
{
    tAbp arv, arv2;
    tAbp no;
    printf("Arvore Binaria de Pesquisa 1!\n");

    cria(&arv);

    insere(&arv, 20);
    insere(&arv, 30);
    insere(&arv, 50);
    insere(&arv, 15);
    insere(&arv, 8);
    insere(&arv, 14);
    insere(&arv, 23);
    insere(&arv, 3);
    insere(&arv, 9);
    insere(&arv, 67);
    insere(&arv, 35);

    no = busca(arv, 20);
    if (no != NULL){
        printf("No = %d \n", no->conteudo);
        printf("No->esq = %d \n", no->esq->conteudo);
        printf("No->dir = %d \n", no->dir->conteudo);
    }else
        printf("No nao encontrado \n");

    no = busca(arv, 50);
    if (no != NULL){
        printf("No = %d \n", no->conteudo);
        printf("No->esq = %d \n", no->esq->conteudo);
        printf("No->dir = %d \n", no->dir->conteudo);
    }else
        printf("No nao encontrado \n");

    no = busca(arv, 14);
    if (no != NULL){
        printf("No = %d \n", no->conteudo);
        if (no->esq)
            printf("No->esq = %d \n", no->esq->conteudo);
        if (no->dir)
            printf("No->dir = %d \n", no->dir->conteudo);
    }else
        printf("No nao encontrado \n");

    exibe(arv);


    printf("!!!!!!!!Arvore Binaria de Pesquisa 2!\n");

    cria(&arv2);

    insere2(&arv2, 20);
    insere2(&arv2, 30);
    insere2(&arv2, 50);
    insere2(&arv2, 15);
    insere2(&arv2, 8);
    insere2(&arv2, 14);
    insere2(&arv2, 23);
    insere2(&arv2, 3);
    insere2(&arv2, 9);
    insere2(&arv2, 67);
    insere2(&arv2, 35);

    no = busca(arv2, 20);
    if (no != NULL){
        printf("No = %d \n", no->conteudo);
        printf("No->esq = %d \n", no->esq->conteudo);
        printf("No->dir = %d \n", no->dir->conteudo);
    }else
        printf("No nao encontrado \n");

    no = busca(arv2, 50);
    if (no != NULL){
        printf("No = %d \n", no->conteudo);
        printf("No->esq = %d \n", no->esq->conteudo);
        printf("No->dir = %d \n", no->dir->conteudo);
    }else
        printf("No nao encontrado \n");

    no = busca(arv2, 14);
    if (no != NULL){
        printf("No = %d \n", no->conteudo);
        if (no->esq)
            printf("No->esq = %d \n", no->esq->conteudo);
        if (no->dir)
            printf("No->dir = %d \n", no->dir->conteudo);
    }else
        printf("No nao encontrado \n");

    exibe(arv2);




    return 0;
}
