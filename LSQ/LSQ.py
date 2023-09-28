# Criando class da lista

class LSQ:
    # Construtor da classe
    def __init__(self):
        # Definimos o tamanho máximo da lista
        self.tam_max = 15
        #iniciamos a variavel n_elementos
        self.n_elementos = 0
        #declaração da lista
        self.lista = []
        

    # verifica se a lista está vazia
    def lista_vazia(self):
        return self.n_elementos == 0

    # verifica se a lista está cheia
    def lista_cheia(self):
        return self.n_elementos == 15

    # retorna a quantidade de elementos na lista
    def lista_tam(self):
        return self.n_elementos

    # retorna um elemento da lista
    def elemento(self, pos):
        if self.lista_vazia() or pos < 1 or pos > self.lista_tam():
            return False
        else:
            return self.lista[pos - 1]

    # insere elementos novos na lista recebendo o valor e a posição

    def insere_dados(self, dado, pos):
        if self.lista_cheia() or pos < 1 or pos > self.tam_max + 1:
            return False
        else:
            if self.n_elementos == self.tam_max:
                return False

            # Verifica se a lista está vazia
            if self.n_elementos == 0:
                self.lista.append(dado)
            else:
                # Desloca os elementos à direita para abrir espaço para o novo dado
                # Adicione um espaço vazio no final da lista
                self.lista.append(None)
                for i in range(self.n_elementos, pos - 1, -1):
                    self.lista[i] = self.lista[i - 1]

                self.lista[pos - 1] = dado
            self.n_elementos += 1
            return True


    # metodo para remover um elemento pela posição

    def remove(self, pos):
        if pos > self.n_elementos or pos < 1:
            return False

        aux = self.lista[pos - 1]

        for i in range(pos - 1, self.n_elementos - 1):
            self.lista[i] = self.lista[i + 1]

        self.n_elementos -= 1

        return aux

    # procura o valor passado como argumento e retorna sua posição
    def posicoes(self, valor):
        posicoes = []

        for i in range(len(self.lista)):
            if self.lista[i] == valor:
                posicoes.append(i + 1)

        return posicoes

    # procura a posição passada como parâmetro e retorna o valor dessa posição
    def valor(self, indice):
        

        valor = self.lista[indice - 1]

        return valor
