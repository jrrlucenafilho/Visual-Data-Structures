/*
 * FilaEnc.cpp
 *
 *  Created on: 10 de nov. de 2022
 *      Author: Administrador
 */

#include "FilaEnc.h"

FilaEnc::FilaEnc() {
	inicio = NULL;
	fim = NULL;
	nElementos = 0;
}

FilaEnc::~FilaEnc() {
}


/**Verifica se a Fila está vazia */
bool FilaEnc::vazia () {
	return (nElementos == 0);
}

/** Obtém o tamanho da Fila */
int FilaEnc::tamanho () {
	return nElementos;
}

/** Consulta o elemento do início da fila
	Retorna -1 se a fila estiver vazia */
int FilaEnc::primeiro () {
	if (vazia())
		return -1; // Erro: Fila vazia

	return inicio->getConteudo();
}

/** Insere um elemento no fim de uma fila
	Retorna false se a mem. for insuficiente, true caso contrário*/
bool FilaEnc::insere (int valor) {
	No *novoNo = new No();
	novoNo->setConteudo(valor);
	novoNo->setProx(NULL);

	if (vazia()){    /*Inserção em fila vazia */
		inicio = novoNo;
	}
	else {
		fim->setProx(novoNo); /* liga com a fila */
	}

	fim = novoNo; // atualiza o novo fim
	nElementos++;
	return true;
}

/**Retira o elemento do início da fila e retorna o seu valor
	Retorna -1 se a fila estiver vazia. */
int FilaEnc::remove() {
	if (vazia())
	        return -1; // Erro: Fila vazia

	No *aux = inicio;
	int valor = inicio->getConteudo();

	if (tamanho() == 1){ // Fila com 1 elemento
		fim = NULL;
	}

	inicio = aux->getProx();

	// libera a memoria da regiao apontada por aux
	delete aux;

	nElementos--;
	return valor;
}
