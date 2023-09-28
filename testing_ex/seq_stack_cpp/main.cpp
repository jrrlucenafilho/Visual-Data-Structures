
#include <iostream>
#include "PilhaSeq.h"

using namespace std;

int main() {
    int tam = 0, to = 0;

    PilhaSeq pilha = PilhaSeq();

    tam = pilha.tamanho();
    cout << "Tamanho inicial da pilha = " << tam << endl;

    pilha.push(10);
    pilha.push(20);
    pilha.push(30);
    pilha.push(40);

    tam = pilha.tamanho();
    cout << "Tamanho atual da pilha = " << tam << endl;

    to = pilha.top();
    cout << "Topo da pilha atualmente =  " << to << endl;

    to = pilha.pop();
    cout << "Removendo topo da pilha = " << to << endl;

    to = pilha.pop();
    cout << "Removendo topo da pilha = " << to << endl;

    pilha.push(50);

    to = pilha.pop();
    cout << "Removendo topo da pilha = " << to << endl;

    to = pilha.pop();
    cout << "Removendo topo da pilha = " << to << endl;

    to = pilha.pop();
    cout << "Removendo topo da pilha = " << to << endl;

    tam = pilha.tamanho();
    cout << "Tamanho final da pilha = " << tam << endl;

    to = pilha.top();
    cout << "Topo da pilha atualmente = " << to << endl;

    return 0;

}
