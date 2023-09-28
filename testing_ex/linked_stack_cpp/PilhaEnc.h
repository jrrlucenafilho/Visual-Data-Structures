/*
 * PilhaEnc.h
 *
 *  Created on: 10 de nov. de 2022
 *      Author: Administrador
 */

#ifndef PILHAENC_H_
#define PILHAENC_H_

#include <stdlib.h>
#include "No.h"

class PilhaEnc {

private:
	No *topo;
	int nElementos;

public:
	PilhaEnc();
	virtual ~PilhaEnc();

	bool vazia();
	bool cheia();
	int tamanho();
	int top();
	bool push(int valor);
	int pop();

};

#endif /* PILHAENC_H_ */
