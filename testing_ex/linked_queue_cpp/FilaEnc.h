/*
 * FilaEnc.h
 *
 *  Created on: 10 de nov. de 2022
 *      Author: Administrador
 */

#ifndef FILAENC_H_
#define FILAENC_H_

#include <stdlib.h>
#include "No.h"

class FilaEnc {

private:
	No *inicio;  // aponta para o inicio da fila
	No *fim;    	// aponta para o fim da fila
	int nElementos;

public:
	FilaEnc();
	virtual ~FilaEnc();

	bool vazia();
	int tamanho();
	int primeiro();
	bool insere(int valor);
	int remove();
};

#endif /* FILAENC_H_ */
