/*
 * PilhaEnc.cpp
 *
 *  Created on: 10 de nov. de 2022
 *      Author: Administrador
 */

#include "PilhaEnc.h"

PilhaEnc::PilhaEnc() {
	topo = NULL;
	nElementos = 0;
}

PilhaEnc::~PilhaEnc() {
}


/** Verifica se a Pilha está vazia*/
bool PilhaEnc::vazia () {
	return (nElementos == 0);
}

/** Obtém o tamanho da Pilha*/
int PilhaEnc::tamanho() {
	return nElementos;
}

/** Consulta o elemento do topo da Pilha
    Retorna -1 se a pilha estiver vazia.*/
int PilhaEnc::top (){
	if (vazia())
	 return -1; // Pilha vazia

	return topo->getConteudo();

}

/** Insere um elemento no topo da pilha.
	Retorna true se a insercao funcionar*/
bool PilhaEnc::push(int valor) {

	// Aloca memoria para novo no e preenche conteudo
	No *novoNo = new No();
	novoNo->setConteudo(valor);

	// Faz o novo no apontar pro atual topo da pilha
	novoNo->setProx(topo);

	// Atualiza o topo da pilha que agora sera o novo nó
	topo = novoNo;

	// Atualiza o tamanho da pilha
	nElementos++;
	return true;
}

/** Retira o elemento do topo da pilha.
	Retorna -1 se a pilha estiver vazia.
	Caso contrário retorna o valor removido */
int PilhaEnc::pop () {
	if (vazia())
		return -1; // pilha vazia

	// Guarda o nó que é topo da pilha e o seu conteudo
	No *p = topo;
	int valor = p->getConteudo();

	/* Modifica o topo da pilha para ser o proximo elemento (2o elemento da pilha) */
	/* Isso equivale a retirar o 1o elemento (topo) da pilha */
	topo = topo->getProx();

	// Decrementa o tamanho da pilha
	nElementos--;

	/* libera a memoria da regiao apontada por p*/
	delete p;

	return valor;
}
