#include <stdio.h>
#include <stdlib.h>
#include "arvbin.h"

int main()
{
   tArvBin arv;
    tArvBin no;
    printf("Arvores Binarias!\n");

    cria(&arv);
    insereRaiz(&arv, 2);

    insereEsq(arv, 2, 4); /* insere 4 a esq do 2*/
    insereDireita(arv, 2, 6);

    insereEsq(arv, 4, 8);
    insereDireita(arv, 4, 10);

    insereEsq(arv, 6, 12);

    insereEsq(arv, 10, 14);
    insereDireita(arv, 10, 16);

    insereEsq(arv, 14, 18);
    insereDireita(arv, 14, 20);


/*    insereDireita(arv, 14, 16);
    insereEsq(arv, 14, 12);

    insereDireita(arv, 6, 8);
    insereEsq(arv, 6, 4);
    insereDireita(arv, 4, 7);

    insereEsq(arv, 12, 11);
    insereDireita(arv, 12, 13);
    insereEsq(arv, 11, 17);

    no = busca(arv, 12);
   printf("No = %d \n", no->conteudo);
*/
  
    no = busca(arv, 14);
    if (no != NULL){
        printf("No existe, conteudo = %d \n", no->conteudo);
    }

    printf("Pre-ordem \n");
    exibePreOrdem(arv);

    printf("\nIn-ordem \n");
    exibeInOrdem(arv);

    printf("\nPos-ordem \n");
    exibePosOrdem(arv);

    return 0;
}
