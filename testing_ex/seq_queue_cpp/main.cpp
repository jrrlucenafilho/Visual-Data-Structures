
#include <iostream>
#include "FilaSeq.h"

using namespace std;

int main() {
    int tam, valor;

    cout << "Inicio do programa!" << endl;

    FilaSeq f1 = FilaSeq();
    tam = f1.tamanho();
    cout << "Tamanho inicial da fila = " << tam << endl;

    f1.insere(10);
    f1.insere(20);
    f1.insere(30);
    f1.insere(40);

    tam = f1.tamanho();
    cout << "\n\nTamanho atual da fila = " << tam << endl;

    valor = f1.remove();
    cout << "Removido da fila = " << valor << endl;

    valor = f1.remove();
    cout << "Removido da fila = " << valor << endl;

    f1.insere(50);

    valor = f1.remove();
    cout << "Removido da fila = " << valor << endl;

    valor = f1.remove();
    cout << "Removido da fila = " << valor << endl;

    valor = f1.remove();
    cout << "Removido da fila = " << valor << endl;

}
